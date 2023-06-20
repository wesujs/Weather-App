import tkinter
import customtkinter
    

# System Settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Weather App")


# Adding UI Elements

title = customtkinter.CTkLabel(app, text="Insert Your City")
title.pack(padx=10, pady=10)

# Load Button

get_weather = customtkinter.CTkButton(app, text="Check Weather!", command=check_weather())

# Run App

app.mainloop()