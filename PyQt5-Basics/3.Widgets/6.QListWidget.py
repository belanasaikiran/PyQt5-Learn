import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget
)

from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])


        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)


    def index_changed(self, i):
        print(i.text())


    def text_changed(self, s):
        print(s)




app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()