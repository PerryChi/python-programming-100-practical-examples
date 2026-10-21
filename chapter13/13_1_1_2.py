from pathlib import Path
import matplotlib.pyplot as plt
# 导入设置属性的模块
from matplotlib import rcParams
import numpy as np

# 设置X为0~2π之间的数值
X = np.linspace(0, 2*np.pi)
# 设置Y1为sin(X)的函数值
Y1 = np.sin(X)
Y2 = np.cos(X)
# 设置字体为楷体 显示中文
rcParams['font.sans-serif'] = 'Kai'
# 以下设置可以正常显示字符，防止汉字变成方框
rcParams['axes.unicode_minus'] = False
# 设置画板大小，设置画板宽度为12，高度为5，单位为inch
plt.figure(figsize=(12, 5))
# 将画板区域分成1行3列，也就是画板区域可以放1*3个图形
# 第三个参数1表示第一个图形
ax1 = plt.subplot(1, 3, 1)
# 画出正弦和余弦曲线
# 可以在一个plot函数中传入多对X,Y值，实现在一个图中绘制多个图形，marker设置曲线上的点型
ax1.plot(X, Y1, X, Y2, marker='*')
# 设置图标的标题
plt.title('双曲线图形', fontsize=20)
# 设置图例标题，loc制定图例标题的位置
plt.legend(['正弦曲线', '余弦曲线'], loc='lower left')
ax1.grid(lw=1, alpha=0.2, color='gray', ls='dashed')
# ==========
# 将画板区域分成1行3列，第三个参数3表示第三个图形
# facecolor设置背景色
ax2 = plt.subplot(1, 3, 3, facecolor='white')
# 画出正弦曲线，color设置线的颜色，ls设置线型
ax2.plot(X, Y1, color='green', ls='--')
# xticks()设置x轴上刻度值，第一个参数是x轴上刻度对应的列表，第二个参数是将第一个参数中每个值对应转换成内容
# 这些值要放置在x轴上显示
plt.xticks(
    np.arange(0, 2*np.pi+0.03, np.pi/4),
    ['0', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$',],
    fontsize=10
    )
# 设置x轴坐标
plt.xlabel('数值', color='red', fontsize=16)
# 设置y轴坐标
plt.ylabel('正弦', color='red', fontsize=16, rotation=90)
# 设置图形标题
plt.title('正弦曲线图', fontsize=20)
# 保存图形，dpi设置分辨率
plt.savefig(Path(__file__).parent / '13_1_1_2.pdf', dpi=500)
# 显示
plt.show()