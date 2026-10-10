# 导入相关模块
import numpy as np

# 选择排序
def insert_sort(vlist):
    n = len(vlist)

    for i in range(1, n):
        # min_index  = i
        key = vlist[i]
        j = i - 1
        while j >= 0 and key < vlist[j]:
            vlist[j + 1] = vlist[j]
            j = j - 1
        vlist[j + 1] = key

    return vlist


# 主函数
if __name__ == '__main__':
    test_list = np.random.randint(0, 1000, size=10)
    print('排序前: ', test_list)
    v1 = test_list.tolist()
    # test_list = [34, 65, 12, 2, 5, 7, 32, 78, 22, 1]
    sorted_list = insert_sort(test_list)
    print('排序后的结果是: ', sorted_list)