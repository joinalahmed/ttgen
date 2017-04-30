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
        self.scnBtn.clicked.connect(self.clicked)
        self.scnBtn4.clicked.connect(self.appearcross)
        self.scnBtn1.clicked.connect(self.rmgf)
        self.scnBtn3.clicked.connect(self.pmgf)

        self.scnBtn2.clicked.connect(self.mmgf)
        self.scnBtn8.clicked.connect(self.stuck0)
        self.scnBtn9.clicked.connect(self.stuck1)
        self.scnBtn5.clicked.connect(self.dappearcross)
        self.scnBtn7.clicked.connect(self.bridgeand)

        self.scnBtn6.clicked.connect(self.bridgeor)
        self.scnBtn10.clicked.connect(self.reverse)
        self.scnBtn11.clicked.connect(self.detail)
        self.scnBtn12.clicked.connect(self.smart)

    def smart(self):
        res = subprocess.call(['python smart_ui.py'], shell=True)
        res = subprocess.call(['python smart_dis.py'], shell=True)

    def detail(self):
        res = subprocess.call(['python detail.py'], shell=True)
        res = subprocess.call(['python detail_image.py'], shell=True)

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
    def pmgf(self):
        res = subprocess.call(['python pmgf.py'], shell=True)
        # res=subprocess.call(['python comp.py'])
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
        self.scnBtn10 = QtGui.QPushButton("Reverse Circuit")
        self.scnBtn11 = QtGui.QPushButton("Circuit Details")
        self.scnBtn12 = QtGui.QPushButton("Smart Simulation")




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

        pGrid.addWidget(self.scnBtn6, 9,0)

        pGrid.addWidget(self.scnBtn7, 10,0)

        pGrid.addWidget(self.scnBtn8, 11, 0)

        pGrid.addWidget(self.scnBtn9, 12, 0)

        pGrid.addWidget(self.scnBtn10, 13,0)
        pGrid.addWidget(self.scnBtn11, 14,0)
        pGrid.addWidget(self.scnBtn12, 15,0)



        pGrid.addWidget(self.specList, 2, 5, 13, 50)
        #pGrid.addWidget(self.specList1)
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
