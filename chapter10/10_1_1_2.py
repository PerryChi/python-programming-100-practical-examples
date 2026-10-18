# 定义一个类
class Person(object):
    def __init__(self, sex, age):
        self.sex = sex
        self.age = age

    # 定义一个方法（函数）
    def think(self, language = None):
        print('我是一个人，我会思考，我的母语是' + language)

    # __str__()是一个特殊函数，其作用是： 当print()函数打印该类的实例化对象时，会打印出的该函数的返回内容
    def __str__(self):
        return '我的年龄:' + str(self.age) + '，性别:' + self.sex


# 用一个类继承父类Person，这个类就是Person类的子类
class Teacher(Person):
    def think(self, language=None):
        print('我是一个教师，我会思考，我的母语是' + language)


# 主函数
if __name__ == '__main__':
    # 实例化对象
    teacher_one = Teacher('女', 18)
    # 以下语句调用Teacher类的父类Person的__str__()函数
    # 打印出：我的年龄:18, 性别:女
    print(teacher_one)
    # 应用Teacher类的函数think(),不会调用Person类的函数think
    teacher_one.think('汉语')