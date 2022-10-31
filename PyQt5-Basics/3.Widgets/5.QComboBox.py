"""
The QComboBox is a drop down list, closed by default with an arrow to open it. You can select a single item from the list, with the currently selected item being shown as a label on the widget. The combo box is suited to selection of a choice from a long list of options.

You have probably seen the combo box used for selection of font faces, or size, in word processing applications. Although Qt actually provides a specific font-selection combo box as QFontComboBox.

You can add items to a QComboBox by passing a list of strings to .addItems(). Items will be added in the order they are provided.

"""


import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QComboBox
)

from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("QCombo Box")

        widget = QComboBox()
        # widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.addItems(["One", "Two", "Three"])

        # send the current index position of the selected item
        widget.currentIndexChanged.connect(self.index_changed)

        # there is an alternate signal to send the text
        widget.currentTextChanged.connect(self.text_changed)


        # to make the box editable
        widget.setEditable(True)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an Integer
        print(i)

    def text_changed(self, s):  # s prints string
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
