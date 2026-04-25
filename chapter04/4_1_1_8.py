from tkinter import messagebox

messagebox.showinfo(title='提示',message='你的操作是正确的')
messagebox.showwarning(title='警告', message='如果不保存关闭程序，有可能丢失数据！')
messagebox.showerror(title='操作错误', message='你录入的数据类型不正确')
messagebox.askquestion(title='请选择', message='你确定数据正确无误？')
messagebox.askyesno(title='请选择',message='是否进入下一个流程！')
messagebox.askokcancel(title='请选择', message='你是否同意这个方案')