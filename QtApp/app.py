import sys
from PyQt5.QtWidgets import QApplication

# We use uic to load  Qt Designed UI file
from PyQt5 import uic


app = QApplication(sys.argv)


# We use uic method to load UI
window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()
