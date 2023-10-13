import tkinter as tk
from PIL import ImageTk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("Adonis Transfer")
root.geometry("500x800")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


class functions():
    def Login(self, event=None):
        canvas.destroy()

    def Register(self, event=None):
        print("Nigga")
        canvas.destroy()


obj = functions()

# Initialising Canvas
canvas = Canvas(root, bg="#1E1E1E", width=500, height=800)

# importing images
ICON = tk.PhotoImage(file="assets/Nigga.png")
title = ImageTk.PhotoImage(file="assets/Group 5.png")
loginImg = ImageTk.PhotoImage(file="assets/Login.png")
RegisterImg = ImageTk.PhotoImage(file="assets/Register.png")
Field = ImageTk.PhotoImage(file="assets/Rectangle 6.png")
LoginText = ImageTk.PhotoImage(file="assets/LoginText.png")

# App icon
root.iconphoto(False, ICON)

# Buttons Fr
canvas.create_image(-6, 20, image=title, anchor=NW)
loginBtn = canvas.create_image(150, 400, image=loginImg, anchor=NW)
registerBtn = canvas.create_image(150, 600, image=RegisterImg, anchor=NW)
canvas.tag_bind(loginBtn, "<Button-1>", obj.Login)
canvas.tag_bind(registerBtn, "<Button-1>", obj.Register)
canvas.pack()

root.mainloop()
