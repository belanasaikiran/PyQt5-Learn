import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QCheckBox, QComboBox, QListWidget, QLineEdit,
    QSpinBox, QDoubleSpinBox, QSlider
)

from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("example")

        widget = QLabel("Hello")
        widget.setText("Hello LightSpeed!")

        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        widget.setAlignment(Qt.AlignCenter)

  

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
