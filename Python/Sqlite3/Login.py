import sqlite3
import os
import time
import pwinput

if os.path.exists("testdb.db"):
    conn = sqlite3.connect("testdb.db")
    c = conn.cursor()
else:
    conn = sqlite3.connect("testdb.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE accounts
                (user text, pass text)''')
    conn.commit()

while True:
    print("\n----- Login Page -----")
    print("1. Sign Up ")
    print("2. Sign In ")
    print("3. Exit ")
    select = input("\n>> ")

    if select == '1':
        print("\n----- Signing Up -----")
        user = input("Enter Username: ").strip().upper()
        passw = pwinput.pwinput("Enter Password: ", "*").strip().upper()

        c.execute("INSERT INTO accounts VALUES (?, ?)", [user, passw])
        conn.commit()

        print("\n\n  ----- Signed Up Successfully -----")
        print("----- Redirecting To Login Page -----\n")
        for i in range(37):
            print("*", end="")
            time.sleep(0.006)

        continue

    elif select == '2':
        print("\n----- Signing In -----")
        user = input("Enter Username: ").strip().upper()
        passw = pwinput.pwinput("Enter Password: ", "*").strip().upper()

        c.execute("SELECT * FROM accounts WHERE user=? AND pass=?",
                  [user, passw])

        if c.fetchone() == None:
            print("\nIncorrect Credentials")
            chs = input("Try again? ").strip().upper()
            if chs == "YES" or chs == "Y":
                continue
            elif chs == "NO" or chs == "N":
                break
            else:
                print("You have to enter (y or n)")
                break
        else:
            print("\n----- Logged In -----")
            break

    elif select == '3':
        exit()

    else:
        print("\nInvalid Input Enter Numbers Only(1 - 3)")
