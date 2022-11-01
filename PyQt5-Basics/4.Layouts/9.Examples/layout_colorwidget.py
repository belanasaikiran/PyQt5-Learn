import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPalette

# set Color Palette

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


