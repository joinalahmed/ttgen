
from PyQt4 import QtGui, QtCore

class MyDialog(QtGui.QWidget):
    def __init__(self, modelSource, parent=None):
        super(MyDialog, self).__init__(parent)

        self.tableView = QtGui.QTableView(self)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setModel(modelSource)

        self.listView = QtGui.QListView(self)
        self.listView.setModel(modelSource)
        self.listView.setModelColumn(0)

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setModel(modelSource)
        self.comboBox.setModelColumn(1)

        self.layoutGrid = QtGui.QGridLayout(self)
        self.layoutGrid.addWidget(self.comboBox, 0, 0, 1, 2)
        self.layoutGrid.addWidget(self.listView, 1, 0, 1, 1)
        self.layoutGrid.addWidget(self.tableView, 1, 1, 1, 1)

class MyWindow(QtGui.QWidget):
    _dialogs = []
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.modelSource = QtGui.QStandardItemModel(self)

        for rowNumber in range(3):
            items = []
            for columnNumber in range(3):
                item = QtGui.QStandardItem()
                item.setText("row: {0} column {1}".format(rowNumber, columnNumber))

                items.append(item)

            self.modelSource.appendRow(items)

        self.labelDialogs = QtGui.QLabel(self)
        self.labelDialogs.setText("Select a number of dialogs to create:")

        self.spinBoxDialogs = QtGui.QSpinBox(self)
        self.spinBoxDialogs.setValue(3)

        self.pushButtonShow = QtGui.QPushButton(self)
        self.pushButtonShow.setText("Show Dialogs!")
        self.pushButtonShow.clicked.connect(self.on_pushButtonShow_clicked)

        self.pushButtonClose = QtGui.QPushButton(self)
        self.pushButtonClose.setText("Close Dialogs")
        self.pushButtonClose.clicked.connect(self.on_pushButtonClose_clicked)

        self.layoutHorizontal = QtGui.QHBoxLayout(self)
        self.layoutHorizontal.addWidget(self.labelDialogs)
        self.layoutHorizontal.addWidget(self.spinBoxDialogs)
        self.layoutHorizontal.addWidget(self.pushButtonShow)
        self.layoutHorizontal.addWidget(self.pushButtonClose)

    @QtCore.pyqtSlot()
    def on_pushButtonShow_clicked(self): 
        self._dialogs = []
        dialogsNumber = self.spinBoxDialogs.value()

        for dialogNumber in range(dialogsNumber):  
            dialog = MyDialog(self.modelSource)
            dialog.show()
            dialog.move(100, 100)

            self._dialogs.append(dialog)

    @QtCore.pyqtSlot()
    def on_pushButtonClose_clicked(self): 
        for dialog in self._dialogs:
            dialog.close()

        self._dialogs = []

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()
    sys.exit(app.exec_())