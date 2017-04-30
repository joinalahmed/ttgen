import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "../../Desktop/test/x.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.clicked)

    def clicked(self):
        n = int(self.filename.toPlainText())
        with open('../../Desktop/test/main.txt', 'r') as file:
            data = file.readlines()
        data[n+1] = '\n'
        print data
        # and write everything back
        with open('../../Desktop/test/main.txt', 'w') as file:
            file.writelines(data)
        res = subprocess.call(['python ../../Desktop/test/fault_gen.py'], shell=True)
        subprocess.call(['python ../../Desktop/test/comp.py'], shell=True)
        if res == 0:
            sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
