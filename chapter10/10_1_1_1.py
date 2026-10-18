# 定义一个教师类
class Teacher(object):
    # 私有变量
    __marital_status = None

    # 初始化函数
    def __init__(self, course, sex, age):
        self.course = course
        self.sex = sex
        self.age = age

    def get_capacity(self):
        return '本人是一名教授' + self.course + '的' + self.sex + '老师，现在年龄' + str(self.age) + '岁。'

    # 私有变量可通过函数对外提供变量值
    def get_marital(self):
        if self.__marital_status == True:
            return '我是一名老师，现在已结婚。'
        elif self.__marital_status == False:
            return '我是一名老师，未婚。'
        else:
            return '我是一名老师，婚姻状况保密。'


    # 私有变量可通过函数对外提供修改其变量的功能
    def set_marital(self, martital = None):
        if martital in [True, False, None]:
            self.__marital_status = martital
        else:
            raise ValueError('数据不合规范')



# 主函数main
if __name__ == '__main__':
    english_teacher = Teacher('English', '女', 26)
    info = english_teacher.get_capacity()
    print(info)
    # 调用方法取得私有变量的值
    marital_stat = english_teacher.get_marital()
    print(marital_stat)
    # 设置私有变量的值,调用对象的方法来修改私有变量的值
    english_teacher.set_marital(False)
    marital_stat = english_teacher.get_marital()
    print(marital_stat)