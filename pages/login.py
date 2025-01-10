from register import RegisterWindow
import locale
import customtkinter as ctk
from PIL import Image, ImageTk

locale.setlocale(locale.LC_ALL, '')


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        """Set Geometry, Theme, Icon, and Title"""
        ctk.set_default_color_theme('dark-blue')
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")
        icon = ImageTk.PhotoImage(Image.open("../assets/logo2.png"))
        self.iconphoto(True, icon)
        self.geometry(self.center_window(800, 750))

        """Set The GUI"""
        # Background
        bg = Image.open("../assets/bg.png")
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
        logo = ctk.CTkImage(Image.open("../assets/logo2.png"), size=(100, 75))
        self.logo_label = ctk.CTkLabel(self.main_frame, image=logo, text="")
        self.logo_label.place(relx=0.5, rely=0.3, anchor="center")

        # Username Entry
        self.user_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Username", font=("Century", 13))
        self.user_entry.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.065)

        # Password Entry
        self.pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*", font=("Century", 13))
        self.pass_entry.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.9, relheight=0.065)

        # Login Button
        self.login_button = ctk.CTkButton(self.main_frame, text="Login", font=("Century", 15), command=self.login_action)
        self.login_button.place(relx=0.5, rely=0.7, anchor="center", relwidth=0.5, relheight=0.065)

        # Register Button
        self.register_button = ctk.CTkButton(self.main_frame, text="Register", font=("Century", 15),
                                             command=self.open_register_window)
        self.register_button.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.5, relheight=0.065)

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
