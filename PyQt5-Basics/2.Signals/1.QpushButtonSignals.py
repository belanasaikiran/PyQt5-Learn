import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # title
        self.setWindowTitle("Qpush Button for Signals")

        button = QPushButton("Click Me!")
        button.setCheckable(True)
        # executing another function on click of a button
        button.clicked.connect(self.the_button_was_clicked)


        # center the widget
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("I'm clicked!")





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()