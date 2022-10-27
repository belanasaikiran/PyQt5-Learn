from curses import window
import sys



# PyQt5 
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton




# subclas QMAIn window to custome our application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle(" 4. Main Window ")
        button = QPushButton("click Me!")

        # Set the window centre with central widget
        self.setCentralWidget(button)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()