# 按钮示例
import tkinter as tk

# 生成根窗口
win=tk.Tk()
# 设置窗口标题
win.title('这是一个测试窗口')
# 设置窗口宽380像是，高200像素
win.geometry('380x100')
# 生成一个字符型变量，这个变量将与Label控件vlabel1的text属性值绑定，
# 也就是这个变量值发生变化，vlabel1的显示文本也跟着变化
var=tk.StringVar()
# 设置一个标志vflag，当vflag=0时单击按钮显示一句话
# 当vflag=1时，单击按钮，这一句话消失
vflag=0


# 以下函数是单击按钮调用的函数
def click_it():
    # 设置vflag为公有变量
    global vflag
    if vflag == 0:
        vflag = 1
        var.set('你单击了测试按钮，再单击一下，这句话小时···')
    else:
        vflag=0
        var.set('')


# 生成按钮，单击调用click_it()函数(command=click+it)
bt=tk.Button(win, text='测 试', font=('Arial', 12), width=6,  height=1, command=click_it)
# 在窗体上放置按钮
bt.pack()

vlabel1=tk.Label(win, textvariable=var, bg='green', fg='red', font=('Arial', 12), width=5, height=2)
vlabel1.pack()
win.mainloop()