from json import tool
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QLabel, QToolBar, QAction, QCheckBox, QStatusBar

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Menu bar")

        label = QLabel("Main Toolbar")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)



        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)


        button_action = QAction(QIcon("lsp.svg"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)


        toolbar.addSeparator()


        button_action2 = QAction(QIcon("lsp.svg"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)


        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))


        menu = self.menuBar()


        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)


    def onMyToolBarButtonClick(self, s):
        print("Click", s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()





