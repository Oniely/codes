from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("300x175")

def get_data():
    label.config(text=entry.get(), font=("Courier 22 bold"))

entry = Entry(window, width=40)
entry.place(relx= .5, rely= .5, anchor= CENTER)

label = Label(window, text="", font=("Helvetica 16"))
label.pack()

ttk.Button(window, text="Display Text", command=get_data).place(relx= .8, rely= .5, anchor= CENTER)

window.mainloop()