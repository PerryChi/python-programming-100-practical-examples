# 窗体和图片展示
import tkinter as tk
from tkinter import PhotoImage

# 建立一个根窗口
win = tk.Tk()
win.title('这是第一个窗口')
win.geometry('300x200+30+10')
lb_test = tk.Label(win, text="这是第一个窗口", font=('宋体', 12), bg='green', fg='red')
# 参数pady设置控件在纵向上的边距，一般用于飞精确位置摆放
lb_test.pack(pady=2)
# 在程序当前目录添加GIF格式的图片test.gif
# 读入图片文件
img = PhotoImage(file='./test.gif')
lb_img = tk.Label(win, image=img)
# 在窗口底部防止控件
lb_img.pack(side=tk.BOTTOM)
# 显示窗口
win.mainloop()
