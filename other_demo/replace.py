
import os

def replace_hyphen_with_underscore(directory):
    """
    递归地将指定目录下所有文件和文件夹名称中的连字符(-)替换为下划线(_)
    
    Args:
        directory: 要处理的目录路径
    """
    # 遍历目录树（自底向上避免重命名后路径失效）
    for root, dirs, files in os.walk(directory, topdown=False):
        # 处理当前目录下的所有文件
        for filename in files:
            if '-' in filename:
                new_name = filename.replace('-', '_')
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"重命名文件: {old_path} -> {new_path}")
        
        # 处理当前目录下的所有子目录
        for dirname in dirs:
            if '-' in dirname:
                new_name = dirname.replace('-', '_')
                old_path = os.path.join(root, dirname)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"重命名目录: {old_path} -> {new_path}")

# 使用示例
if __name__ == "__main__":
    target_dir = "/Users/perrychi/code/python/python-programming-100-practical-examples/chapter04"  # 请替换为实际目录路径
    replace_hyphen_with_underscore(target_dir)