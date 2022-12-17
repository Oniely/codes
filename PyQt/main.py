from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QIcon
import sqlite3
import sys


class SIGNIN(QMainWindow):
    def __init__(self):
        super(SIGNIN, self).__init__()

        # Opening Ui File

        uic.loadUi("signin.ui", self)
        widget.setFixedWidth(1280)
        widget.setFixedHeight(800)

        widget.setWindowTitle("Sign In")
        # Assigning Widget

        self.label = self.findChild(QLabel, "label_3")
        pixmap = QPixmap("sc.png")
        self.label.setPixmap(pixmap)

        self.pushButton2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton2.clicked.connect(self.sign_up)

        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.searchAccount)

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")

        # Show UI
        self.show()

    def sign_up(self):
        w_signup = SIGNUP()
        widget.addWidget(w_signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def mainMenu(self):
        w_main = MainMENU()
        widget.addWidget(w_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def searchAccount(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM account WHERE username=? AND password=?",
                       [self.lineEdit.text().strip(), self.lineEdit2.text().strip()])

        result = cursor.fetchone()

        if result == None:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("""You Have Entered The Incorrect Credentials.
Please Try Again.""")
            msgbox.setWindowTitle("Error!")
            msgbox.setStandardButtons(QMessageBox.Ok)
        else:
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText("""Logged In Successfully.""")
            msgbox.setWindowTitle("Success!")
            msgbox.setStandardButtons(QMessageBox.Ok)
            self.mainMenu()

        popup = msgbox.exec_()
        self.lineEdit.clear()
        self.lineEdit2.clear()


class SIGNUP(QMainWindow):
    def __init__(self):
        super(SIGNUP, self).__init__()

        # Opening Ui File
        uic.loadUi("signup.ui", self)
        widget.setFixedWidth(1280)
        widget.setFixedHeight(800)

        widget.setWindowTitle("Sign Up")
        # Assigning Widget
        self.label = self.findChild(QLabel, "label_3")
        pixmap = QPixmap("sc.png")
        self.label.setPixmap(pixmap)

        self.pushButton2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton2.clicked.connect(self.sign_in)

        self.pushButton = self.findChild(QPushButton, "pushButton")
        self.pushButton.clicked.connect(self.addAccount)

        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")

        # Show UI
        self.show()

    def sign_in(self):
        w_signin = SIGNIN()
        widget.addWidget(w_signin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addAccount(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        if self.lineEdit.text().strip() == "" or self.lineEdit2.text().strip() == "":
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("""Empty Spaces Detected...
Please Try Again.""")
            msgbox.setWindowTitle("Error!")
            msgbox.setStandardButtons(QMessageBox.Ok)
        else:
            cursor.execute("SELECT * FROM account WHERE username=? AND password=?",
                           [self.lineEdit.text().strip(), self.lineEdit2.text().strip()])

            result = cursor.fetchone()

            if result == None:

                cursor.execute("INSERT INTO account VALUES (?, ?)",
                               [self.lineEdit.text().strip(), self.lineEdit2.text().strip()])
                conn.commit()

                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("""Signed Up Successfully.""")
                msgbox.setWindowTitle("Success!")
                msgbox.setStandardButtons(QMessageBox.Ok)

            else:
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Warning)
                msgbox.setText("""Account Already Exist.""")
                msgbox.setWindowTitle("Error!")
                msgbox.setStandardButtons(QMessageBox.Ok)

        popup = msgbox.exec_()
        self.lineEdit.clear()
        self.lineEdit2.clear()


class MainMENU(QMainWindow):
    def __init__(self):
        super(MainMENU, self).__init__()

        # Opening Ui File

        uic.loadUi("main.ui", self)
        widget.setFixedWidth(1000)
        widget.setFixedHeight(600)
        widget.setWindowTitle("Main Menu")
        # Assigning Widget

        self.home = self.findChild(QPushButton, "home")
        pixmap = QIcon("home.png")
        self.home.setIcon(pixmap)

        self.calendar = self.findChild(QPushButton, "calendar")
        pixmap2 = QIcon("calendar.png")
        self.calendar.setIcon(pixmap2)

        self.add = self.findChild(QPushButton, "add")
        pixmap3 = QIcon("add.png")
        self.add.setIcon(pixmap3)

        self.signout = self.findChild(QPushButton, "signout")
        pixmap4 = QIcon("signout.png")
        self.signout.setIcon(pixmap4)
        self.signout.clicked.connect(self.sign_in)

        self.name = self.findChild(QLineEdit, "name")
        self.tkNum = self.findChild(QLineEdit, "tkNum")
        self.dateP = self.findChild(QDateEdit, "dateP")
        self.pNum = self.findChild(QLineEdit, "pNum")
        self.courseYear = self.findChild(QLineEdit, "courseYear")
        self.dateP.setDateTime(QtCore.QDateTime.currentDateTime())

        # Buttons
        self.tableData = self.findChild(QTableWidget, "tableData")
        self.tableData.setHorizontalHeaderLabels(
            ["id", "name", "ticket no.", "ticket amount", "date purchase", "phone no.", "course & year"])

        self.showbtn = self.findChild(QPushButton, "showbtn")
        self.showbtn.clicked.connect(self.loadData)

        self.addbtn = self.findChild(QPushButton, "addbtn")
        self.addbtn.clicked.connect(self.addData)

        self.delbtn = self.findChild(QPushButton, "delbtn")
        self.delbtn.clicked.connect(self.delData)

        self.updatebtn = self.findChild(QPushButton, "updatebtn")
        self.updatebtn.clicked.connect(self.updateData)

        self.searchbtn = self.findChild(QPushButton, "searchbtn")
        self.searchbtn.clicked.connect(self.searchData)

        self.loadData()

        # Show UI
        self.show()

    def sign_in(self):
        w_signin = SIGNIN()
        widget.addWidget(w_signin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addData(self):
        from datetime import date

        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        if self.name.text().strip() == "" or self.tkNum.text().strip() == "" or self.pNum.text().strip() == "" or self.courseYear.text().strip() == "" or self.dateP.text().strip() == "":
            msgbox = QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("""Empty Spaces Detected...
    Please Try Again.""")
            msgbox.setWindowTitle("Error!")
            msgbox.setStandardButtons(QMessageBox.Ok)

            popup = msgbox.exec_()
        else:

            cursor.execute("SELECT * FROM customer WHERE tkNum=?",
                           [self.tkNum.text().strip()])

            result = cursor.fetchone()

            if result == None:

                cursor.execute("""INSERT INTO customer (name, tkNum, numPurchase, dateP, pNum, courseYear) VALUES (?, ?, ?, ?, ?, ?)""", [
                    self.name.text().strip(),
                    self.tkNum.text().strip(),
                    1,
                    self.dateP.text().strip(),
                    self.pNum.text().strip(),
                    self.courseYear.text().strip()
                ])
                conn.commit()

                self.name.clear()
                self.tkNum.clear()
                self.dateP.setDateTime(QtCore.QDateTime.currentDateTime())
                self.pNum.clear()
                self.courseYear.clear()

            else:
                msgbox = QMessageBox()
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setText("""Duplicate Ticket Number Detected
Please Try Again.""")
                msgbox.setWindowTitle("Error!")
                msgbox.setStandardButtons(QMessageBox.Ok)

                msgbox.exec_()

            self.loadData()

    def loadData(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        self.tableData.setRowCount(0)

        result = cursor.execute("SELECT * FROM customer;")

        for row_number, row_data in enumerate(result):
            self.tableData.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableData.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))

    def delData(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        query = "SELECT * FROM customer"
        res = cursor.execute(query)

        for row in enumerate(res):
            if row[0] == self.tableData.currentRow():
                data = row[1]
                id = data[0]
                name = data[1]
                tkNum = data[2]

                cursor.execute("DELETE FROM customer WHERE id=? AND name=? AND tkNum=?", [
                               id, name, tkNum])
                conn.commit()
                self.loadData()

    def updateData(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        query = "SELECT * FROM customer"
        res = cursor.execute(query)

        for row in enumerate(res):
            if row[0] == self.tableData.currentRow():
                data = row[1]
                id = data[0]
                name = data[1]
                tkNum = data[2]
                numPurchase = data[3]
                dateP = data[4]
                pNum = data[5]
                courseYear = data[6]

                self.name.setText(name)
                self.tkNum.setText(tkNum)
                self.numPurchase.setValue(numPurchase)
                self.dateP.setDateTime(QtCore.QDateTime.currentDateTime())
                self.pNum.setText(str(pNum))
                self.courseYear.setText(courseYear)

                cursor.execute("DELETE FROM customer WHERE id=? AND name=? AND tkNum=?", [
                               id, name, tkNum])
                conn.commit()
                self.loadData()

    def searchData(self):
        conn = sqlite3.connect("southlandDB.db")
        cursor = conn.cursor()

        query = """select * from customer
                    where name in (
                    select name from customer WHERE name=?
                    group by name
                    having count(id) > 1
                )"""

        self.tableData.setRowCount(0)

        result = cursor.execute(query, [self.name.text()])

        for row_number, row_data in enumerate(result):
            self.tableData.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableData.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    window = MainMENU()
    widget.addWidget(window)
    widget.show()
    app.exec_()
