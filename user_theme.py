from decouple import config
import bcrypt
import customtkinter as ctk


class LoadingWidget(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme('dark-blue')
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")
        self.title("Finance Fusion Login")
        self.geometry(self.center_window(350, 350))

        """
        Create a Toplevel Window while connecting to database and 
        execute login logic
        """

        # UI
        self.label = ctk.CTkLabel(self, text="Please Wait\nLogin in System", font=("Century", 15, "bold"))
        self.label.place(relx=0.5, rely=0.39, anchor='center')
        
        self.progress = ctk.CTkProgressBar(self, mode="indeterminate", corner_radius=20, height=10)
        self.progress.place(relx=0.5, rely=0.5, relwidth=0.6, anchor="center")
    


    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        return f"{width}x{height}+{x}+{y}"
    

if __name__ == '__main__':
    app = LoadingWidget()
    app.mainloop()