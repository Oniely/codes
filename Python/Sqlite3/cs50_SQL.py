from cs50 import SQL 

db = SQL("sqlite:///accounting.db")

menu = input("Enter 1 to add account and 2 to Login: ")

if menu == "1":
    uname = input("Enter account to add: ")
    upass = input("Enter password to add: ")

    db.execute("INSERT INTO qwe VALUES (?,?)", uname, upass)

    print("Account Added")

elif menu == "2":
    uname = input("Enter account: ")
    upass = input("Enter password: ")

    qwe = db.execute("SELECT * FROM qwe WHERE name=? and pass=?", uname, upass)
    
    # Error 
    if len(qwe) < 0:
        print("Invalid Credentials")
    else:
        print("Logged In")
