import openpyxl
from pathlib import Path

# 获取当前脚本所在的目录
current_dir = Path(__file__).parent
# 拼接出 Excel 文件的完整路径
excel_path = current_dir / 'userinfo.xlsx'
# 打开一个工作簿
excel_file = openpyxl.load_workbook(excel_path)
# 取得工作簿的第一个工作表
sheet_obj = excel_file.worksheets[0]
# 打印出工作表的名字，通过title属性获得名字
print('工作表的名字是: ', sheet_obj.title)
# 取得工作表的总行数
rows_count = sheet_obj.max_row
# 取得工作表的总列数
cols_count = sheet_obj.max_column
# 打印出工作表单的函数和列数
print('工作表共有%d行, 每行有%d列'%(rows_count, cols_count))
# 打印出第二行第二列单元格中的内容
# 提示：openpyxl模块中的行列计数都是从1开始，而不是从0开始
print(sheet_obj.cell(3, 2).value)
# 下面这一句代码与上句代码是等价的，它使用的是Excel单元格表示法取得单元格的内容
print(sheet_obj['b3'].value)
