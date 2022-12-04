from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("OOP Activity")
win.geometry("300x175")
win.eval("tk::PlaceWindow . center")
win.config(bg="black")

def MsgBox():
    messagebox.showinfo("Hello, World!","HAPPY TEACHER DAY!",)

btn1 = Button(
    win,
    text="Show Message Box",
    command=MsgBox,
    fg="white",
    bg="darkblue"
)
btn1.pack(expand=True)

win.mainloop()