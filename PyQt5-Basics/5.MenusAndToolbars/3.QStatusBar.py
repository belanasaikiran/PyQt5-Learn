"""
We create a status bar object by calling QStatusBar to get a new status bar object and then passing this into .setStatusBar. Since we don't need to change the statusBar settings we can also just pass it in as we create it, in a single line:
"""


from json import tool
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)


from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("Toolbars & Stuff")

        label = QLabel("Hell!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)


        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)


        self.setStatusBar(QStatusBar(self))



    def onMyToolBarButtonClick(self, s):
        print("click", s)
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()