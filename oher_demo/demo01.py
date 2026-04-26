import tkinter as tk

def layout():
    # 这里直接使用 win
    bt = tk.Button(win, text='7')  # 错误！win 未定义
    bt.pack()

win = tk.Tk()  # win 在这里定义
layout()  # 调用时会报错
win.mainloop()