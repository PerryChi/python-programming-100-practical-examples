import wave
import pyaudio
from pathlib import Path

# 设置录音时间
RECORD_SECONDS = 8
# 设置PyAudio内置缓存大小
CHUNK = 1024
# 设置量化位数，这里设置量化位数是16bit，2字节
FORMAT = pyaudio.paInt16
# 设置声道数
CHANNELS = 1
# 设置采样率
RATE = 16000

# 音频播放函数
def record_wave():
    # 建立pyaudio对象
    p = pyaudio.PyAudio()
    # 打开一个数据流对象，设置参数output=True
    # 可以使解码形式的音频直接通过stream播放出来，这样就可以听到声音
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    print('开始录音···')
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print('结束录音')
    # 关闭stream数据流对象
    stream.stop_stream()
    stream.close()
    # 停止PyAudio对象
    p.terminate()
    # 以下语句把列表frames中的数据写入文件test1.wav
    wf = wave.open(str(Path(__file__).parent / 'test1.wav'), 'wb')
    # 设置wave文件的声道数
    wf.setnchannels(CHANNELS)
    # 设置wave文件的量化位数
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # 设置wave文件的采样率
    wf.setframerate(RATE)
    # 把列表中数据写入文件
    wf.writeframes(b''.join(frames))
    wf.close()
    print('录制结束')

# 调用播放函数
record_wave()