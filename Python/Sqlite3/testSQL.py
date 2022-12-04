import sqlite3
import os

if os.path.exists("accounting.db"):
    conn = sqlite3.connect("accounting.db")
    c = conn.cursor()

else:
    conn = sqlite3.connect("accounting.db")
    c = conn.cursor()

    c.execute("CREATE DATABASE accounting")
    conn.commit()

    conn.close()

menu = input("Enter 1 if you want to add account and 2 to login: ")

if menu == "1":
    uname = input("Enter account to add: ")
    upass = input("Enter password to add: ")

    c.execute("INSERT INTO qwe VALUES (?, ?)", [uname, upass])

    conn.commit()
    conn.close()

    print("Account Added")

elif menu == "2":
    uname = input("Enter account: ")
    upass = input("Enter password: ")

    c.execute("SELECT * FROM qwe WHERE name=? AND pass=?", [uname, upass])
    
    if c.fetchone() == None:
        print("Incorrect Credential")
    else:
        print("Logged In")


else: 
    print("You have to enter 1 or 2") 