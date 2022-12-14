import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")


        # default we enable "true"
        button.setCheckable(True)

        # checking the status of button
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("checked?", checked)
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()