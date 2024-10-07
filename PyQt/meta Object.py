import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import *
from PyQt6.QtCore import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Show message!")

    b.move(50, 50)
    b.clicked.connect(showdialog)
    w.setWindowTitle("PyQt Dialog demo")
    w.show()
    sys.exit(app.exec())

def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec()
    print("Value of pressed message box button:", retval)

def msgbtn(i):
    print("Button pressed is:", i.text())

if __name__ == '__main__':
    window()
