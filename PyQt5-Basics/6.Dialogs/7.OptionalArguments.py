"""
The four information, question, warning and critical methods also accept optional buttons and defaultButton arguments which can be used to tweak the buttons shown on the dialog and select one by default. Generally though you don't want to change this from the default.
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

        button = QMessageBox.critical(
            self,
            "Oh Dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
        )

        if button == QMessageBox.Discard:
            print("Discard !")

        elif button == QMessageBox.NoToAll:
            print("No to all")
        else:
            print("Ignore!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
