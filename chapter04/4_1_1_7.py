# 滑动条的示例
import tkinter as tk

win = tk.Tk()
win.title('这是一个测试窗口')

var = tk.IntVar()
vlabel = tk.Label(win, text='')
vlabel.pack()

def s_select(v):
    vlabel.config(text='现在选择的数值是：' + v)

s=tk.Scale(win, label='数值', from_=0, to=10, orient=tk.HORIZONTAL, 
           length=200, showvalue=0, tickinterval=2, resolution=0.01, command=s_select)

s.pack()
win.mainloop()