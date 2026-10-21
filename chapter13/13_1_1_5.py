# 散点图示例
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 设置字体为平方体，显示中文
rcParams['font.sans-serif'] = 'PingFang SC'
# 设置正常显示字符，防止汉字变成方程
rcParams['axes.unicode_minus'] = False
# 设置图形尺寸
plt.figure(figsize=(6, 3))
# np.random.randn()函数生成100个标准正态分布数值
# scatter()函数中第一、二个参数分别表示坐标X和Y，color指定每个点颜色值
# marker指定点的外形，这里是圆点
plt.scatter(
    np.random.randn(100),
    np.random.randn(100),
    color = np.random.rand(100, 3), 
    marker='o'
)
plt.show()