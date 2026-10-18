class Person(object):
    def __init__(self):
        self.ii = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.ii += 1
        if self.ii > 10:
            # 遇到StopIteration会退出循环
            raise StopIteration()
        return '这是第' + str(self.ii) + '个实例'

    # 这个函数实现按下标取得类对象的某个属性
    def __getitem__(self, n):
        return '===这是第' + str(n) + '个实例==='

# 主函数
if __name__ == '__main__':
    for obj in Person():
        print(obj)
    obj_n = Person()
    print(obj_n[3])