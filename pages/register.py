import customtkinter as ctk
from PIL import Image, ImageTk


class RegisterWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master=master)
        self.withdraw()  # Ensure window starts hidden
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
        self.title_label = ctk.CTkLabel(self.main_frame, text="Register", font=("Century", 30, "bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Username Entry
        self.user_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Username", font=("Century", 13))
        self.user_entry.place(relx=0.5, rely=0.4, anchor="center", relwidth=0.9, relheight=0.065)

        # Password Entry
        self.pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*", font=("Century", 13))
        self.pass_entry.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.065)

        # Confirm Password Entry
        self.confirm_pass_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Confirm Password", show="*",
                                               font=("Century", 13))
        self.confirm_pass_entry.place(relx=0.5, rely=0.6, anchor="center", relwidth=0.9, relheight=0.065)

        # Back Button
        self.back_button = ctk.CTkButton(self.main_frame, text="Back", font=("Century", 15),
                                         command=self.close_register_window)
        self.back_button.place(relx=0.5, rely=0.8, anchor="center", relwidth=0.5, relheight=0.065)
        
        self.protocol("WM_DELETE_WINDOW", self.master.destroy())

    def close_register_window(self):
        self.destroy()
        self.master.deiconify()

    @staticmethod
    def center_window(width, height):
        screen_width = ctk.CTk().winfo_screenwidth()
        screen_height = ctk.CTk().winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        return f"{width}x{height}+{x}+{y}"
