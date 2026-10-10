# 定义冒泡排序
def bubble_sort(vlist):
    n = len(vlist)

    for i in range(0, n - 1):
        # exchange_counter用来记录内层循环中相邻元素的交换次数
        exchange_counter = 0
        for j in range(0, n - i - 1):
            if (vlist[j] > vlist[j+1]):
                vlist[j], vlist[j+1] = vlist[j+1], vlist[j]
                exchange_counter += exchange_counter + 1
        if exchange_counter == 0:
            # 如果相邻元素的交换次数为0，则说明所有元素的顺序已经符合要求了，不需继续循环了
            break
    return vlist

# 主函数
if __name__ == '__main__':
    test_list = [34, 65, 12, 2, 5, 7, 32, 78, 22, 1]
    sorted_list = bubble_sort(test_list)
    print(sorted_list)