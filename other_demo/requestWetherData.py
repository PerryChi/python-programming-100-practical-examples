import json
import subprocess
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

hangzhou_cmd_str = '''
    curl --url 'https://www.nmc.cn/rest/weather?stationid=HIieJ&_=1792570829170' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'Accept-Language: zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7' \
    -H 'Connection: keep-alive' \
    -b '__nmcu=2112821227897884672' \
    -H 'Referer: https://www.nmc.cn/publish/forecast/AZJ/hangzhou.html' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'sec-ch-ua: "Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"'
  '''

try:
    result = subprocess.run(hangzhou_cmd_str, shell=True, capture_output=True, check=True)
    print(type(result.stdout))
    # # curl 返回的是字符串；将 JSON 转换为 Python 对象
    data = json.loads(result.stdout)
    passedchart = data.get('data').get('passedchart')
    print(passedchart)

    # Excel 表头：将时间放在第一列
    headers = [
        "time",
        "temperature",
        "humidity",
        "pressure",
        "windDirection",
        "windSpeed",
        "rain1h",
        "rain6h",
        "rain12h",
        "rain24h",
        "tempDiff",
    ]

    # 创建工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "过去24小时天气"

    # 写入表头
    ws.append(headers)

    # 写入天气数据
    for item in passedchart:
        row = [item.get(header, "") for header in headers]
        ws.append(row)

    # 设置表头样式
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center")

    # 冻结首行，滚动时始终显示表头
    ws.freeze_panes = "A2"

    # 开启筛选
    ws.auto_filter.ref = ws.dimensions

    # 根据内容设置列宽
    for column in ws.columns:
        max_length = max(
            len(str(cell.value)) if cell.value is not None else 0
            for cell in column
        )
        ws.column_dimensions[column[0].column_letter].width = max_length + 2

    # 保存到当前工作目录
    output_path = Path(__file__).parent / "hangzhou_weather.xlsx"
    wb.save(output_path)

    print(f"Excel 文件已保存：{output_path}")
    print(f"共写入 {len(passedchart)} 条天气记录")

except subprocess.CalledProcessError as e:
    print("curl 执行失败: ", e.stderr)
except json.JSONDecodeError as e:
    print("响应不是合法的 JSON: ", e)