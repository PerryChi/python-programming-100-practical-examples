# 布局管理 - pack布局
import tkinter as tk

win=tk.Tk()
win.title('pack布局测试')
win.geometry('500x100')

# 增加一个Frame控件当做容器，其中包含三个Button控件
frame1=tk.Frame(win)
bt1=tk.Button(frame1, text='左边', width=8)
bt1.pack(side=tk.LEFT, padx=2)
bt2=tk.Button(frame1, text='中间', width=8)
bt2.pack(side=tk.LEFT, padx=2)
bt3=tk.Button(frame1, text='右边', width=8)
bt3.pack(side=tk.LEFT, padx=2)
frame1.pack(side=tk.LEFT, fill=tk.Y, padx=6)

frame2=tk.Frame(win)
label1=tk.Label(frame2, bg='green', width=8, text='顶部')
label1.pack(side='top', anchor='w', fill='x', pady=2)
label2=tk.Label(frame2, bg='green', width=8, text='中部')
label2.pack(side='top', anchor='w', fill='x', pady=2)
label3=tk.Label(frame2, bg='green', width=8, text='下部')
label3.pack(side='top', anchor='w', fill='x', pady=2)
frame2.pack(side=tk.RIGHT)

win.mainloop()
