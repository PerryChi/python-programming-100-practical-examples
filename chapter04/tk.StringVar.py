# tk.StringVar()的基本用法和双向绑定示例
import tkinter as tk

root = tk.Tk()

# 创建 StringVar 变量
text_var = tk.StringVar()
text_var.set("初始文本")      # 设置值
print(text_var.get())         # 获取值：初始文本

# 真实场景下应该还要增加防抖机制
def on_change(*args):
    print(f"输入内容: {text_var.get()}")
# 监听变量变化
text_var.trace_add('write', on_change)


# 绑定到 Label（自动显示变量值）
label = tk.Label(root, textvariable=text_var)
label.pack()

# 绑定到 Entry（自动双向同步）
entry = tk.Entry(root, textvariable=text_var)
entry.pack()

root.mainloop()