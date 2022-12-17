from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
import sqlite3
import sys


class SIGNIN(QMainWindow):
    def __init__(self):
        super(SIGNIN, self).__init__()

        # Opening Ui File

        uic.loadUi("signin.ui", self)

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

        popup = msgbox.exec_()
        self.lineEdit.clear()
        self.lineEdit2.clear()


class SIGNUP(QMainWindow):
    def __init__(self):
        super(SIGNUP, self).__init__()

        # Opening Ui File
        uic.loadUi("signup.ui", self)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    window = SIGNIN()
    widget.addWidget(window)
    widget.setFixedWidth(1280)
    widget.setFixedHeight(800)
    widget.show()
    app.exec_()
