"""
Connecting widgets together directly
So far we've seen examples of connecting widget signals to Python methods. When a signal is fired from the widget, our Python method is called and receives the data from the signal. But you don't always need to use a Python function to handle signals -- you can also connect Qt widgets directly to one another.

In the following example, we add a QLineEdit widget and a QLabel to the window. In the \\__init__ for the window we connect our line edit .textChanged signal to the .setText method on the QLabel. Now any time the text changes in the QLineEdit the QLabel will receive that text to it's .setText method.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("My App")


        self.label = QLabel()


        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        """
        Notice that in order to connect the input to the label, 
        the input and label must both be defined. 
        This code adds the two widgets to a layout, 
        and sets that on the window. We'll cover layouts in detail later, 
        you can ignore it for now.
        """
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)



app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()