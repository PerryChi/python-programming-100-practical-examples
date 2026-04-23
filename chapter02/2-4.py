# 删除目录
import os

# 删除目录的函数
def del_dir(path):
    # 取得当前目录的子目录和文件
    list_dir_file = os.listdir(path)
    # 取得目录下各项（子目录、文件）
    for file_dir in list_dir_file:
        # 每个项的路径
        down_path = os.path.join(path, file_dir)
        # 如果是目录应递归调用本身，即调用del_dir()函数积蓄判断
        if os.path.isdir(down_path):
            del_dir(down_path)
        else:
            os.remove(down_path)
    # 取当前目录下各项（重新取一次）
    list_dir_file = os.listdir(path)
    if len(list_dir_file) == 0:
        os.rmdir(path)


# 主函数
if __name__ == '__main__':
    del_path = 'testdir'

    # 判断该目录是否是文件
    if os.path.isfile(del_path):
        # 是文件直接删除
        os.remove(del_path)
    else:
        # 调用删除目录的函数
        del_dir(del_path)