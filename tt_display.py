import csv
import subprocess
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PIL import Image
import shutil

res = 1


class UserWindow(QtGui.QMainWindow):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.scnBtn = QtGui.QPushButton("Save")
        self.specTable = QtGui.QTableView()
        self.specModel = QtGui.QStandardItemModel(self)
        self.specList = self.createSpecTable()
        self.initUI()
        self.scnBtn.clicked.connect(self.file_save)

    def file_save(self):
        subprocess.call(['python ../../Desktop/test/csvtoimagesmart.py'], shell=True)
        name = QtGui.QFileDialog.getSaveFileName(self, "Choose PNG Image","../../Desktop/", "PNG (*.png)")
        name=str(name)
        shutil.copy("../../Desktop/test/smart.png",name)


    def specData(self):
        with open('../../Desktop/test/tests.csv', 'rb') as csvInput:
            for row in csv.reader(csvInput):
                if row > 0:
                    items = [QtGui.QStandardItem(field) for field in row]
                    self.specModel.appendRow(items)

    def createSpecTable(self):
        specHdr = []
        self.specData()
        specM = specTableModel(self.specModel, specHdr, self)
        self.specTable.setModel(specM)
        self.specTable.setShowGrid(False)
        vHead = self.specTable.verticalHeader()
        vHead.setVisible(False)
        hHead = self.specTable.horizontalHeader()
        hHead.setVisible(False)
        self.specTable.sortByColumn(3, Qt.DescendingOrder)
        return self.specTable

    def initUI(self):
        self.ctr_frame = QtGui.QWidget()

        self.specList.setModel(self.specModel)
        pGrid = QtGui.QGridLayout()
        pGrid.setSpacing(5)
        pGrid.addWidget(self.scnBtn, 2, 0)

        pGrid.addWidget(self.specList, 2, 5, 13, 50)

        self.ctr_frame.setLayout(pGrid)
        self.setCentralWidget(self.ctr_frame)
        self.statusBar()

        self.setWindowTitle('Full Truth Table of the Circuit')


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


def main():
    app = QtGui.QApplication(sys.argv)
    ex = UserWindow()
    ex.resize(1050, 420)
    ex.move(150, 150)
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
