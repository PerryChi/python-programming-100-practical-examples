# 文本框示例
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
    print('用户名: ', (e1.get()))
    print('密  码: ', (e2.get()))

e1 = tk.Entry(win, show=None, font=('宋体', 12))
e2=tk.Entry(win, show='*', font=('Arial', 12))
e1.pack()
e2.pack()

bt=tk.Button(win,text='登录', font=(('Arial', 12)), command=click_it)
bt.pack()
win.mainloop()