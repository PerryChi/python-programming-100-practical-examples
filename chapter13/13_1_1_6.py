# 条形图&直方图
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 设置字体为平方体，显示中文
rcParams['font.sans-serif'] = 'PingFang SC'
# 设置正常显示字符，防止汉字变成方程
rcParams['axes.unicode_minus'] = False
# 生成10个值
# X = [10, 20, 30, 36, 50, 66, 77, 87,97, 100]
X = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 对应生成10个Y值
# Y = np.random.randint(1, 20, size=10)
Y = [70, 120, 30, 36, 52, 66, 77, 57, 97, 100]
# 设置画板尺寸
plt.figure(figsize=(9, 5))
ax1 = plt.subplot(1, 2, 1)
ax1.bar(X, Y, color="green")
plt.figtext(0.3, 0.6, s='条形图形', color='red', fontsize=12)
ax1.set_title('条形图', fontsize=16)

# 划分第二个区域
ax2 = plt.subplot(1, 2, 2)
# 随机生成1~2000中的600整数
X1 = np.random.randint(1, 2000, 600)
ax2.hist(X1, bins=9, range=[0,360], color='red', rwidth=0.6)
plt.figtext(0.7, 0.65, s='直方图例', fontsize=12)
ax2.set_title('直方图', fontsize=16)

plt.suptitle('条形图和直方图', fontsize=20, x=0.5, y=1)
plt.show()