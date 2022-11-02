## Converting UI File to Python

To generate a Python output file run pyuic5 from the command line, passing the .ui file and the target file for output, with a -o parameter. The following will generate a Python file named MainWindow.py which contains our created UI.


```bash 

pyuic5 mainwindow.ui -o MainWindow.py

```