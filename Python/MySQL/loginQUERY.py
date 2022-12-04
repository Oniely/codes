import mysql.connector
from account import Account

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="testdb"
)
c = conn.cursor()

# if parameter is empty it will select all
def select(id = ""):

        if id == "":
            c.execute("SELECT * FROM accounts")
            result = c.fetchall()
            for i in result:
                print(i)
        else:
            c.execute("SELECT * FROM accounts WHERE id=%s", [id])
            print(c.fetchone())

# inserting data using class "identifiers"
def insert(account):
    query = "INSERT INTO accounts VALUES (%s, %s, %s)"
    value = ([account.id , account.email, account.passw])

    c.execute(query, value)
    conn.commit()

# updating data row by using class "identifiers"
def update(account, where):
    query = "UPDATE students SET id=%s, fname=%s, lname=%s WHERE id=%s"
    value = ([account.id, account.fname, account.lname, where])

    c.execute(query, value)
    conn.commit()