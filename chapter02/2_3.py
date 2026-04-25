# 导入模块
import os

ret_tuple = os.walk('/Users/perrychi/.V2rayU', topdown=True)

print('\\testdir的目录结构如下所示：')

for cur_dir, list_dir, list_file in ret_tuple:
    print('当前目录结构：', cur_dir)
    print('当前目录结构：', list_dir)
    if len(list_dir) > 0:
        print('包含的子目录：', list_dir)
    if len(list_file) > 0:
        print('当前目录下的文件：', list_file)
    print('=' * 66)
