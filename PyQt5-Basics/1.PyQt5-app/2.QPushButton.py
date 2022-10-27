from curses import window
import sys
from PyQt5.QtWidgets import QApplication, QPushButton


app = QApplication(sys.argv)

window = QPushButton("I'm a push button")
window.show()


app.exec_()