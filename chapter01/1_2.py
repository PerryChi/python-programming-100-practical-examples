# 定义函数
def fab(n):
    if n <= 0:
        return '传递的参数必须是大于0的整数'
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        fab_list = [0, 1]
        for i in range(n - 2):
            # 以下语句实现后一个数等于前两个数的和
            a, b = b, a + b
            fab_list.append(b)
        return fab_list

print(fab(-11))
