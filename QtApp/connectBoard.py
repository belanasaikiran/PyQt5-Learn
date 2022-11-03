import pyfirmata
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


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


wait = input("Turn On/Off LED with () ? (y/n)")
print("You have selected", wait)

if wait == "y" or wait == "Y":
    board.digital[pin].write(1)
    print("LED Turned On")
elif wait == "n" or wait == "N":
    board.digital[pin].write(0)
    print("LED Turned Off")
else:
    print("Error!")


def On():
    led.write(1)


def Off():
    led.write(0)



