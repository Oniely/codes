import sys
from clr import clear
import mysql.connector
from pwinput import pwinput # Hide password entry by using pwinput instead of input function...
from account import Account # A class...
from loginQUERY import * # Query Function...

# Connector...
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="testdb"
)
c = conn.cursor()

def main():
    while True:
        clear()
        print("----- Login Page -----")
        print("1. Sign Up ")
        print("2. Sign In ")
        print("3. Exit ")
        option = input(">> ").strip()

        if option == '1':
            sign_up()
            break
        elif option == '2':
            sign_in()
            break
        elif option == '3':
            sys.exit()
        elif option == 'admin123':
            account = input("\n>> ")
            if account == "":
                select()
            else:
                select(account)
            
            input("\nPress 'ENTER' to continue.")

        else:
            print("Invalid option, please select from 1-3.")
            print("\nEnter 'c' to continue and 'q' to quit.")
            chs = input(">> ")
            if chs == 'c':
                continue
            elif chs == 'q':
                break


def sign_up():
    clear()
    print("----- Signing Up -----")
    email = input("Enter email: ").upper().strip()
    passw = pwinput("Enter password: ", "*").upper()

    # store value to account with Account(Class)...
    # default is for integer auto increment...
    account = Account("default", email=email, passw=passw)

    # checking if the account is already registered and if not we will add is using insert function from loginQUERY...
    c.execute("SELECT * FROM accounts WHERE email=%s AND passw=%s", [email, passw])
    if c.fetchone():
        print("Account is already registered.")
    else:
        insert(account)
        print("Account Added Successfully.")



    

def sign_in():
    clear()
    print("----- Signing In -----")
    email = input("Enter email: ").upper().strip()
    passw = pwinput("Enter password: ", "*").upper()

    # checking if there is a match in the data column if not then don't authorize login...
    c.execute("SELECT * FROM accounts WHERE email=%s AND passw=%s", [email, passw])
    if c.fetchone():
        print("Logged In")
    else:
        print("Account not found.")
        

if __name__ == "__main__":
    main()