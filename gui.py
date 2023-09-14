import tkinter
from tkinter import *
from ip_taker import *

root = tkinter.Tk()
root.geometry("600x500+300+300")
root.resizable(0,0)
root.title("Adonis Transfer")

ob = IP()

user_ip = Label(root, text=ob.getIP())
user_ip.pack()


root.mainloop()