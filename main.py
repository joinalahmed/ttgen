import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "main.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start.clicked.connect(self.clicked)

    def clicked(self):
        
        res=subprocess.call(['python newgui.py'], shell=True)
        if res == 0:
            subprocess.call(['python aa.py'], shell=True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(350,250)
    sys.exit(app.exec_())
