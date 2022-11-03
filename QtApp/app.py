import pyfirmata
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout


# ==============================================
# Input to Arduino board for communication


# if __name__ == '__main__':
#     # port = input("Enter COM port Name:  \n")
#     # comPort = port
#     board = pyfirmata.Arduino("/dev/ttyACM0")
#     print("Communication Successfully Initiated ")


# ledBoard = pyfirmata.Arduino()

def ConnectDevice():
        DeviceAddress = "/dev/ttyACM0"

        board = pyfirmata.Arduino(DeviceAddress)
        if (board):
            print("Device Connected")
        else:
            print("Problem Connecting to Device")





# ======GET LED PIN ======
# pin = 13
# led = ledBoard.digital[pin]



def On():
    # led.write(1)
    print("on")


def Off():
    # led.write(0)
    print("off")




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("LED ON-OFF")


        label = QLabel("Testing LED")



        ConnectBoard = QPushButton("Connect Arduino")
        ConnectBoard.clicked.connect(ConnectDevice)

        turnOn_button = QPushButton("ON")
        turnOn_button.clicked.connect(On)

        turnOff_button = QPushButton("OFF")
        turnOff_button.clicked.connect(Off)


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(ConnectBoard)
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
