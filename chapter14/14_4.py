# 导入所需模块
import requests
import base64
from pathlib import Path
from constant import API_Key, Secret_Key

# 百度智能云
# 文字识别服务: https://console.bce.baidu.com/ai-engine/ocr/overview/index?type=2
# 车牌识别文档: https://cloud.baidu.com/doc/OCR/s/ck3h7y191

# 车牌识别函数
def getToken():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res_json = response.json()
    # print(res_json)
    return res_json['access_token']

# 图文识别函数
def character_recognition(filename, access_token):
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    # 二进制方式打开图片文件
    f = open(filename, 'rb')
    img = base64.b64encode(f.read())
    params = { 'image': img }
    response = requests.post(request_url, headers=headers, data=params)
    res = response.json()
    if 'number' in res ['words_result']:
        return res['words_result']['number']
    else:
        return res


# 主函数
if __name__ == '__main__':
    vtoken = getToken()
    print(vtoken)
    img_path = str(Path(__file__).parent / 'car_plate.jpeg')
    # img_path = str(Path(__file__).parent / 'car_plates.jpg')
    result = character_recognition(img_path, vtoken)
    print(f'识别出来的车牌为: {result}')
