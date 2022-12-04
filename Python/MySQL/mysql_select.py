import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="schooldb",
    user="root",
    password=""
)
cursor = conn.cursor()

def main():
    showID = input("Enter ID to show: ").strip()

    cursor.execute("SELECT * FROM students WHERE id=%s", [showID])
    result = cursor.fetchall()

    for i in result:
        print(i)

main()