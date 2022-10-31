"""
One of the main events which widgets receive is the QMouseEvent. QMouseEvent events are created for each and every mouse movement and button click on a widget. The following event handlers are available for handling mouse events --
"""


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window dude!")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mouse press Event")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouse release Event")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouse double click Event")


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
