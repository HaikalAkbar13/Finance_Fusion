import tkinter
from tkinter import font
import customtkinter

root_tk = customtkinter.CTk()
check_var = tkinter.StringVar("on")

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

checkbox = customtkinter.CTkCheckBox(master=root_tk, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=20, pady=10)







"""Paste this to user.py in ttk theme library
USER_THEMES = {
    "dark_v2": {
        "type": "dark",
        "colors": {
            "primary": "#31304d",
            "secondary": "#555555",
            "success": "#257180",
            "info": "#e1d7c6",
            "warning": "#ff8800",
            "danger": "#800000",
            "light": "#ADAFAE",
            "dark": "#31304d",
            "bg": "#060606",
            "fg": "#ffffff",
            "selectbg": "#5f8670",
            "selectfg": "#f0ece5",
            "border": "#060606",
            "inputfg": "#e2dad6",
            "inputbg": "#191919",
            "active": "#282828"
        }
    }
}"""

