import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit
)

from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("QLine Edit")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your Text")

        # widget.setReadOnly(True)  # for read only
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_changed)


        """
        Additionally, it is possible to perform input validation using an input mask to define which characters are supported and where. This can be applied to the field as follows:
        """

        # widget.setInputMask('000.000.000.000;_') # helpful for numbers to be filled such as phone numbers and MAC address
        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return Pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("selection Changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text Changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
