"""
We should make the toolbar a bit more interesting. We could just add a QButton widget, but there is a better approach in Qt that gets you some additional features — and that is via QAction. QAction is a class that provides a way to describe abstract user interfaces. What this means in English, is that you can define multiple interface elements within a single object, unified by the effect that interacting with that element has. For example, it is common to have functions that are represented in the toolbar but also the menu — think of something like Edit->Cut which is present both in the Edit menu but also on the toolbar as a pair of scissors, and also through the keyboard shortcut Ctrl-X (Cmd-X on Mac).

Without QAction you would have to define this in multiple places. But with QAction you can define a single QAction, defining the triggered action, and then add this action to both the menu and the toolbar. Each QAction has names, status messages, icons and signals that you can connect to (and much more).

In the code below you can see this first QAction added.
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



    def onMyToolBarButtonClick(self, s):
        print("click", s)
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()