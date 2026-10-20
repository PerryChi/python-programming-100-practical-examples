from pathlib import Path
import matplotlib.pyplot as plt

# 读入图片，test.jpg可用任意的jpg格式的文件放在当前目录下进行测试
img = plt.imread(Path(__file__).parent / 'test.jpg')
# 把表示图片数组的第三维取出最大值加上100，形成新的图片
img = img.mean(axis=2) + 100
# 设置要显示的图片
plt.imshow(img)
# 显示图片
plt.show()