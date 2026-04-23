# 导入正则模块库
import re


class CounterWord:
    # 初始化
    def __init__(self, filename):
        # 设置要统计单词的文件名
        self.filename = filename
        self.dict_count = {}

    # 定义一个统计函数
    def count_word(self):
        # 以读取的方式打开文本文件
        with open(self.filename, 'r') as f:
            # 循环读取文件的每一行，防止因文件过大而造成卡顿
            for line in f:
                # words = []
                words = [s.lower() for s in re.findall(r"\w+", line)]
                # print(words)
                for word in words:
                    self.dict_count[word] = self.dict_count.get(word, 0) + 1

    # 取出出现次数在前num的单词
    def top_number(self, num):
        return sorted(self.dict_count.items(), key=lambda item: item[1], reverse=True)[: num]


# 主函数main
if __name__ == '__main__':
    # 生成 CounterWord 的实例对象
    counter_obj = CounterWord('2-1.py')
    counter_obj.count_word()
    num = 6
    top_num_6 = counter_obj.top_number(num)
    print('出现次数最高的{num}是：')
    for word in top_num_6:
        print(word[0], '出现次数是：', word[1])
