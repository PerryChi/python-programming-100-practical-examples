# 导入相关模块
import numpy as np

# 快速排序
def quick_sort(vlist, first, last):
    if first >= last:
        return vlist

    if first >= last:
        return vlist

    pivot = vlist[first]
    low = first
    high = last

    while low < high:
        while low < high and vlist[high] >= pivot:
            high -= 1
        vlist[low] = vlist[high]
        while low < high and vlist[low] < pivot:
            low += 1
        vlist[high] = vlist[low]

    vlist[low] = pivot

    quick_sort(vlist, first, low - 1)
    quick_sort(vlist, low + 1, last)

    return vlist


# 主函数
if __name__ == '__main__':
    test_list = np.random.randint(0, 1000, size=10)
    print('排序前: ', test_list)
    v1 = test_list.tolist()
    # test_list = [34, 65, 12, 2, 5, 7, 32, 78, 22, 1]
    sorted_list = quick_sort(v1, 0, len(v1) - 1)
    print('排序后的结果是: ', sorted_list)