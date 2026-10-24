# 导入相关库模块
import pytesseract
from PIL import Image
from pathlib import Path

eng_file_path = str(Path(__file__).parent / 'eng-img.png')
chi_img_path = Path(__file__).parent / 'chi-img.png'
# print(file_path)
# 打开一个有文字的图形
eng_im = Image.open(eng_file_path)
chi_im = Image.open(chi_img_path)
# 进行识别
# 识别英文
vtext = pytesseract.image_to_string(eng_im, lang='eng')
print(vtext)
# 识别中文，lang='chi_sim'指定用中文简体库识别图片上的文字
vtext = pytesseract.image_to_string(chi_im, lang='chi_sim')
print(vtext)