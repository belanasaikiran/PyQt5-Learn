import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # initially we define button checked to true
        self.button_is_checked = True

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()