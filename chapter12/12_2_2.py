# 导入相关模块
import numpy as np

# 选择排序
def select_sort(vlist):
    n = len(vlist)

    for i in range(0, n - 1):
        min_index  = i
        for j in range(i + 1, n):
            if vlist[j] < vlist[min_index]:
                min_index = j
        vlist[i], vlist[min_index] = vlist[min_index], vlist[i]

    return vlist


# 主函数
if __name__ == '__main__':
    test_list = np.random.randint(0, 1000, size=100)
    print('排序前: ', test_list)
    v1 = test_list.tolist()
    sorted_list = select_sort(v1)
    print('排序后的结果是: ', sorted_list)