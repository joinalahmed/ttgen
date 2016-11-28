import sys
import csv
from PyQt4 import QtGui
from PyQt4.QtCore import *
import subprocess
from array import *

res = 1


class UserWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(UserWindow, self).__init__()
        self.specModel = QtGui.QStandardItemModel(self)
        self.specList = self.createSpecTable()
        # self.specListF = self.createSpecTable()
        self.initUI()
        self.scnBtn.clicked.connect(self.clicked)
        self.scnBtn4.clicked.connect(self.appearcross)
        self.scnBtn1.clicked.connect(self.rmgf)
        self.scnBtn2.clicked.connect(self.mmgf)
        self.scnBtn8.clicked.connect(self.stuck0)
        self.scnBtn9.clicked.connect(self.stuck1)
        self.scnBtn5.clicked.connect(self.dappearcross)
        self.scnBtn7.clicked.connect(self.bridgeand)

        self.scnBtn6.clicked.connect(self.bridgeor)

    def clicked(self):
        res = subprocess.call(['python smfg.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def appearcross(self):
        res = subprocess.call(['python appear_cross.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def dappearcross(self):
        res = subprocess.call(['python cross_diss.py'], shell=True)
        # res=subprocess.call(['python comp.py'])
        res = subprocess.call(['python f_dis.py'], shell=True)

    def rmgf(self):
        res = subprocess.call(['python rmgf.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def mmgf(self):
        res = subprocess.call(['python mmgf.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def stuck0(self):
        res = subprocess.call(['python stuck0.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def stuck1(self):
        res = subprocess.call(['python stuck1.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def bridgeand(self):
        res = subprocess.call(['python bridge_and.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def bridgeor(self):
        res = subprocess.call(['python bridge_or.py'], shell=True)
        res = subprocess.call(['python f_dis.py'], shell=True)

    def specData(self):
        with open('tests.csv', 'rb') as csvInput:
            for row in csv.reader(csvInput):
                if row > 0:
                    items = [QtGui.QStandardItem(field) for field in row]
                    self.specModel.appendRow(items)

    def createSpecTable(self):
        self.specTable = QtGui.QTableView()
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
        self.label = QtGui.QLabel("Inject Faults In the Circuit")
        self.scnBtn = QtGui.QPushButton("SMGF")
        self.scnBtn1 = QtGui.QPushButton("RMGF")
        self.scnBtn2 = QtGui.QPushButton("MMGF")
        self.scnBtn3 = QtGui.QPushButton("PMGF")
        self.scnBtn4 = QtGui.QPushButton("Crosspoint-Appearence")
        self.scnBtn5 = QtGui.QPushButton("Crosspoint-Disappearence")

        self.scnBtn6 = QtGui.QPushButton("Bridging - ORed")

        self.scnBtn7 = QtGui.QPushButton("Bridging - ANDed")

        self.scnBtn8 = QtGui.QPushButton("Stuck-at-0")

        self.scnBtn9 = QtGui.QPushButton("Stuck-at-1")

        self.scnBtn10 = QtGui.QPushButton("BIT")

        # List Window
        self.specList.setModel(self.specModel)
        # self.specListF.setModel(self.specModel)

        # Layout of Widgets
        pGrid = QtGui.QGridLayout()
        pGrid.setSpacing(5)
        pGrid.addWidget(self.label, 2, 25)
        pGrid.addWidget(self.scnBtn, 3, 0)
        pGrid.addWidget(self.scnBtn1, 3, 5)
        pGrid.addWidget(self.scnBtn2, 3, 10)
        pGrid.addWidget(self.scnBtn3, 3, 14)
        pGrid.addWidget(self.scnBtn4, 3, 20)
        pGrid.addWidget(self.scnBtn5, 3, 25)

        pGrid.addWidget(self.scnBtn6, 3, 30)

        pGrid.addWidget(self.scnBtn7, 3, 34)

        pGrid.addWidget(self.scnBtn8, 3, 38)

        pGrid.addWidget(self.scnBtn9, 3, 35)

        pGrid.addWidget(self.scnBtn10, 3, 40)

        pGrid.addWidget(self.specList, 4, 0, 4, 50)
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
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

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
    ex = UserWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
