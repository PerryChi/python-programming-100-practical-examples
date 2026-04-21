# 1.3.2 代码实现: 对文本进行分词

# 导入正则表达式相关的模块
import re
from pathlib import Path


def get_char(txt):
    vlist = re.split(r'[:;,.\s]\s*', txt)
    vdic_frequency = dict()

    for vachar in vlist:
        if vachar in vdic_frequency:
            vdic_frequency[vachar] += 1
        else:
            vdic_frequency[vachar] = 1
    vdic_sort = sorted(vdic_frequency.items(), key=lambda item: item[1], reverse=True)
    return vdic_sort


if __name__ == '__main__':
    file_path = Path(__file__).parent / 'test.txt'

    with open(file_path, 'r') as f:
        vtext = f.read()
    vstr = get_char(vtext)
    print('列出文本中的英文单词：\n')
    print(vstr)
