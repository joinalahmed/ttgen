from PyQt4 import QtCore, QtGui
import subprocess

class QDataViewer(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.uploadButton = QtGui.QPushButton('UPLOAD', self)
        self.uploadButton.setGeometry(300, 20, 80, 35)
        self.Button = QtGui.QPushButton('Key', self)
        self.Button.setGeometry(90, 150, 180, 35)
        self.connect(self.uploadButton, QtCore.SIGNAL('clicked()'), self.open)
        self.Button.clicked.connect(lambda:self.run('My_file.py'))
    def open (self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "*.txt")
        return self.filename # I want THIS VARIABLE to be passed to another python file.

    def run(self, path):
        subprocess.call(['python',path])