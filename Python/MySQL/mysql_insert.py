import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="schooldb",
    user="root",
    password="qwerty"
)
cursor = conn.cursor()

def main():
    addID = input("Enter ID to add: ").strip()
    addStudent = input("Add Student: ").strip()
    sql = "INSERT INTO students (id,name) VALUES (%s, %s)"
    val = (addID, addStudent)

    cursor.execute(sql, val)
    conn.commit()

    print("\nSuccessfully Added Student.")

main()