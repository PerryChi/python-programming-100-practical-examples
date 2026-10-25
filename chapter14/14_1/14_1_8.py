# coding=utf-8
# 百度智能云： https://console.bce.baidu.com/ai-engine/speech/overview/index?type=0
# 语音识别文档： https://cloud.baidu.com/doc/SPEECH/s/Jlbxdezuf
import base64
import time
import requests
from pathlib import Path
from constant import API_KEY, SECRET_KEY

timer = time.perf_counter

# 当前文件所在路径
CURR_PATH = Path(__file__).parent
# 需要识别的文件
AUDIO_FILE = str(CURR_PATH / 'audio/news3.m4a')  # 只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
# 文件格式
FORMAT = AUDIO_FILE[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

CUID = '123456PYTHON'
# 采样率
RATE = 16000  # 固定值

# 普通版

DEV_PID = 1537  # 1537 表示识别普通话，使用输入法模型。根据文档填写PID，选择语言及识别模型
ASR_URL = 'http://vop.baidu.com/server_api'
SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

#测试自训练平台需要打开以下信息， 自训练平台模型上线后，您会看见 第二步：“”获取专属模型参数pid:8001，modelid:1234”，按照这个信息获取 dev_pid=8001，lm_id=1234
# DEV_PID = 8001 ;   
# LM_ID = 1234 ;

# 极速版 打开注释的话请填写自己申请的appkey appSecret ，并在网页中开通极速版（开通后可能会收费）

# DEV_PID = 80001
# ASR_URL = 'http://vop.baidu.com/pro_api'
# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有极速版能力，没有请在网页里开通极速版

# 忽略scope检查，非常旧的应用可能没有
# SCOPE = False

"""  TOKEN start """
TOKEN_URL = 'http://aip.baidubce.com/oauth/2.0/token'

def fetch_token():
    params = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET_KEY
    }
    # post_data = urlencode(params)
    # post_data = post_data.encode( 'utf-8')
    res = requests.post(TOKEN_URL, params)
    json_data = res.json()
    return json_data['access_token']
"""  TOKEN end """

if __name__ == '__main__':
    token = fetch_token()

    speech_data = []
    with open(AUDIO_FILE, 'rb') as speech_file:
        speech_data = speech_file.read()

    length = len(speech_data)
    speech = base64.b64encode(speech_data)
    # speech = str(speech, 'utf-8')
    params = {
        'dev_pid': DEV_PID,
        #"lm_id" : LM_ID,    #测试自训练平台开启此项
        'format': FORMAT,
        'rate': RATE,
        'token': token,
        'cuid': CUID,
        'channel': 1,
        'speech': speech.decode('utf-8'),
        'len': length
    }
    headers = { 'Content-Type': 'application/json' }
    res = requests.post(url=ASR_URL, json=params, headers=headers)
    resp = res.json()
    txt = resp['result'][0] if 'result' in resp else 'err'
    print(txt)
    with open(CURR_PATH / "news3.txt", "w") as of:
        of.write(txt)