
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 设置 X 为 0～2π 之间的数值
X = np.linspace(0, 2 * np.pi)

# 设置 Y1、Y2 为正弦和余弦函数值
Y1 = np.sin(X)
Y2 = np.cos(X)

# 设置字体为楷体，显示中文
rcParams['font.sans-serif'] = ['Kai']
rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(12, 5))

# 第一个子图：同时绘制正弦曲线和余弦曲线
ax1 = plt.subplot(1, 2, 1)
ax1.plot(X, Y1, X, Y2, marker='*')
ax1.set_title('双曲线图形', fontsize=20)
ax1.legend(['正弦曲线', '余弦曲线'], loc='lower left')
ax1.grid(lw=1, alpha=0.2, color='gray', ls='dashed')

# 第二个子图：绘制正弦曲线
ax2 = plt.subplot(1, 2, 2, facecolor='white')
ax2.plot(X, Y1, color='green', ls='--')

# 设置 X 轴刻度和标签
ticks = np.arange(0, 2 * np.pi + 0.03, np.pi / 4)
labels = [
    '0',
    r'$\pi/4$',
    r'$\pi/2$',
    r'$3\pi/4$',
    r'$\pi$',
    r'$5\pi/4$',
    r'$3\pi/2$',
    r'$7\pi/4$',
    r'$2\pi$',
]
ax2.set_xticks(ticks, labels, fontsize=10)

ax2.set_xlabel('数值', color='red', fontsize=16)
ax2.set_ylabel('正弦', color='red', fontsize=16, rotation=90)
ax2.set_title('正弦曲线图', fontsize=20)

# 保存 PDF 文件到当前 Python 源码所在目录
plt.savefig(
    Path(__file__).parent / '13_1_1_3.pdf',
    dpi=500,
    bbox_inches='tight'
)

# 显示图形
plt.show()
