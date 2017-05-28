import sys
import os
from PyQt4 import QtGui


class Notepad(QtGui.QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QtGui.QTextEdit(self)
        self.initUI()
        self.openFile()

    def initUI(self):
        self.setCentralWidget(self.text)
        self.setGeometry(400, 600, 400,600)
        self.setWindowTitle('Generated Real File ')
        self.show()

    def openFile(self):
        filename = "../../Desktop/test/converted.real"
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        self.text.setReadOnly(True)
        f.close()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Notepad()
    # ex.resize(1050,420)
    ex.move(450, 50)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
