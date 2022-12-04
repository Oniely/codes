from tkinter import *
import tkinter.messagebox as msgbox

w = Tk()
w.title("Home Menu")
w.geometry("300x150")
w.eval("tk::PlaceWindow . center")

user = ["user"]
passw = ["pass"]


def form2():
    w.withdraw()
    w2 = Tk()
    w2.title("Login Form")
    w2.geometry("300x150")
    w2.eval("tk::PlaceWindow . center")

    global entry1, entry2

    def login():

        userlogin = entry1.get()
        passlogin = entry2.get()

        try:
            if userlogin in user and passlogin in passw:
                msgbox.showinfo("Successful!!", "Logged in Successfully!!")

                w2.destroy()
                form4()
            else:
                msgbox.showerror("Warning!!", "Username or Password do not match.")

        except NameError:
            msgbox.showerror("Error!!", "You have to register first before logging in.")

    # N
    label1 = Label(
        w2,
        text="Username: ",
    ).place(relx=.2, rely=.3, anchor=CENTER)

    label2 = Label(
        w2,
        text="Password: ",
    ).place(relx=.2, rely=.5, anchor=CENTER)

    entry1 = Entry(
        w2,
        text=""
    )
    entry1.place(relx=.6, rely=.3, anchor=CENTER)

    entry2 = Entry(
        w2,
        text=""
    )
    entry2.place(relx=.6, rely=.5, anchor=CENTER)
    # I
    btn = Button(
        w2,
        text="Login",
        command=login
    ).place(relx=.8, rely=.8, anchor=CENTER)
    
    def back():
        w.deiconify()
        w2.destroy()
    
    backBTN = Button(
        w2,
        text="Back",
        command=back
    ).pack()


def form3():
    w.withdraw()
    w3 = Tk()
    w3.title("Register Form")
    w3.geometry("300x150")
    w3.eval("tk::PlaceWindow . center")

    global ent1, ent2

    # E
    def register():
        global reg_user
        global reg_pass

        reg_user = ent1.get()
        reg_pass = ent2.get()
        
        user.append(reg_user)
        passw.append(reg_pass)

        msgbox.showinfo("Successful!!", "Registered Successfully!!")

        w3.destroy()
        w.deiconify()

        print(reg_user)
        print(reg_pass)

    label1 = Label(
        w3,
        text="Username: ",
    ).place(relx=.2, rely=.3, anchor=CENTER)

    label2 = Label(
        w3,
        text="Password: ",
    ).place(relx=.2, rely=.5, anchor=CENTER)

    ent1 = Entry(
        w3,
        text=""
    )
    ent1.place(relx=.6, rely=.3, anchor=CENTER)
    # L
    ent2 = Entry(
        w3,
        text=""
    )
    ent2.place(relx=.6, rely=.5, anchor=CENTER)

    btn = Button(
        w3,
        text="Register",
        command=register,
    ).place(relx=.8, rely=.8, anchor=CENTER)
    
    def back():
        w.deiconify()
        w3.destroy()
    
    backBTN = Button(
        w3,
        text="Back",
        command=back
    ).pack()


def form4():
    w.withdraw()
    w4 = Tk()
    w4.title("ML")
    w4.geometry("500x300")
    w4.eval("tk::PlaceWindow . center")

    label = Label(
        w4,
        text="Welcome to Mobile Legends!!",
        font="Courier 22 bold"
    ).place(relx=.5, rely=.5, anchor=CENTER)
    
    def back():
        w.deiconify()
        w4.destroy()
    
    backBTN = Button(
        w4,
        text="Back",
        command=back
    ).pack()


# ------------------------------------------------------------------------------------------------------------


registerBTN = Button(
    text="Register",
    command=form3
).place(relx=.5, rely=.3, anchor=CENTER)

loginBTN = Button(
    text="Login",
    command=form2
).place(relx=.5, rely=.5, anchor=CENTER)

w.mainloop()