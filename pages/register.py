import locale
import customtkinter as ctk
import ttkbootstrap as ttk 
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *


class RegisterWindow(ttk.Window):
    def __init__(self, title="Finance Fusion Register", themename="dark_v2"):
        super().__init__(title, themename)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_width, self.window_height = self.screen_size(self.screen_width, self.screen_height)
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.place_window_center()

        # Main Frame
        self.main_frame = ttk.Frame(self, style=LIGHT)
        self.main_frame.place(anchor='center', relwidth=0.6, relheight=0.7, relx=0.5, rely=0.5)

        # Title Frame
        self.title_frame = ttk.Label(self.main_frame, text='New Here?\nRegister Below!', style=(INVERSE,LIGHT), font=('Century Schoolbook', 15, 'bold'), justify='center')
        self.title_frame.place(relx=0.5, rely=0.4, anchor='center')

        # Logo
        logo = Image.open("../assets/logo2.png")
        resize_logo = logo.resize((75,45), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(image=resize_logo)
        self.label_logo = ttk.Label(self.main_frame, image=self.logo, style='inverse-light')
        self.label_logo.place(relx=0.5, rely=0.15, anchor='center')
    
    def screen_size(self, screen_height, screen_width, height_ratio=0.4, width_ratio=0.65):
        """Calcute the size of the window"""
        width = int(screen_width * width_ratio)
        height = int(screen_height * height_ratio)
        return width, height
    


if __name__ == '__main__':
    app = RegisterWindow()
    app.mainloop()
