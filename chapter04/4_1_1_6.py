# 列表选择框 示例
import tkinter as tk

# 生成根窗口
win = tk.Tk()
# 设置窗口标题
win.title('这是一个测试窗口')
# 设置窗口宽380像是，高200像素
# 设置窗体宽高
window_width = 380
window_height = 280
# 获取屏幕尺寸
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
# 计算窗体左上角的坐标
x=(screen_width - window_width) // 2
y=(screen_height - window_height) // 2
win.geometry(f"{window_width}x{window_height}+{x}+{y}")
# 生成一个字符型变量，这个变量将与Label控件vlabel1的text属性值绑定，
# 也就是这个变量值发生变化，vlabel1的显示文本也跟着变化
var_label = tk.StringVar()
# 设置一个标志vflag，当vflag=0时单击按钮显示一句话
# 当vflag=1时，单击按钮，这一句话消失
vlabel = tk.Label(win, textvariable=var_label, bg='white', fg='black', font=('宋体', 12), width=50, height=1)

vlabel.pack()


# 点击按钮bt3后的处理函数: 在vlabel中显示选中的项
def display_select():
    try:
        print(lb.curselection())
        vsel = lb.get(lb.curselection())
        var_label.set('你选择的是：' + vsel)
    except Exception as e:
        var_label.set('你尚未选择')


# 生成按钮
bt3 = tk.Button(win, text='显示选中', font=('Arial', 10), width=6, height=1, command=display_select)
bt3.pack()

# 生成一个字符型变量
var = tk.StringVar()
var.set(('程序员', '架构师', '产品经理', '设计师'))
# 创建列表框，将变量var的值加入Listbox控件lb的选项中
lb = tk.Listbox(win, listvariable=var)
lb.pack()

# 生成一个列表变量
vlist = ['python语言', 'c#语言', 'go语言', 'php语言']

for item in vlist:
    lb.insert('end', item)

lb.insert(0, '程序员爱编程')
lb.insert(3, '产品经理爱客户')
lb.delete(6)
# 显示窗口
win.mainloop()
