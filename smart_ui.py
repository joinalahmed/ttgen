import sys
import subprocess
from PyQt4 import QtGui, uic

main_li = []
main_li_1 = []
my_fp = open('../../Desktop/test/smart.tfc', 'w')
my_fp.close()
with open('../../Desktop/test/a.tfc', 'r+') as file_tfc:

    for line in file_tfc:
        if line.strip() == 'BEGIN':
            break
    for line in file_tfc:
        if line.strip() == 'END':
            break
        if '#' in line:
            continue
        main_li.append(line)

qtCreatorFile = "../../Desktop/test/smart.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.for_2.clicked.connect(self.forward)
        self.rev.clicked.connect(self.reverse)

    def forward(self):
        my_fp = open('../../Desktop/test/smart.tfc', 'w')
        my_fp.close()
        val_1 = int(self.start.toPlainText())
        val_2 = int(self.final_2.toPlainText())
        with open('../../Desktop/test/state_smart.txt','w') as state_smart:
            state_smart.write(str(val_1))
            state_smart.write('\n')
            state_smart.write(str(val_2))


        with open('../../Desktop/test/smart.tfc', 'a') as file_smart_tfc:
            with open('../../Desktop/test/a.tfc', 'r+') as file_1:

                for line in file_1:
                    if line.strip() == 'BEGIN':
                        break
                    kk = open('../../Desktop/test/smart.tfc', 'a')
                    kk.write(line)
                    kk.close()
                file_smart_tfc.write('BEGIN' + '\n')
            main_li_1 = main_li[val_1:val_2+1]
            print main_li_1
            for ii in range(len(main_li_1)):
                temp_1 = str(main_li_1[ii])
                file_smart_tfc.write(temp_1)
            file_smart_tfc.write('END' + '\n')

        subprocess.call(['python ../../Desktop/test/smart_sim.py'], shell=True)
        sys.exit(app.exec_())

    def reverse(self):
        my_fp = open('../../Desktop/test/smart.tfc', 'w')
        my_fp.close()
        val_1 = int(self.start.toPlainText())
        val_2 = int(self.final_2.toPlainText()) + 1
        with open('../../Desktop/test/state_smart.txt','w') as state_smart:
            state_smart.write(str(val_1))
            state_smart.write('\n')
            state_smart.write(str(val_2))
        with open('../../Desktop/test/smart.tfc', 'w') as file:
            with open('../../Desktop/test/a.tfc', 'r+') as file_1:
                file_data=file_1.readlines()
                file.writelines(file_data)
                '''for line in file_1:
                    if line.strip() == 'BEGIN':
                        break
                    kk = open('../../Desktop/test/smart.tfc', 'a')
                    kk.write(line)
                    kk.close()
                file.write('BEGIN' + '\n')
            main_li_1 = main_li[val_1:val_2]
            print main_li_1
            main_li_1 = main_li_1[::-1]
            print main_li_1
            for ii in range(len(main_li_1)):
                temp_1 = str(main_li_1[ii])
                file.write(temp_1)
            file.write('END' + '\n')'''
        subprocess.call(['python ../../Desktop/test/smart_sim_reverse.py'], shell=True)
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.move(350, 250)
    sys.exit(app.exec_())
v