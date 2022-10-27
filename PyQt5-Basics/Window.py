# PyQt5 Libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# system calls -  Only needed for access to command line arguments
import sys

# Creating a class to open a window
class MainWindow(QMainWindow):
    # pass

    # adding content to the window
    def  __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        # Window Title
        self.setWindowTitle("First App")

        # body content
        label = QLabel("content here !")

        # Align content center
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


# Qt5 Application instance 
app = QApplication(sys.argv)


# creating our first window from declared class
# Create a Qt widget, which will be our window.
window = MainWindow()
window.show() # Important!!! Windows are hidden by default



# Launching the QApplication by starting the event loop.
app.exec_()





# Your application won't reach here until you exit and the event
# loop has stopped.


