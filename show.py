import sys
from PyQt4 import QtGui, QtCore
import subprocess


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("a.jpg")
        pixmap1 = QtGui.QPixmap("b.jpg")
        pixmap2 = QtGui.QPixmap("extracted.png")
        pixmap3 = QtGui.QPixmap("stego.png")

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        lbl1 = QtGui.QLabel(self)
        lbl1.setPixmap(pixmap1)
        lbl2 = QtGui.QLabel(self)
        lbl2.setPixmap(pixmap2)
        lbl3 = QtGui.QLabel(self)
        lbl3.setPixmap(pixmap3)
        l1 = QtGui.QLabel()
        l2 = QtGui.QLabel()
        l3 = QtGui.QLabel()
        l4 = QtGui.QLabel()
        l1.setText("Cover Image")
        l4.setText("STego Image")
        l2.setText("Secret Image")

        l3.setText("Extracted Image")
        hbox.addWidget(lbl)
        hbox.addWidget(l1)
        hbox.addWidget(lbl1)
        hbox.addWidget(l2)
        hbox.addWidget(lbl2)
        hbox.addWidget(l3)
        hbox.addWidget(lbl3)
        hbox.addWidget(l4)
        self.setLayout(hbox)

        self.setWindowTitle('Encrypted Images')
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.resize(1050,420)
    ex.move(150,150)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 