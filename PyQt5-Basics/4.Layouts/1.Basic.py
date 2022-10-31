import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("Basic Layout")



app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()