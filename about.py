import os
import sys
from PyQt4.QtGui import *

# Create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("About :: RC Tool ")

# Create widget
label = QLabel(w)
pixmap = QPixmap('../../Desktop/test/about.png')
label.setPixmap(pixmap)
w.resize(pixmap.width(), pixmap.height())

# Draw window
w.show()
w.move(200,150)
app.exec_()