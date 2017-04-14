import sys
import subprocess
from PyQt4 import QtGui, uic

qtCreatorFile = "new.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.clicked)

    def clicked(self):
        price = str(self.filename.toPlainText())
        prices="tfc/"+price
        to_readfile = open(prices, 'r')
        writefile = open('filename.txt', 'w')
        writefile.write(price)
        writefile.close()
        try:
            reading_file = to_readfile.read()

            writefile = open('a.tfc', 'w')
            try:
                writefile.write(reading_file)
            finally:
                writefile.close()
        finally:
            to_readfile.close()
        print reading_file
        print "test"
        res=subprocess.call(['python truth_gen.py'], shell=True)
        if res == 0:
            subprocess.call(['python aa.py'], shell=True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(350,250)
    sys.exit(app.exec_())
