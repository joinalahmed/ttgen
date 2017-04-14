import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "bridgingor.ui"  # Enter file here.

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
        lines=list(line)
        print lines
        with open('main.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now inject fault in nth level, note that you have to add a newline
        print data[1]
        #if line in data[0]:
	    #print("success")
        data.insert(n + 1, '^' + ',' + line + '\n')
        # and write everything back
        with open('main.txt', 'w') as file:
            file.writelines(data)
        res = subprocess.call(['python bridge.py'], shell=True)
        res = subprocess.call(['python comp.py'], shell=True)
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(550,250)

    sys.exit(app.exec_())
