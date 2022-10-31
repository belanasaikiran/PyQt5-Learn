# Nesting Layouts
"""
For more complex layouts you can nest layouts inside one another using .addLayout on a layout. Below we add a QVBoxLayout into the main QHBoxLayout. If we add some widgets to the QVBoxLayout, they’ll be arranged vertically in the first slot of the parent layout.
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor


# set Color Palette
class Color(QWidget):
    def __init__(self, color):
        super(color, self).__init__()
        self.autoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.window, QColor(color))
        self.setPalette(palette)

# Our Main Window


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Nesting Layouts")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))

        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setlayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
