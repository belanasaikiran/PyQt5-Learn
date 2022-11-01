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


        label = QLabel("HEll")
        label.setAlignment(Qt.AlignCenter)


        self.setCentralWidget(label)


        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)


    def onMyToolBarButtonClick(self, s):
        print("click", s)
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()