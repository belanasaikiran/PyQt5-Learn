# QMessageBox
"""
As with the dialog button box we looked at already, the buttons shown on a QMessageBox are also configured with the same set of constants which can be combined with | (the binary OR operator) to show multiple buttons. The full list of available button types is shown below.

QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.NoButton
You can also tweak the icon shown on the dialog by setting the icon with one of the following.

Icon state	Description
QMessageBox.NoIcon	The message box does not have an icon.
QMessageBox.Question	The message is asking a question.
QMessageBox.Information	The message is informational only.
QMessageBox.Warning	The message is warning.
QMessageBox.Critical	The message indicates a critical problem.
For example, the following creates a question dialog with Yes and No buttons.

"""

from configparser import LegacyInterpolation
import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        question = QPushButton("Question !")
        question.clicked.connect(self.question_button_clicked)
        # self.setCentralWidget(button)

        information = QPushButton("Information !")
        information.clicked.connect(self.information_button_clicked)

        warning = QPushButton("Warning !")
        warning.clicked.connect(self.warning_button_clicked)

        critical = QPushButton("Critical !")
        critical.clicked.connect(self.critical_button_clicked)

        layout = QVBoxLayout()

        layout.addWidget(question)
        layout.addWidget(information)
        layout.addWidget(warning)
        layout.addWidget(critical)


        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)






    def question_button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a Question!")

        dlg.setText("This is a Question Dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

    def warning_button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Information!")

        dlg.setText("Information here!")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Warning)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes !")
        else:
            print("no!")

    def critical_button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Information!")

        dlg.setText("Information here!")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Critical)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes !")
        else:
            print("no!")


    def information_button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Information!")

        dlg.setText("Information here!")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Information)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes !")
        else:
            print("no!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
