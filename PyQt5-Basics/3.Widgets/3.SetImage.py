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

        # Setting an Image ->  Kinda Overriding the text to set Image with setPixmap
        """
        Weirdly, you can also use QLabel to display an image using .setPixmap(). 
        This accepts an pixmap, which you can create by passing an image filename to QPixmap. 
        In the example files provided with this book you can find a file otje.jpg which you can display in your window as follows:
        """
        widget.setPixmap(QPixmap('sloth.webp'))
        # The below auto scales the image around
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
