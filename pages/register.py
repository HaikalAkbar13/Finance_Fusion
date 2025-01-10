import locale
import core
import customtkinter as ctk
import ttkbootstrap as ttk 
from PIL import Image, ImageTk
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *


class RegisterWindow(ttk.Window):
    def __init__(self, title="Finance Fusion Register", themename="dark_v2", iconphoto='../assets/logo2.png'):
        super().__init__(title, themename, iconphoto)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_width, self.window_height = self.screen_size(screen_width= self.screen_width, screen_height=self.screen_height)
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.position_center()

        # Main Frame
        self.main_frame = ttk.Frame(self, style=LIGHT)
        self.main_frame.place(anchor='center', relwidth=0.6, relheight=0.7, relx=0.5, rely=0.5)

        # Logo
        logo = Image.open("../assets/logo2.png")
        resize_logo = logo.resize((65, 45), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(image=resize_logo)
        self.label_logo = ttk.Label(self.main_frame, image=self.logo, style='inverse-light')
        self.label_logo.place(relx=0.5, rely=0.15, anchor='center')

        # Title Frame
        self.title_frame = ttk.Label(self.main_frame, text='New Here?\nRegister Below!', style=(INVERSE, LIGHT), font=('Century Schoolbook', 15, 'bold'), justify='center')
        self.title_frame.place(relx=0.5, rely=0.28, anchor='center')

        # User Name
        self.label_user_name = ttk.Label(self.main_frame, style=(INVERSE, LIGHT), text='User Name', font=('Century Schoolbook', 10, 'bold'), justify='left')
        self.label_user_name.place(relx=0.19, rely=0.35, anchor='n')
        self.entry_user_name = ttk.Entry(self.main_frame, style=(SUCCESS), font=('Century Schoolbook', 8, 'bold'))
        self.entry_user_name.place(relx=0.47, rely=0.40, anchor='n', relwidth=0.8)

        # User Password
        self.label_password = ttk.Label(self.main_frame, style=(INVERSE, LIGHT), text='Password', font=('Century Schoolbook', 10, 'bold'), justify='left')
        self.label_password.place(relx=0.19, rely=0.49, anchor='n')
        self.entry_password = ttk.Entry(self.main_frame, style=(SUCCESS), font=('Century Schoolbook', 8, 'bold'), show='*', validate='focus', validatecommand=core.validators.validate_entry(self.entry_password.cget()))
        self.entry_password.place(relx=0.47, rely=0.55, anchor='n', relwidth=0.8)

        # Show Password
        self.variable_pass = ttk.BooleanVar()
        self.show_password = ttk.Checkbutton(self.main_frame, text="Show Password", variable=self.variable_pass, command=self.toggle_password_visibility)
        self.show_password.place(relx=0.09, rely=0.62)

    def toggle_password_visibility(self):
        if self.variable_pass.get():
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show='*')

    def screen_size(self, screen_width, screen_height, height_ratio=0.8, width_ratio=0.5):
        """Calculate the size of the window"""
        width = int(screen_width * width_ratio)
        height = int(screen_height * height_ratio)
        return width, height


if __name__ == '__main__':
    app = RegisterWindow()
    app.mainloop()
