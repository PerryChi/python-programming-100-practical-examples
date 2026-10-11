# 导入相关模块
import numpy as np

# 希尔排序
def shell_insert_sort(vlist):
    n = len(vlist)

    dk = n // 2
    while dk >= 1:
        for i in range(dk, n - 1):
            j = i + 1
            while j > 0:
                if vlist[j] < vlist[j - dk]:
                    vlist[j], vlist[j - dk] = vlist[j - dk], vlist[j]
                    j -= dk
                else:
                    break
        dk = dk // 2
    return vlist        

# 主函数
if __name__ == '__main__':
    test_list = np.random.randint(0, 1000, size=10)
    print('排序前: ', test_list)
    v1 = test_list.tolist()
    # test_list = [34, 65, 12, 2, 5, 7, 32, 78, 22, 1]
    sorted_list = shell_insert_sort(v1)
    print('排序后的结果是: ', sorted_list)