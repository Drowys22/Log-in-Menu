import customtkinter as ctk
import tkinter as tk
from tkinter import font
from PIL import Image
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Login")
app.geometry("300x185")

kep = ctk.CTkImage(Image.open("Login.png"), size=(200, 200))
kep1 = ctk.CTkImage(Image.open("Login1.png"), size=(3, 200))

def LogButtonD():
    Username = Userentry.get()
    Password = Passentry.get()
    print("Pressed Log In!")
    print("---------------")
    print("Un: " + Username)
    print("Pass: " + Password)
    print("---------------")
    if Password == "Admin321":
        if Username == "Drowys":
            print("Hi admin :D")
    else:
        print("Wrong details.")

def LogAnim():
    title_label.configure(text="Login In.")
    app.after(300, LogAnim1)

def LogAnim1():
    title_label.configure(text="Login In..")
    app.after(300, LogAnim2)

def LogAnim2():
    title_label.configure(text="Login In...")
    app.after(300, LogAnim)


title_label = ctk.CTkLabel(master=app, text="Login In!", font=("Segoe UI", 28, "bold"))
title_label.place(y=10, x=20)

Userentry = ctk.CTkEntry(master=app, placeholder_text="Enter your Username!")
Userentry.place(y=70, x=15)
Passentry = ctk.CTkEntry(master=app, placeholder_text="Enter your Password!")
Passentry.place(y=110, x=15)
LogButton = ctk.CTkButton(master=app, text="Log in!", font=("Segoe UI", 15, "bold"), width=30, height=10, command=LogButtonD)
LogButton.place(y=143, x=15)
LoginImage = ctk.CTkLabel(master=app, text="", image=kep)
LoginImage.place(y=0, x=170)
LoginImage1 = ctk.CTkLabel(master=app, text="", image=kep1)
LoginImage1.place(y=0, x=167)

LogAnim()
app.mainloop()
