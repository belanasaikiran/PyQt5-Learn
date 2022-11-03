import pyfirmata
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout


# ==============================================
# Input to Arduino board for communication


if __name__ == '__main__':
    # port = input("Enter COM port Name:  \n")
    # comPort = port
    board = pyfirmata.Arduino("/dev/ttyACM0")
    print("Communication Successfully Initiated ")


# ======GET LED PIN ======
pin = 13
led = board.digital[13]


# wait = input("Turn On/Off LED with () ? (y/n)")
# print("You have selected", wait)

# if wait == "y" or wait == "Y":
#     board.digital[pin].write(1)
#     print("LED Turned On")
# elif wait == "n" or wait == "N":
#     board.digital[pin].write(0)
#     print("LED Turned Off")
# else:
#     print("Error!")


def On():
    led.write(1)


def Off():
    led.write(0)





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("LED ON-OFF")


        label = QLabel("Testing LED")

        

        turnOn_button = QPushButton("ON")
        turnOn_button.clicked.connect(On)

        turnOff_button = QPushButton("OFF")
        turnOff_button.clicked.connect(Off)


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(turnOn_button)
        layout.addWidget(turnOff_button)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




app = QApplication(sys.argv)


# We use uic method to load UI
window = MainWindow()
window.show()
app.exec()
