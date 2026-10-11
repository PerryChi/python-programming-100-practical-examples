# 导入相关模块
import numpy as np

def merge(left_list, right_list):
    left_list_index = 0
    right_list_index = 0
    result = []

    while (left_list_index < len(left_list) and right_list_index < len(right_list)):
        if left_list[left_list_index] <= right_list[right_list_index]:
            result.append(left_list[left_list_index])
            left_list_index += 1
        else:
            result.append(right_list[right_list_index])
            right_list_index += 1

    if (left_list_index < len(left_list)):
        result.extend(left_list[left_list_index:])
    if (right_list_index < len(right_list)):
        result.extend(right_list[right_list_index:])
    return result

# 归并排序
def merge_sort(vlist):
    n = len(vlist)
    if n <= 1:
        return vlist
    mid_index = n // 2
    left_list = merge_sort(vlist[:mid_index])
    right_list = merge_sort(vlist[mid_index:])
    vlist = merge(left_list, right_list)
    return vlist


# 主函数
if __name__ == '__main__':
    test_list = np.random.randint(0, 1000, size=10)
    print('排序前: ', test_list)
    v1 = test_list.tolist()
    # test_list = [34, 65, 12, 2, 5, 7, 32, 78, 22, 1]
    sorted_list = merge_sort(v1)
    print('排序后的结果是: ', sorted_list)