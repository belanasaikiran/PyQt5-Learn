import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


from random import choice


window_titles = [
    'My App',
    'My APp',
    "still My APp",
    "still My APp",
    'What on Earth',
    'What on Earth',
    'This is surprising',
    'This is surprising',
    'Oops! something went wrong'
]



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # checking the button clicked from n times
        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton('Press Me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)


    def the_button_was_clicked(self):
        print('Clicked!')
        new_window_title = choice(window_titles)
        print("setting title",  new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("window title changed: %s " % window_title)

        if window_title == 'Oops! something went wrong':
            self.button.setDisabled(True)




app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec_()