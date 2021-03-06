from __future__ import print_function
from PyQt4.QtGui import *
import csv
import subprocess
import sys
from PyQt4.QtCore import *
from imageviewer import ImageViewer
from PyQt4 import QtGui
from PyQt4 import QtCore


res = 1
with open('filename.txt') as f:
    lines = f.readlines()
a=lines[0]
a=a[:-4]
name='tfc/'+str(a)+'.jpg'
print(name)
class UserWindow(QtGui.QMainWindow):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.ctr_frame = QtGui.QWidget()
        self.specTable = QtGui.QTableView()
        self.specModel = QtGui.QStandardItemModel(self)
        self.specList = self.createSpecTable()
        self.image = ImageViewer(None, name)

        self.initUI()

    def specData(self):
        with open('details.csv', 'rb') as csvInput:
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
        # List Window
        self.specList.setModel(self.specModel)
        pGrid = QtGui.QGridLayout()
        pGrid.setSpacing(5)
        pGrid.addWidget(self.specList, 2, 5,15,10)
        pGrid.addWidget(self.image, 2, 15,15,150)
        if res == 0:
            pGrid.addWidget(self.label, 5, 0)

        self.ctr_frame.setLayout(pGrid)
        self.setCentralWidget(self.ctr_frame)
        self.statusBar()

        self.setWindowTitle('Circuit Details')


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
    palette = QtGui.QPalette()
    app.setPalette(palette)
    ex = UserWindow()
    ex.resize(1050, 420)
    ex.move(150, 150)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
