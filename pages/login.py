import locale
import customtkinter as ctk
import hashlib
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from ttkbootstrap.validation import *

locale.setlocale(locale.LC_ALL, '')

class LoginWindow(ttk.Window):
    def __init__(self, title="Finance Fusion Login", themename="darkly"):
        super().__init__(title, themename)
        """Set The Window Size"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width, window_height = self.screen_size(screen_height, screen_width)
        self.geometry(f"{window_width}x{window_height}")
        self.position_center()
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.main_frame = ttk.Frame(self, style='secondary')
        self.main_frame.place(relwidth=0.35, relheight=0.8, relx=0.5, rely=0.5, anchor='center')


        # Title Frame
        self.title_frame = ttk.Label(self.main_frame, text='Welcome\nFinance Fusion', font=('Century Schoolbook', 18, 'bold'), style='inverse-secondary', justify='center').pack(side='top', anchor='center', pady=20)


        # User Entry 
        self.user_title = ttk.Label(self.main_frame, text='Username', font=('Century Schoolbook', 12, 'bold'), style='inverse-secondary')
        self.user_entry = ttk.Entry(self.main_frame, font=('Century Schoolbook', 10, 'bold'))
        self.user_entry.pack(side='top', after=self.title_frame, anchor='center', fill='x', padx = 20)
        self.user_title.pack(side='top', before=self.user_entry, anchor='w', padx=20, pady=10)


        # Password Entry
        self.pass_title = ttk.Label(self.main_frame, text='Password', font=('Century Schoolbook', 12, 'bold'), style='inverse-secondary')
        self.pass_entry = ttk.Entry(self.main_frame, font=('Century Schoolbook', 10, 'bold'), show='*')
        self.pass_title.pack(side='top', after=self.user_entry, anchor='center', fill='x', padx = 20, pady = 10)
        self.pass_entry.pack(side='top', after=self.pass_title, anchor='center', fill='x', padx = 20)


        # Login & Register Button
        self.login_button = ttk.Button(self.main_frame, text='Login', width=20, style='light')
        self.regis_button = ttk.Button(self.main_frame, text='Register', width=20, style='light')
        self.regis_button.pack(side='top',after=self.pass_entry, anchor='center', pady = 10)
        self.login_button.pack(side='top',after=self.pass_entry, anchor='center',  pady=30)

    def screen_size(self, screen_height, screen_width, height_ratio=0.75, width_ratio=0.65):
        """Calcute the size of the window"""
        width = int(screen_width * width_ratio)
        height = int(screen_height * height_ratio)
        return width, height
    

if __name__ == '__main__':
    app = LoginWindow()
    app.mainloop()