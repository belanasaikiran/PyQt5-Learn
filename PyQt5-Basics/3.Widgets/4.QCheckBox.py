import sys

from PyQt5.QtWidgets import (
    QCheckBox,
    QApplication,
    QMainWindow
)

from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Check Box")


        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()