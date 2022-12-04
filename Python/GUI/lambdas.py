from tkinter import *

form = Tk()
form.geometry("300x150")
form.eval("tk::PlaceWindow . center")

def fullname(fname, lname):
	print(fname, lname)

entry1 = Entry(
	form,
	text=""
	)
entry1.pack()


entry2 = Entry(
	form,
	text=""
	)
entry2.pack()


btn1 = Button(
	form,
	text="Execute Function1",
	command=lambda: fullname(entry1.get(), entry2.get())
	).pack(expand=True)



form.mainloop()