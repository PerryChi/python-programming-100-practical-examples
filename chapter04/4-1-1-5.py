
# 复选框示例
import tkinter as tk

# 生成根窗口
win = tk.Tk()
# 设置窗口标题
win.title('这是一个测试窗口')
# 设置窗口宽380像是，高200像素
win.geometry('380x100+100+20')
# 生成一个字符型变量，这个变量将与Label控件vlabel1的text属性值绑定，
# 也就是这个变量值发生变化，vlabel1的显示文本也跟着变化
var = tk.IntVar()
# 设置一个标志vflag，当vflag=0时单击按钮显示一句话
# 当vflag=1时，单击按钮，这一句话消失
vlabel = tk.Label(win, text='', width=60, bg='white', fg='black', font=('宋体', 14))
vlabel.pack()


def ck_select():
    if var.get() == 1:
        vlabel.config(text='你已经成年了。')
    else:
        vlabel.config(text='你尚未成年。')


var.set('0')

ck1 = tk.Checkbutton(win, text='满18岁', onvalue=1, offvalue=0, variable=var, command=ck_select)
ck1.pack()

print(var.get())
# 显示窗口
win.mainloop()
