import sys
import subprocess
from PyQt4 import QtGui, uic
import shutil

qtCreatorFile = "/home/joy/Desktop/test/stuckat1.ui"  # Enter file here.

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
        with open('/home/joy/Desktop/test/main.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        # now inject fault in nth level, note that you have to add a newline
        print data[1]
        if line in data[0]:
            data.insert(n + 1, '1' + ',' + line + '\n')
        # and write everything back
        with open('/home/joy/Desktop/test/main.txt', 'w') as file:
            file.writelines(data)
        print data
        res = subprocess.call(['python /home/joy/Desktop/test/stuck.py'], shell=True)
        res = subprocess.call(['python /home/joy/Desktop/test/comp.py'], shell=True)
        shutil.copy2('../../Desktop/test/faultfree.txt', '../../Desktop/test/main.txt')
        if res == 0:
            sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
