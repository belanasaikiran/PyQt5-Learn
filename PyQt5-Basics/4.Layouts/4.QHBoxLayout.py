# QHBoxLayout horizontally arranged widgets
"""
QHBoxLayout is the same, except moving horizontally. Adding a widget adds it to the right hand side.
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout #previously we used QVBoxLayout for Vertical stacking
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Color with QVBox Layout")

        layout = QHBoxLayout()
        
        layout.addWidget(Color('red'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
