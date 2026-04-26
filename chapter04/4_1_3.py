# 简单计算器 示例
import tkinter as tk

# 单击按键调用的函数
def call_command(event):
    # 取得计算器按键上的文本
    but_text = event.widget['text']
    if but_text == '=':
        try:
            result_num = str(eval(show_text.get()))
            but_text_new = result_num
        except:
            show_text.set('录入有错，请单击C键清除！')
            return
    elif but_text == 'C':
        but_text_new = ''
    else:
        but_text_new = show_text.get() + but_text
    show_text.set(but_text_new)


# 计算器按钮排列函数
def layout():
    txt = [
        '7', '8', '9', '+', 'C',
        '4', '5', '6', '-', '%',
        '1', '2', '3', '*', '=',
        '0', '.', '/'
    ]
    but_index = 0
    for i in range(1, 5):
        if but_index >= 18:
            break
        for j in range(0, 5):
            if but_index >= 18:
                break
            bt = tk.Button(win, text=txt[but_index], width=3, height=2, padx=1, pady=2)
            if txt[but_index] == '=':
                bt.config(width=3, height=5)
                bt.grid(row=i, column=j, rowspan=2)
            elif txt[but_index] == '0':
                bt.config(width=11)
                bt.grid(row=i, column=j, columnspan=2)
            elif txt[but_index] == '.' or txt[but_index] == '/':
                bt.grid(row=i, column=j + 1)
            else:
                bt.grid(row=i, column=j)
            # <Button-1>是鼠标左键单击事件，监听单击事件并绑定处理函数
            bt.bind('<Button-1>', call_command)
            but_index += 1


# 主函数
if __name__ == '__main__':
    win = tk.Tk()
    win.title('简单的计算器')
    show_text = tk.StringVar(value='')
    lab = tk.Label(win, relief=tk.SUNKEN, borderwidth=3, anchor=tk.SE, font=('Arial', 24))
    lab.configure(background='white', textvariable=show_text, height=1, width=24)
    lab.grid(row=0, column=0, columnspan=5, sticky=tk.SW)
    layout()
    win.mainloop()
