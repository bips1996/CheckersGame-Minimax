import tkinter
from tkinter import *
import os
import random
from tkinter import messagebox


root = tkinter.Tk()
root.geometry("800x600+0+0")
root.title("Checkers")
root.configure(background = "#ddb081")

# opening the main game page on "Play" button Click
def onClick():
    root.destroy()
    os.system("python main.py")

# Closing the window on "Close" button click
def close():
    messagebox.askquestion("Confirm", "Are you sure?")
    root.destroy()

lbl = Label(
    root,
    text = "Welcome to Checkers",
    font = ("Verdana", 18),
    bg = "#ddb081",
   # fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)

btnPlay = Button(
    root,
    text = "Play",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    relief = GROOVE,
    command = onClick,
)
btnPlay.pack(pady = 40)

btnClose = Button(
    root,
    text = "Close",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = close,
)
btnClose.pack()

#default()
root.mainloop()
