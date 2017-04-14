import sys
from PyQt4 import QtGui, QtCore
import subprocess


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)

        self.home()


    def home(self):

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(20, 200, 400, 20)
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("", self)
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("3_17")
        comboBox.addItem("4_49")
        comboBox.addItem("4b15g")
        comboBox.addItem("4b15g_1")
        comboBox.addItem("ham3")
        comboBox.addItem("nthprime")
        comboBox.move(50, 50)
        self.styleChoice.move(80, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def style_choice(self, text):
        b="Proccessing"
        self.styleChoice.setText(b)
        self.download()
        a = text + '.tfc'
        writefile = open('filename.txt', 'w')
        writefile.write(text)
        writefile.close()
        print(a)
        to_readfile = open('tfc/'+a, 'r')
        try:
            reading_file = to_readfile.read()

            writefile = open('a.tfc', 'w')
            try:
                writefile.write(reading_file)
            finally:
                writefile.close()
        finally:
            to_readfile.close()
        subprocess.call(['python truth_gen.py'], shell=True)
        subprocess.call(['python aa.py'], shell=True)


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)





def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()