import sys
import subprocess
from PyQt4 import QtGui, uic
import shutil
qtCreatorFile = "../../Desktop/test/op.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.clicked)

    def clicked(self):
        mmgf = str(self.filename.toPlainText())
        mmgf = list(mmgf)
        temp = list()
        for i in range(len(mmgf)):
            if mmgf[i] != ',':
                temp.append(mmgf[i])
        for i in range(len(temp)):
            n = int(temp[i])
            with open('../../Desktop/test/main.txt', 'r') as file:
                data = file.readlines()
                data[n] = '\n'
                print data
            with open('../../Desktop/test/main.txt', 'w') as file:
                file.writelines(data)
        res = subprocess.call(['python ../../Desktop/test/fault_gen.py'], shell=True)
        subprocess.call(['python ../../Desktop/test/comp.py'], shell=True)
        shutil.copy2('../../Desktop/test/faultfree.txt', '../../Desktop/test/main.txt')
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(550, 250)
    sys.exit(app.exec_())
