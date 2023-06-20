import tkinter
import customtkinter
import sys
import os
import getpass
path = 'C:/Users/Willi/Desktop/Pythons/Weather App/functions'
sys.path.append(path)

from weather_controls import *
from get_location import *

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Weather App")


# Adding UI Elements
username = getpass.getuser()
title = customtkinter.CTkLabel(app, text=f"Welcome Back, {username}!")
title.pack(padx=50, pady=50)

def button_event():
    print("button pressed")
button = customtkinter.CTkButton(app, text="CTkButton", command=button_event)

# pack the button into the window
button.pack()

# Run App

app.mainloop()