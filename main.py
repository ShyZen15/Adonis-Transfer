import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk

root = tk.Tk()
root.title("Adonis Transfer")
root.geometry("500x800")
root.resizable(False, False)
root.configure(bg="#1E1E1E")


class functions():

    def getCred(self, event=None):
        print("NIGGA")
        print("Hello")

    def Login(self, event=None):
        obj = functions()
        canvas.pack_forget()
        canv = Canvas(root, bg="#1E1E1E", width=500, height=800)
        canv.create_image(160, 100, image=LoginText, anchor=NW)

        emailIn = Entry(
            canv, width=20,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Arial", 16)
        )

        emailWin = canv.create_window(110, 250, window=emailIn, anchor=NW)

        passwordIn = Entry(
            canv, width=20,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Arial", 16)
        )

        passwordWin = canv.create_window(110, 350, window=passwordIn, anchor=NW)
        
        loginBtn = canv.create_image(150, 450, image=loginImg, anchor=NW)
        canv.tag_bind(loginBtn, "<Button-1>", obj.getCred)

        canv.pack()

    def Register(self, event=None):
        print("Nigga")
        canvas.destroy()


obj = functions()

# Initialising Canvas
canvas = Canvas(root, bg="#1E1E1E", width=500, height=800)

# importing images
ICON = tk.PhotoImage(file="assets/Nigga.png")
titleIMG = ImageTk.PhotoImage(file="assets/Group 5.png")
loginImg = ImageTk.PhotoImage(file="assets/Login.png")
RegisterImg = ImageTk.PhotoImage(file="assets/Register.png")
Field = ImageTk.PhotoImage(file="assets/Rectangle 6.png")
LoginText = ImageTk.PhotoImage(file="assets/LoginText.png")

# App icon
root.iconphoto(False, ICON)

# Buttons Fr
title = canvas.create_image(-6, 20, image=titleIMG, anchor=NW)
loginBtn = canvas.create_image(150, 400, image=loginImg, anchor=NW)
registerBtn = canvas.create_image(150, 600, image=RegisterImg, anchor=NW)
canvas.tag_bind(loginBtn, "<Button-1>", obj.Login)
canvas.tag_bind(registerBtn, "<Button-1>", obj.Register)

canvas.pack()

root.mainloop()
