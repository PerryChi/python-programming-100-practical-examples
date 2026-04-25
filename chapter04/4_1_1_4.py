# 单选按钮示例
import tkinter as tk
from tkinter import PhotoImage

# 生成根窗口
win = tk.Tk()
# 设置窗口标题
win.title('这是一个测试窗口')
# 设置窗口宽380像是，高200像素
win.geometry('380x100+100+20')
# 生成一个字符型变量，这个变量将与Label控件vlabel1的text属性值绑定，
# 也就是这个变量值发生变化，vlabel1的显示文本也跟着变化
var = tk.StringVar()
# 设置一个标志vflag，当vflag=0时单击按钮显示一句话
# 当vflag=1时，单击按钮，这一句话消失
vlabel = tk.Label(win, text='', width=60, bg='white', fg='black', font=('宋体', 14))
vlabel.pack()


def rd_select():
    vlabel.config(text='你的选择是：' + var.get())


var.set('0')

rb1 = tk.Radiobutton(win, text='Python语言', variable=var, value='Python语言', command=rd_select)
rb1.pack()
rb2 = tk.Radiobutton(win, text='Go语言', variable=var, value='Go语言', command=rd_select)
rb2.pack()
rb3 = tk.Radiobutton(win, text='C#语言', variable=var, value='C#语言', command=rd_select)
rb3.pack()

print(var.get())
# 显示窗口
win.mainloop()
