"""
Context menus are small context-sensitive menus which typically appear when right clicking on a window. Qt has support for generating these menus, and widgets have a specific event used to trigger them. 
"""


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenu, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction('test 2', self))
        context.addAction(QAction('test 3', self))
        context.exec(e.globalPos())




app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
