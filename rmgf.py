import sys
import subprocess
from PyQt4 import QtGui, uic
import shutil
qtCreatorFile = "../../Desktop/test/y.ui"  # Enter file here.

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
            # read a list of lines into data
            data = file.readlines()

        # now inject fault in nth level, note that you have to add a newline
        print data
        data.insert(n+1,data[n])
        print data
        # and write everything back
        with open('../../Desktop/test/main.txt', 'w') as file:
            file.writelines(data)
        res = subprocess.call(['python ../../Desktop/test/fault_gen.py'], shell=True)
        res = subprocess.call(['python ../../Desktop/test/comp.py'], shell=True)
        shutil.copy2('../../Desktop/test/faultfree.txt', '../../Desktop/test/main.txt')
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(550,250)
    sys.exit(app.exec_())
