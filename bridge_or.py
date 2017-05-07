import sys
import subprocess
from PyQt4 import QtGui, uic
import shutil
qtCreatorFile = "../../Desktop/test/bridgingor.ui"  # Enter file here.

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
        lines = list(line)
        print lines
        with open('../../Desktop/test/main.txt', 'r') as file_main:
            data = file_main.readlines()
        print data[1]
        data.insert(n + 1, '^' + ',' + line + '\n')
        with open('../../Desktop/test/main.txt', 'w') as file_main:
            file_main.writelines(data)
        subprocess.call(['python ../../Desktop/test/bridge.py'], shell=True)
        res = subprocess.call(['python ../../Desktop/test/comp.py'], shell=True)
        shutil.copy2('../../Desktop/test/faultfree.txt', '../../Desktop/test/main.txt')
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(400, 250)

    sys.exit(app.exec_())
