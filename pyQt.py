import sys
from PyQt5.QtGui import QPalette, QFont, QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QComboBox, QMessageBox, QLineEdit


def dialog():
    mbox = QMessageBox()
    mbox.setWindowTitle('Jus kiddin')
    reply = mbox.question(w, 'Jus kiddin', 'You are an idiot', QMessageBox.Ok | QMessageBox.Cancel)
    if reply == QMessageBox.Ok:
        mbox.setText('Acceptance is Key')
    elif reply == QMessageBox.Cancel:
        mbox.setText('There is no escape')
    mbox.exec_()


def dialog2():
    mbox = QMessageBox()
    reply = mbox.question(w, 'Message', 'Are you sure you want to quit', QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        mbox.setWindowTitle('Kay')
        mbox.setText('Good choice')
    elif reply == QMessageBox.No:
        mbox.setWindowTitle('NO')
        mbox.setText('You may quit but you can never leave')
    mbox.exec_()


app = QApplication(sys.argv)
w = QWidget()
w.resize(500, 300)
w.setWindowTitle('Yo')
app.setStyle('Fusion')
qp = QPalette()
qp.setColor(QPalette.ButtonText, Qt.black)
qp.setColor(QPalette.Window, Qt.black)
qp.setColor(QPalette.Button, Qt.gray)
w.setPalette(qp)

btn2 = QPushButton('This')
btn3 = QPushButton('That')
hbox = QHBoxLayout(w)


hbox.addWidget(btn2)
hbox.addWidget(btn3)
btn2.clicked.connect(dialog2)
btn3.clicked.connect(dialog)
w.show()
app.exec_()
