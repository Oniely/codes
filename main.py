from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox
import mysql.connector as mysql
from tkcalendar import DateEntry

conn = mysql.connect(
    host="localhost",
    database="southlandDB",
    user="root",
    password="qwerty"
)
cursor = conn.cursor()


w = Tk()
w.title("Window 1")
w.geometry("1000x300")


def insert_db():
    sql = "INSERT INTO customer (id, fullname, course, years, date_purchase) VALUES (%s, %s, %s, %s, %s)"
    val = (ent1.get(), ent2.get(), ent3.get(), ent4.get(), date.get_date())

    cursor.execute(sql, val)
    conn.commit()

    print("Successfully Added a New Student.")


lbl1 = Label(
    w,
    text="ID: "
)
lbl1.grid(row=0, column=0, padx=20, pady=5)
ent1 = Entry(
    w,
    text=""
)
ent1.grid(row=0, column=1, padx=20, pady=5)

lbl2 = Label(
    w,
    text="Fullname: "
)
lbl2.grid(row=1, column=0, padx=20, pady=5)
ent2 = Entry(
    w,
    text=""
)
ent2.grid(row=1, column=1, padx=20, pady=5)

lbl3 = Label(
    w,
    text="Course: "
)
lbl3.grid(row=2, column=0, padx=20, pady=5)
ent3 = Entry(
    w,
    text=""
)
ent3.grid(row=2, column=1, padx=20, pady=5)

lbl4 = Label(
    w,
    text="Year: "
)
lbl4.grid(row=3, column=0, padx=20, pady=5)
ent4 = Entry(
    w,
    text=""
)
ent4.grid(row=3, column=1, padx=20, pady=5)

lbl5 = Label(
    w,
    text="Date: "
)
lbl5.grid(row=4, column=0, padx=20, pady=5)
date = DateEntry(
    w,
    selectmode="day",
    year=2022,
    month=12,
    day=22
)
date.grid(row=4, column=1, padx=20, pady=5)

btn = ttk.Button(
    w,
    text="Save",
    width=10,
    command=insert_db
)
btn.grid(row=5, column=1, padx=50, pady=10)

table = ttk.Treeview(
    w,
    selectmode="browse"
)

# Defining Columns
table["columns"] = ("ID", "Fullname", "Course", "Year", "Date Purchased")

# Formatting Columns
table.column("#0", width=0, stretch=NO)
table.column("ID", anchor=W, width=80)
table.column("Fullname", anchor=W, width=120)
table.column("Course", anchor=W, width=120)
table.column("Year", anchor=W, width=120)
table.column("Date Purchased", anchor=W, width=120)

# Creating headings
table.heading("#0", text="", anchor=W)
table.heading("ID", text="Ticket No.", anchor=W)
table.heading("Fullname", text="Fullname", anchor=W)
table.heading("Course", text="Course", anchor=W)
table.heading("Year", text="Year", anchor=W)
table.heading("Date Purchased", text="Date Purchased", anchor=W)
table.place(x=300, y=5)

# Adding Date


def select():
    sql = "SELECT * FROM customer;"
    cursor.execute(sql)
    result = cursor.fetchall()

    count = 0
    for i in result:
        table.insert(parent="", index="end", iid=count, text="", values=(i))
        count += 1


btn2 = Button(
    w,
    text="Show",
    width=20,
    command=select
)
btn2.place(x=500, y=250)

w.mainloop()
