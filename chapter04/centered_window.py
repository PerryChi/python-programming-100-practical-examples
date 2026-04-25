import tkinter as tk

# 封装一个 居中的窗口类
class CenteredWindow:
    def __init__(self, title="窗口", width=400, height=300):
        self.root = tk.Tk()
        self.root.title(title)
        self.center(width, height)
    
    def center(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def run(self):
        self.root.mainloop()

# 使用
if __name__=='__main__':
    app = CenteredWindow("我的应用", 600, 400)
    app.run()