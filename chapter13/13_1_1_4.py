# 饼图示例
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体为黑体Hei，显示中文
rcParams['font.sans-serif'] = 'Hei'
# 设置正常显示字符，防止汉字变成方框
rcParams['axes.unicode_minus'] = False
# 设置图形的尺寸
plt.figure(figsize=(5, 3))
# 参数explode是列表列型，与第一个参数对应，设置每块蛇形的圆心与饼图圆心的距离（是比例值）
# 参数labels是列表类型，设置每一块扇形的标签
# 参数autopct设置比例值的显示格式
# 参数shadow为布尔值，设置饼图是否有阴影效果
plt.pie(
    [0.3, 0.42, 0.28],
    explode=[0, 0.1, 0],
    labels=['销售部','产品部','管理部'],
    autopct='%0.1f%%',
    shadow=True
)
# 设置图形标题
plt.title('各部门费用显示')
# 显示图形
plt.show()