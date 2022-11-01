import sys
from PyQt5.QtWidgets import QStackedLayout, QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QColor, QPalette

# set Color Palette

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)






class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QStack Layout")


        layout = QStackedLayout()

        layout.addWidget(Color('blue'))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('yellow'))


        layout.setCurrentIndex(2)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()



app.exec()
