import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from core.validators import PasswordValidation


"""
Add Show Password
Add Register Button
Add Logo at the Top
"""

class RegisterWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master=master)
        self.withdraw()  # Ensure window starts hidden
        self.title("Finance Fusion Register")
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
        self.title_label = ctk.CTkLabel(self.main_frame, text="Register", font=("Century", 30, "bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Logo
        logo = ctk.CTkImage(Image.open("./assets/logo2.png"), size=(100, 75))
        self.logo_label = ctk.CTkLabel(self.main_frame, image=logo, text="")
        self.logo_label.place(relx=0.5, rely=0.25, anchor="center")

        # Username Entry
        self.user_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Username", font=("Century", 13), corner_radius=20)
        self.user_entry.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.9, relheight=0.065)

        # Password Entry
        self.pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*", font=("Century", 13), corner_radius=20)
        self.pass_entry.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.065)

        # Confirm Password Entry
        self.confirm_pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Confirm Password", show="*",
                                               font=("Century", 13), corner_radius=20)
        self.confirm_pass_entry.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.9, relheight=0.065)

        # Show Password
        self.var = ctk.StringVar(self, "off")
        self.show_pass = ctk.CTkCheckBox(self.main_frame, width=50, text="Show Passowrd", font=("Century", 12), onvalue="on", offvalue="off", variable=self.var, command=lambda:self.showpass(self.var.get()))
        self.show_pass.place(relx=0.38, rely=0.69, anchor='e')

        # Register Button
        self.register_button = ctk.CTkButton(self.main_frame, text="Register", font=("Century", 15), corner_radius=20, command=lambda:self.pass_validation(self.pass_entry.get()))
        self.register_button.place(relx=0.5, rely=0.8, anchor='center', relwidth=0.5, relheight=0.065)

        # Back Button
        self.back_button = ctk.CTkButton(self.main_frame, text="Back", font=("Century", 15),
                                         command=self.close_register_window, corner_radius=20)
        self.back_button.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.5, relheight=0.065)

        self.wm_protocol("WM_DELETE_WINDOW", self.master.quit)
        
    def showpass(self, value):
        if value == "on":
            self.pass_entry.configure(show="")
            self.confirm_pass_entry.configure(show="")
        else:
            self.pass_entry.configure(show="*")
            self.confirm_pass_entry.configure(show="*")
    
    def pass_validation(self, value):
        password1 = self.pass_entry.get()
        password2 = self.confirm_pass_entry.get()
        if password1 == password2:
            if PasswordValidation.validate_entry(value):
                messagebox.showinfo("Berhasil Register", "Anda telah berhasil register\nSilahkan kembali ke Laman Login")
            else:
                messagebox.showwarning("Password Eror", 
                                       "Password anda tidak memenuhi kriteria :\n1. Minimal 7 hingga 15 Karakter\n2. Kombinasi Huruf Kapital dan Angka\n3.Mengandung Karakter Unik (!#@$)")
        else:
            messagebox.showwarning("Password Eror", "Password yang anda masukkan tidak sama\nSilahkan masukkan ulang")    


    def close_register_window(self):
        self.withdraw()
        self.master.deiconify()
        

    @staticmethod
    def center_window(width, height):
        screen_width = ctk.CTk().winfo_screenwidth()
        screen_height = ctk.CTk().winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        return f"{width}x{height}+{x}+{y}"
