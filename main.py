import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainWindow(ttk.Window):
    def __init__(self, title="ttkbootstrap", themename="darkly"):
        super().__init__(title, themename)
        self.geometry("600x600")
        button = ttk.Button(self, text="Click me!", command=lambda :print("Button Clicked!!"))
        button.pack(anchor='center')

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()