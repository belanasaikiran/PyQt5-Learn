import sys
from PyQt5.QtWidgets  import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Disable Button on Click")

        self.button = QPushButton("Click bait!")
        self.button.clicked.connect(self.the_button_was_Clicked)

        self.setCentralWidget(self.button)


    def the_button_was_Clicked(self):
        self.button.setText("You already Clicked Me ! so you are disabled")
        self.button.setEnabled(False)

        #also we are changing the title of the window
        self.setWindowTitle("Button is now disabled")



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()