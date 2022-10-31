# QSpinBox and QDoubleSpinBox:

"""
QSpinBox provides a small numerical input box with arrows to increase and decrease the value. QSpinBox supports integers while the related widget QDoubleSpinBox supports floats.
"""



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpin Box")



        widget = QSpinBox() 
        # Or: widget = QDoubleSpinBox()



        # widget.setMinimum(-10)
        # widget.setMaximum(3)
        Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3) # or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)



    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
