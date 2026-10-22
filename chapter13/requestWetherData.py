import json
import subprocess
from pathlib import Path
from datetime import datetime
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# 设置中文字体，避免图例中的中文乱码
rcParams["font.sans-serif"] = [
    "PingFang SC",
    "Microsoft YaHei",
    "Arial Unicode MS",
]
rcParams["axes.unicode_minus"] = False

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

guangzhou_cmd_str = '''
    curl --url 'https://www.nmc.cn/rest/weather?stationid=DwzZf&_=1792576381058' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'Accept-Language: zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7' \
    -H 'Connection: keep-alive' \
    -b '__nmcu=2112821227897884672' \
    -H 'Referer: https://www.nmc.cn/publish/forecast/AGD/guangzhou.html' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Site: same-origin' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'sec-ch-ua: "Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "macOS"'
'''

def get_wether_data(cmd_str):
    try:
        result = subprocess.run(cmd_str, shell=True, capture_output=True, check=True)
        print(type(result.stdout))
        # # curl 返回的是字符串；将 JSON 转换为 Python 对象
        data = json.loads(result.stdout)
        passedchart = data.get('data').get('passedchart')
        print(passedchart)
        return passedchart
    except subprocess.CalledProcessError as e:
        print("curl 执行失败: ", e.stderr)
    except json.JSONDecodeError as e:
        print("响应不是合法的 JSON: ", e)


def plot_temperature(hz, gz):
    # 按时间升序排列，并转换时间字符串
    def prepare_data(weather_data):
        weather_data = sorted(
            weather_data,
            key=lambda item: datetime.strptime(
                item["time"], "%Y-%m-%d %H:%M"
            ),
        )

        times = [
            datetime.strptime(item["time"], "%Y-%m-%d %H:%M")
            for item in weather_data
        ]
        temperatures = [
            item["temperature"] for item in weather_data
        ]

        return times, temperatures

    hz_times, hz_temps = prepare_data(hz)
    gz_times, gz_temps = prepare_data(gz)

    # 创建画布
    fig, ax = plt.subplots(figsize=(12, 6))

    # 绘制两条折线
    ax.plot(
        hz_times,
        hz_temps,
        color="tab:blue",
        marker="o",
        markersize=4,
        linewidth=2,
        label="杭州",
    )

    ax.plot(
        gz_times,
        gz_temps,
        color="tab:orange",
        marker="s",
        markersize=4,
        linewidth=2,
        label="广州",
    )

    # 设置标题和坐标轴
    ax.set_title("杭州与广州过去24小时气温变化", fontsize=16)
    ax.set_xlabel("时间")
    ax.set_ylabel("温度（℃）")

    # 横轴每隔3小时显示一个刻度
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=3))
    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%m-%d %H:%M")
    )

    # 日期标签倾斜，避免重叠
    fig.autofmt_xdate(rotation=30)

    # 显示网格、图例
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend()

    # 自动调整布局并显示图表
    fig.tight_layout()
    plt.savefig(Path(__file__).parent / 'hangzhou&guangzhou_temperature.png', dpi=150, bbox_inches="tight")
    plt.show()

hz = get_wether_data(hangzhou_cmd_str)
gz = get_wether_data(guangzhou_cmd_str)
plot_temperature(hz, gz)