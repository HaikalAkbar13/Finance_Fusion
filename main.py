import customtkinter as ctk
from PIL import Image, ImageTk
from pages.login import LoginWindow
from pages.register import RegisterWindow


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.withdraw()
        
        login = LoginWindow(master=self)
        register = RegisterWindow(master=self)
        if login.winfo_exists() is not True:
            login.deiconify()
        else:
            login.focus()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()