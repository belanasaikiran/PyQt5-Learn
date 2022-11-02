import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,  QPushButton,QVBoxLayout, QDialog, QDialogButtonBox


# Our dialog with a label and buttons.
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("HEY! I'm Dialog")


        # adding multiple options using pipe "|"
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)



        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK  ?")

        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")



        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)



    # Let's enable a dialog window on button click
    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



"""
The first step in creating a dialog button box is to define the buttons want to show, using namespace attributes from QDialogButtonBox. The full list of buttons available is below.

QDialogButtonBox.Ok
QDialogButtonBox.Open
QDialogButtonBox.Save
QDialogButtonBox.Cancel
QDialogButtonBox.Close
QDialogButtonBox.Discard
QDialogButtonBox.Apply
QDialogButtonBox.Reset
QDialogButtonBox.RestoreDefaults
QDialogButtonBox.Help
QDialogButtonBox.SaveAll
QDialogButtonBox.Yes
QDialogButtonBox.YesToAll
QDialogButtonBox.No
QDialogButtonBox.Abort
QDialogButtonBox.Retry
QDialogButtonBox.Ignore
QDialogButtonBox.NoButton

"""