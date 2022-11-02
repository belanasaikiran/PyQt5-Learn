import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)



app = QtWidgets.QApplication(sys.argv)
Window = MainWindow()
Window.show()


app.exec()