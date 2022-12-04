from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x150")

def entryexecute():
	label.config(text=entry.get(), font="Courier 18 bold")

entry = Entry(win, width=15, fg="red")
entry.place(relx=.5, rely=.3, anchor=CENTER)

label = Label(
	win,
	text="",
	fg="red"
)
label.pack()

b1 = Button(
	win,
	text="Execute",
	bg="white",
	fg="red",
	command=entryexecute,
	width=8,
	height=1
)
b1.place(relx=.5, rely=.5, anchor=CENTER)

win.mainloop()