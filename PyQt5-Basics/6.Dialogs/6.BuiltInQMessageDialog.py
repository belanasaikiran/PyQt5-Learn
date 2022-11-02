# QMessageBox
"""
Built in QMessageBox dialogs
To make things even simpler the QMessageBox has a number of methods which can be used to construct these types of message dialog. These methods are shown below --

PYTHON
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
The parent parameter is the window which the dialog will be a child of. If you're launching your dialog from your main window, you can just pass in self. The following example creates a question dialog, as before, with Yes and No buttons.

"""

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

    """
    The parent parameter is the window which the dialog will be a child of. 
    If you're launching your dialog from your main window, you can just pass in self. 
    The following example creates a question dialog, as before, with Yes and No buttons.
    
    """

    def question_button_clicked(self, s):
        button = QMessageBox.about(
            self, "Question dialog", "The Longer Message")

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
        buttoon = QMessageBox.critical(self, "Critical Error", "Something is critical in your app")

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
