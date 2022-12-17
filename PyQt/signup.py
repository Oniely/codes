from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QLineEdit, QPushButton, QMessageBox
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
import sqlite3
import sys 

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Opening Ui File
        uic.loadUi("signup.ui", self)

        # Assigning Widget
        self.label = self.findChild(QLabel, "label_3")
        pixmap = QPixmap("sc.png")
        self.label.setPixmap(pixmap)
    
        # Show UI
        self.show()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()