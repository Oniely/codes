import mysql.connector
from class2 import *

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="qwerty",
    database="schooldb"
)
c = conn.cursor()

def insert(student):
    query = "INSERT INTO students VALUES (%s, %s, %s)"
    value = ([student.id , student.fname, student.lname])

    c.execute(query, value)
    conn.commit()

def update(student, where):
    query = "UPDATE students SET id=%s, fname=%s, lname=%s WHERE id=%s"
    value = ([student.id, student.fname, student.lname, where])

    c.execute(query, value)
    conn.commit()

def select(id = ""):

    if id == "":
        c.execute("SELECT * FROM students")
        result = c.fetchall()
        for i in result:
            print(i)

    else:
        c.execute("SELECT * FROM students WHERE id=%s", [id])
        print(c.fetchall())



select()


