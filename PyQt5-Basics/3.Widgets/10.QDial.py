"""
Finally, the QDial is a rotatable widget that functions just like the slider, but appears as an analogue dial. This looks nice, but from a UI perspective is not particularly user friendly. However, they are often used in audio applications as representation of real-world analogue dials.

"""

import sys
from turtle import width
from PyQt5.QtWidgets import QApplication, QMainWindow, QDial
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("QSlider")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
