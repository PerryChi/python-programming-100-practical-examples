# 折线图示例
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 设置字体为平方体，显示中文
rcParams['font.sans-serif'] = 'PingFang SC'
# 设置正常显示字符，防止汉字变成方程
rcParams['axes.unicode_minus'] = False

# 生成X值
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 生成10个Y值，这10个值是随机整数
y = np.random.randint(1, 100, size=10)

print(y)
# 取出y中最大值的索引值
y_index = y.argmax()
# 通过索引值取出y中的最大值
y_max = y[y_index]
# 设置尺寸
plt.figure(figsize=(9, 6))
# 画出折线
plt.plot(x, y, color='green')
# 设置x轴的坐标值为-1~15, y轴的坐标为1~100
plt.axis([-1, 25, 1, 100])
# 标识出最大值的位置
plt.annotate(
    text='这个点数值最大，最大值为: ' + str(y_max),
    xy = (y_index+1, y_max+1),
    xytext=(y_index+2, y_max+3),
    arrowprops={
        'width': 2,
        'headwidth': 6,
        'headlength':6,
        'shrink': 0.1,
        'color': 'red'
    }
)
plt.show()