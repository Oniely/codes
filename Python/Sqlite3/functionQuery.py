import sqlite3
from classquery import *

#SQL Query in Function

def insert(student):
    with conn:
        c.execute("INSERT INTO student VALUES (?, ?, ?)", [
                  student.fname, student.lname, student.gpa])

def update(lastname, student):
    with conn:
        c.execute("UPDATE student SET fname=?, lname=?, gpa=? WHERE lname=:lastname", [
                  student.fname, student.lname, student.gpa, lastname])

def select(lastname = ""):
    with conn:
        if lastname == "":
            c.execute("SELECT * FROM student")
            result = c.fetchall()
            for i in result:
                print(i)
        else:
            c.execute("SELECT * FROM student WHERE lname=:lastname", [lastname])
            print(c.fetchall())

# ---------------------------------------------------------------------------------- #

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("""CREATE TABLE student (
                fname text,
                lname text,
                gpa float) """)
conn.commit()

#inserting student to table using function
student1 = Student("Oniel", "Gencaya", 4.5)
student2 = Student("Maya", "Kikiw", 3.0)
insert(student1)
insert(student2)

#update the student2 by lname using function
new_student2 = Student("Yza", "Gencaya", 5.0)
update("Kikiw", new_student2)



conn.commit()

select()

