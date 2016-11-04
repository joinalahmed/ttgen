import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "x.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.clicked)

    def clicked(self):
        mmgf = str(self.filename.toPlainText())
        mmgf=list(mmgf)
        temp=list()
        for i in range(len(mmgf)):
            if mmgf[i] != ',':
                temp.append(mmgf[i])
        for i in range(len(temp)):
            n=int(temp[i])


            with open('main.txt', 'r') as file:
             # read a list of lines into data
             data = file.readlines()

        # now inject fault in nth level, note that you have to add a newline
             data[n] = '\n'

        # and write everything back
            with open('main.txt', 'w') as file:
             file.writelines(data)
        res = subprocess.call(['python fault_gen.py'], shell=True)
        subprocess.call(['python comp.py'], shell=True)
        if res == 0:
            sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
