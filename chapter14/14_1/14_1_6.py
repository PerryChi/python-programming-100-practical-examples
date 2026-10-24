import base64
import requests
from create_audio import TestAudio
from constant import API_KEY, SECRET_KEY

vhttp = 'https://'

vurl = 'openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
base_url = vhttp + vurl % (API_KEY, SECRET_KEY)
# 获取token
def getToken(base_url):
    res = requests.post(base_url)
    return res.json()['access_token']

def SpeechToText(speech_data, token, dev_pid=1537):
    FILETYPE='wav'
    RATE = 1600
    CHANNEL = 1
    CUID = '12345678python12345678'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')
    data = {
        'format': FILETYPE,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid,
    }
    # 拼接URL地址
    url = vhttp + 'vop.baidu.com/server_api'
    headers = { 'Content-Type': 'application/json' }
    print('正在识别···')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    if 'result' in Result:
        return Result['result'][0]
    else:
        return Result

def get_audio(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data


# 主函数
if __name__ == '__main__':
    TOKEN = getToken(base_url)
    print(TOKEN)
    # message = input('按任意键开始录入')
    # test = TestAudio('test.wav')
    # test.record()
    # TOKEN = getToken(base_url)
    # speech = get_audio('test.wav')
    # result = SpeechToText(speech, TOKEN, 1537)
    # print(result)