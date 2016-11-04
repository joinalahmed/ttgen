import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "stuckat.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.clicked)

    def clicked(self):
        n = int(self.level.toPlainText())
        line = str(self.line.toPlainText())
        with open('main.txt', 'r') as files:
            # read a list of lines into data
            data = files.readlines()

        # now inject fault in nth level, note that you have to add a newline
        print data[1]
        if line in data[0]:
            data.insert(n + 1, '0' + ',' + line + '\n')
        # and write everything back
        with open('main.txt', 'w') as files:
            files.writelines(data)
        res = subprocess.call(['python stuck.py'], shell=True)
        res = subprocess.call(['python comp.py'], shell=True)
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
