from .register import RegisterWindow
import locale
import customtkinter as ctk
from PIL import Image, ImageTk

locale.setlocale(locale.LC_ALL, '')


class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master=master)
        self.withdraw()
        """Set Geometry, Theme, Icon, and Title"""
        ctk.set_default_color_theme('dark-blue')
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")
        self.title("Finance Fusion Login")
        self.geometry(self.center_window(800, 750))

        """Set The GUI"""
        # Background
        bg = Image.open("./assets/bg.png")
        img_bg = ctk.CTkImage(dark_image=bg, size=(800, 750))
        self.bg_label = ctk.CTkLabel(self, image=img_bg, text="")
        self.bg_label.pack(fill="both", expand=True)

        # Main Frame
        self.main_frame = ctk.CTkFrame(self.bg_label, corner_radius=10)
        self.main_frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.7, anchor="center")

        # Title Label
        self.title_label = ctk.CTkLabel(self.main_frame, text="Finance Fusion", font=("Century", 30, "bold"))
        self.title_label.place(relx=0.5, rely=0.15, anchor="center")

        # Logo
        logo = ctk.CTkImage(Image.open("./assets/logo2.png"), size=(100, 75))
        self.logo_label = ctk.CTkLabel(self.main_frame, image=logo, text="")
        self.logo_label.place(relx=0.5, rely=0.3, anchor="center")

        # Username Entry
        self.user_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Username", font=("Century", 13), corner_radius=20)
        self.user_entry.place(relx=0.5, rely=0.45, anchor="center", relwidth=0.9, relheight=0.065)

        # Password Entry
        self.pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*", font=("Century", 13), corner_radius=20)
        self.pass_entry.place(relx=0.5, rely=0.55, anchor="center", relwidth=0.9, relheight=0.065)

        # Show Password
        self.var = ctk.StringVar(self, "off")
        self.show_pass = ctk.CTkCheckBox(self.main_frame, width=50, text="Show Password", font=("Century", 11), onvalue="on", offvalue="off", variable=self.var, command=lambda:self.showpass(self.var.get()))
        self.show_pass.place(relx=0.36, rely=0.62, anchor='e')

        # Login Button
        self.login_button = ctk.CTkButton(self.main_frame, text="Login", font=("Century", 15), command=self.login_action, corner_radius=20)
        self.login_button.place(relx=0.5, rely=0.75, anchor="center", relwidth=0.5, relheight=0.065)

        # Register Button
        self.register_button = ctk.CTkButton(self.main_frame, text="Register", font=("Century", 15),
                                             command=self.open_register_window, corner_radius=20)
        self.register_button.place(relx=0.5, rely=0.85, anchor="center", relwidth=0.5, relheight=0.065)
        self.wm_protocol("WM_DELETE_WINDOW", self.master.quit)

    def showpass(self, value):
        if value == "on":
            self.pass_entry.configure(show="")
        else:
            self.pass_entry.configure(show="*")

    def login_action(self):
        print("Login logic here.")

    def open_register_window(self):
        self.withdraw()  # Hide current window
        register_window = RegisterWindow(self)
        register_window.deiconify()


    @staticmethod
    def center_window(width, height):
        screen_width = ctk.CTk().winfo_screenwidth()
        screen_height = ctk.CTk().winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        return f"{width}x{height}+{x}+{y}"


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
