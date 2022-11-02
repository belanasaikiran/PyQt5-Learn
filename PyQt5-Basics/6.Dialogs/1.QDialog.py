import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")



        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)



    # Let's enable a dialog window on button click
    def button_clicked(self, s):
        print("click", s)


        dlg = QDialog(self)

        dlg.setWindowTitle("Hello!")
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()