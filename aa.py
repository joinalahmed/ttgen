import sys
import csv
from PyQt4 import QtGui
from PyQt4.QtCore import *
from array import *


class UserWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        super(UserWindow, self).__init__()
        self.specModel = QtGui.QStandardItemModel(self)
        self.specList = self.createSpecTable()
        self.initUI()

    def specData(self):
        with open('test.csv', 'rb') as csvInput:
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


# List Window
        self.specList.setModel(self.specModel)

# Layout of Widgets
        pGrid = QtGui.QGridLayout()
        pGrid.setSpacing(5)
        pGrid.addWidget(self.specList, 10, 0, 20, 6)
        self.ctr_frame.setLayout(pGrid)
        self.setCentralWidget(self.ctr_frame)
        self.statusBar()

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Output')


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
