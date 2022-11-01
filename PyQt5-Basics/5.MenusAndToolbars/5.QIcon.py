"""4
we're going to turn our QAction toggleable — so clicking will turn it on, clicking again will turn it off. To do this, we simple call setCheckable(True) on the QAction object.
"""


from json import tool
import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)


from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()


        self.setWindowTitle("QACtion Toggle")

        label = QLabel("QAction Toggable")
        label.setAlignment(Qt.AlignCenter)


        self.setCentralWidget(label)


        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("lsp.svg"),"Your Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        # Checking button click
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()