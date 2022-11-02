# QMessageBox

"""
There are many dialogs which follow the simple pattern we just saw -- a message 
with buttons with which you can accept or cancel the dialog. While you can construct 
these dialogs yourself, Qt also provides a built-in message dialog class called
 QMessageBox. This can be used to create information, warning, about or question dialogs.
"""

import sys


from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("My App")


        button = QPushButton("Press me for a Dialog !")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)



    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a Question!")
        dlg.setMinimumSize(QSize(500, 600))
        dlg.setText("This is a simple Dialog")
        button = dlg.exec()


        if button == QMessageBox.Ok:
            print("OK!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()