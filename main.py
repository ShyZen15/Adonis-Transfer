import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk
import socket
from datetime import datetime
import os
import sqlite3

currentTime = datetime.now()

if currentTime.hour < 12:
    phase = "Morning"
elif 12 <= currentTime.hour > 18:
    phase = "Afternoon"
else:
    phase = "Evening"

host = socket.gethostbyname(socket.gethostname())
print(host)

root = tk.Tk()
root.title("Adonis Transfer")
root.geometry("500x800+728+200")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# client.connect(("localhost", 1230))



class functions():

    def Login(self, event):
        global passwordIn
        global emailWin
        global emailIn
        global canv
        obj = functions()

        def login(event):
            obj = functions()
            conn = sqlite3.connect("accounts.db")
            cur = conn.cursor()
            username = emailIn.get()
            password = passwordIn.get()
            cur.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", (username, password))
            result = cur.fetchall()
            if result == []:
                n = messagebox.showerror("Login Failed", "Invalid Credentials")

            else:
                n = messagebox.showerror(f"Success", "Login Successfully !\n" + f"Welcome back {username}")
                canv.pack_forget()
                obj.mainPage()

                conn.commit()

        canvas.pack_forget()
        canv = Canvas(root, bg="#1E1E1E", width=500, height=800)
        canv.create_image(160, 100, image=LoginText, anchor=NW)

        emailIn = Entry(
            canv,
            width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Arial", 16)
        )

        emailWin = canv.create_window(110, 250, window=emailIn, anchor=NW)

        passwordIn = Entry(
            canv, width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Arial", 16)
        )

        passwordWin = canv.create_window(110, 350, window=passwordIn, anchor=NW)

        loginBtn = canv.create_image(150, 450, image=loginImg, anchor=NW)
        BackBtn = canv.create_image(0, 10, image=backBtn, anchor=NW)
        canv.tag_bind(loginBtn, "<Button-1>", login)
        canv.tag_bind(BackBtn, "<Button-1>")

        canv.pack()

    def Register(self, event):
        global passwordIn
        global emailWin
        global emailIn
        global canv

        def register(event):
            obj = functions()
            username = emailIn.get()
            password = passwordIn.get()
            if os.path.exists("accounts.db"):
                conn = sqlite3.connect("accounts.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM accounts WHERE username = :username", {"username": username})

                exists_ = cur.fetchall()
                print(exists_)
                if exists_ == []:
                    cur.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                    n = messagebox.showerror("Success", "Account Created !")
                    canv.pack_forget()
                    obj.mainPage()

                else:
                    n = messagebox.showerror("Error", "Username already exists")
                    conn.commit()

            else:
                conn = sqlite3.connect("accounts.db")
                cur = conn.cursor()
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS accounts (
                        id INTEGER PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL
                    )
                """)

        print("Nigga")
        canvas.pack_forget()
        canv = Canvas(root, bg="#1E1E1E", width=500, height=800)
        canv.create_image(125, 100, image=RegisterText, anchor=NW)

        emailIn = Entry(
            canv, width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Inter", 16)
        )

        emailIn.insert(0, "Enter Username")


        emailWin = canv.create_window(110, 250, window=emailIn, anchor=NW)

        passwordIn = Entry(
            canv, width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Inter", 16)
        )

        passwordIn.insert(0, "Enter Password")

        passwordWin = canv.create_window(110, 350, window=passwordIn, anchor=NW)

        BackBtn = canv.create_image(0, 10, image=backBtn, anchor=NW)

        registerBtn = canv.create_image(150, 450, image=RegisterImg, anchor=NW)
        canv.tag_bind(registerBtn, "<Button-1>", register)
        canv.pack()

    def mainPage(self, event=None):
        obj = functions()
        print("Main page")
        canvas.pack_forget()

        CANVAS = Canvas(root, bg="#1E1E1E", width=500, height=800)
        CANVAS.create_image(0, 0, image=hamMenu, anchor=NW)

        CANVAS.create_text(255, 185, text=f"Good {phase}, ShyZen!", fill="white", font=("Inter", 27, "bold"))
        CANVAS.create_text(255, 270, text="Don't be a Jeffery!", fill="white", font=("Inter", 27, "bold"))
        CANVAS.create_text(255, 350, text="Send a file or Receive one now!", fill="white", font=("Inter", 27, "bold"))

        SendBtn = CANVAS.create_image(150, 450, image=sendBtn, anchor=NW)
        CANVAS.tag_bind(SendBtn, "<Button-1>", obj.sendPage)

        ReceiveBtn = CANVAS.create_image(150, 600, image=receiveBtn, anchor=NW)
        CANVAS.tag_bind(ReceiveBtn, "<Button-1>", obj.receivePage)

        CANVAS.pack()

    def sendPage(self, event):

        obj = functions()

        master = Toplevel(root)

        master.title("Adonis Transfer")
        master.geometry("500x800+728+200")
        master.resizable(False, False)
        master.configure(bg="#1E1E1E")

        canva = Canvas(master, bg="#1E1E1E", width=500, height=800)

        canva.create_rectangle(0, 0, 500, 250, fill="white")
        canva.create_image(2, 20, image=ICON, anchor=NW)

        SendBtn = canva.create_image(350, 150, image=sendImg, anchor=NW)
        selectBtn = canva.create_image(175, 150, image=select, anchor=NW)

        canva.tag_bind(selectBtn, "<Button-1>", obj.selectFile)
        canva.tag_bind(SendBtn, "<Button-1>", obj.send)

        canva.create_image(50, 350, image=circle, anchor=NW)
        canva.create_image(250, 75, image=texting, anchor=NW)

        host = socket.gethostname()

        Label(master, text=f"ID: {host}", bg="white", fg="black").place(x=160, y=470)


        canva.pack()

        master.mainloop()

    def receivePage(self, event):
        obj = functions()

        master = Toplevel(root)

        master.title("Adonis Transfer")
        master.geometry("500x800+728+200")
        master.resizable(False, False)
        master.configure(bg="#1E1E1E")


        def receiver(event):
            ID = idIn.get()
            fileName = fileIn.get()

            s = socket.socket()
            port = 5000
            s.connect((ID, port))

            file = open(fileName, "wb")
            file_data = s.recv(1024)
            file.write(file_data)
            file.close()
            print("[SUCCESS] File received successfully")


        canva = Canvas(master, bg="#1E1E1E", width=500, height=800)

        canva.create_image(165, 20, image=ICON, anchor=NW)

        canva.create_image(135, 250, image=text, anchor=NW)

        idIn = Entry(
            canva, width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Inter", 16)
        )

        idIn.insert(0, "Enter Sender ID")

        idIn.focus()

        idWin = canva.create_window(105, 350, window=idIn, anchor=NW)

        fileIn = Entry(
            canva, width=30,
            bg="#423F3F",
            fg="#FFFFFF",
            font=("Inter", 16)
        )

        fileIn.insert(0, "Enter the filename for the incoming file!")
        fileIn.focus()

        fileWin = canva.create_window(105, 450, window=fileIn, anchor=NW)

        ReceiveBtn = canva.create_image(150, 550, image=receiveBtn, anchor=NW)
        canva.tag_bind(ReceiveBtn, "<Button-1>", receiver)


        canva.pack()

    def selectFile(self, event):
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(('file_type', '*.txt'), ('all files', '*')))

    def send(self, event):
        print("hello")
        s = socket.socket()
        host = socket.gethostname()
        print(host)
        port = 5000
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("[LISTENING] for any incoming connections...")
        conn, addr = s.accept()

        file = open(filename, 'rb')

        file_data = file.read(1024)
        conn.send(file_data)
        print("[DONE] File has been transferred!")

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
RegisterText = ImageTk.PhotoImage(file="assets/RegisterText.png")
backBtn = ImageTk.PhotoImage(file="assets/Back.png")
hamMenu = ImageTk.PhotoImage(file="assets/Group 8.png")
sendBtn = ImageTk.PhotoImage(file="assets/Button/send.png")
receiveBtn = ImageTk.PhotoImage(file="assets/Button/receive.png")
sendImg = ImageTk.PhotoImage(file="assets/Button/Send1.png")
select = ImageTk.PhotoImage(file="assets/Button/receive1.png")
circle = ImageTk.PhotoImage(file="assets/Group 9.png")
texting = ImageTk.PhotoImage(file="assets/Send2.png")
text = ImageTk.PhotoImage(file="assets/Receive2.png")

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
