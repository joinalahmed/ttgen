from PyQt4 import QtGui, QtCore
import testWidget


class TestWindow(QtGui.QMainWindow):
    def __init__(self, parent):
        super(TestWindow, self).__init__(parent=None)

        # create the ui (or load it)
        self.__editor = testWidget.TestWidget(self)
        self.setCentralWidget(self.__editor)

        # create connections
        self.__editor.textSaved.connect(self.showMessage)

    def showMessage(self, message):
        QtGui.QMessageBox.information(self, 'Message', message)
