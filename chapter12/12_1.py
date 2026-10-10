# 执行二分查找法的算法函数
# 二分查找的对象必须是一个有序的集合
# 如果找到相应的元素则返回其索引位置，否则返回None
def binsearch(list, search_value):
    low_index = 0
    high_index = len(list) - 1

    while(low_index < high_index):
        mid_index = round((low_index + high_index) / 2)
        mid_value = list[mid_index]
        if (search_value == mid_value):
            return mid_index
        if (search_value < mid_value):
            high_index = mid_index + 1
        else:
            low_index = mid_index - 1

    # 循环结束，依然没有找到
    return None

# 提供一个用于测试的有序列表
test_list = [1, 2, 3, 5, 8, 33, 55, 67, 88, 99, 203, 211, 985]
# 录入要查找的数值
search_value = int(input('请录入要查找的数值: '))
vret = binsearch(test_list, search_value)

if vret:
    print('你在', test_list, '中查找：', search_value)
    print('查找结果：', search_value, '在数据集中的索引值是', vret)
else:
    print('你在', test_list, '中查找：', search_value)
    print('查找结果：未查到')

