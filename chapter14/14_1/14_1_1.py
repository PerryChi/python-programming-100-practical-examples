import wave
import pyaudio
from pathlib import Path

# 音频播放函数
def play_wave():
    # 通过wave对象打开一个音频文件
    # test.wav是一个测试文件，可以是任意的wav格式文件
    print(type(Path(__file__).parent / 'sample-12s.wav'))
    wf = wave.open(str(Path(__file__).parent / 'sample-12s.wav'), 'rb')
    
    # 建立pyaudio对象
    p = pyaudio.PyAudio()
    # 打开一个数据流对象，设置参数output=True
    # 可以使解码形式的音频直接通过stream播放出来，这样就可以听到声音
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    # 播放音频，使用while循环连续读取音频帧并播放
    while True:
        # 从文件中读取1024帧
        oneframe = wf.readframes(1024)
        # 当读到了空的帧，退出循环，前面用b作前缀，指明后面为二进制空串
        if (oneframe == b''):
            break
        # 把帧写入数据流，因为这个数据流是输出的，所以能立即听到声音
        stream.write(oneframe)
    # 停止数据流
    stream.stop_stream()
    # 关闭数据流
    stream.close()
    # 关闭pyaudio对象
    p.terminate()
    print('播放结束')

# 调用播放函数
play_wave()