import csv
import subprocess
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from PyQt4.QtCore import *

res = 1


class UserWindow(QtGui.QMainWindow):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.specTable = QtGui.QTableView()
        self.specModel = QtGui.QStandardItemModel(self)
        self.specList = self.createSpecTable()
        self.initUI()
        self.scnBtn.clicked.connect(self.poutput)
        self.scnBtn1.clicked.connect(self.qc)
        self.scnBtn2.clicked.connect(self.ld)
        self.scnBtn3.clicked.connect(self.reverse)
        self.scnBtn4.clicked.connect(self.image)
        self.scnBtn5.clicked.connect(self.tfc)
  
    def poutput(self):
        res = subprocess.call(['python smfg.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def qc(self):
        res = subprocess.call(['python appear_cross.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def ld(self):
        res = subprocess.call(['python cross_diss.py'], shell=True)
        # res=subprocess.call(['python comp.py'])
        res = subprocess.call(['python f_dis.py'], shell=True)

    def image(self):
        res = subprocess.call(['python rmgf.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def tfc(self):
        res = subprocess.call(['python mmgf.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def reverse(self):
        res = subprocess.call(['python reverse.py'], shell=True)
        # res=subprocess.call(['python comp.py'])
        res = subprocess.call(['python r_dis.py'], shell=True)
    def specData(self):
        with open('tests.csv', 'rb') as csvInput:
            for row in csv.reader(csvInput):
                if row > 0:
                    items = [QtGui.QStandardItem(field) for field in row]
                    self.specModel.appendRow(items)

    def createSpecTable(self):
        # This is a test header - different from what is needed
        specHdr = ['Test', 'Date', 'Time', 'Type']
        self.specData()
        specM = specTableModel(self.specModel, specHdr, self)
        self.specTable.setModel(specM)
        self.specTable.setShowGrid(False)
        vHead = self.specTable.verticalHeader()
        vHead.setVisible(False)
        hHead = self.specTable.horizontalHeader()
        hHead.setStretchLastSection(True)
        self.specTable.sortByColumn(3, Qt.DescendingOrder)
        return self.specTable

    def initUI(self):
        self.ctr_frame = QtGui.QWidget()
        self.label = QtGui.QLabel("Circuit Details")
        self.scnBtn = QtGui.QPushButton("Primary Output ")
        self.scnBtn1 = QtGui.QPushButton("Quantum Cost")
        self.scnBtn2 = QtGui.QPushButton("Level Details")
        self.scnBtn3 = QtGui.QPushButton("Reverse Circuit")
        self.scnBtn4 = QtGui.QPushButton("Circuit Image")
        self.scnBtn5 = QtGui.QPushButton("TFC of Circuit")


        # List Window
        self.specList.setModel(self.specModel)
        pGrid = QtGui.QGridLayout()
        pGrid.setSpacing(5)
        pGrid.addWidget(self.label, 2, 0)
        pGrid.addWidget(self.scnBtn, 3, 0)
        pGrid.addWidget(self.scnBtn1, 4, 0)
        pGrid.addWidget(self.scnBtn2, 5, 0)
        pGrid.addWidget(self.scnBtn3, 6, 0)
        pGrid.addWidget(self.scnBtn4, 7, 0)
        pGrid.addWidget(self.scnBtn5, 8, 0)

        pGrid.addWidget(self.specList, 2, 5, 13, 50)
        # pGrid.addWidget(self.specListF)
        if res == 0:
            pGrid.addWidget(self.label, 5, 0)

        self.ctr_frame.setLayout(pGrid)
        self.setCentralWidget(self.ctr_frame)
        self.statusBar()

        self.setWindowTitle('Truth Table')


class specTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):

        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return 0

    def columnCount(self, parent):
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headerdata[col]
        return None


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("plastique"))
    palette=QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Background,QtCore.Qt.cyan)
    app.setPalette(palette)
    ex = UserWindow()
    ex.resize(1050,420)
    ex.move(150,150)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
