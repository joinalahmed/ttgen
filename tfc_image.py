import re,csv
import pyexcel as pe
import numpy as np
import PIL
from PIL import Image
from image_teest import vertical
from image_teest import horizon
list_im = list()

execfile('/home/joy/Desktop/test/fine_r.py')
asd1 = 0
cd = list()
final = list()
with open('/home/joy/Desktop/test/a.tfc', 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.i' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
            cd = list(cc)
            asd = len(cc)
            asd1 = str(asd)
            # print asd1
            break

final.append(cc)
dd = cd
for i in range(len(dd)):
    dd[i] = "-"
with open('/home/joy/Desktop/test/image_tfc.txt', 'r') as datafile:
    a = datafile.readlines()
    for i in range(len(a)):
        final.append(list(dd))

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == ',':
                continue
            if a[i][j] == '\n':
                continue
            item = final[0].index(a[i][j])
            value = "control"
            k=len(a[i])-2
            if j == (k):
                value = "target"
            final[i + 1][item] = value
del(final[0])
x=np.array(final)
test=x.T
tests=final
print final
pe.save_as(array=test, dest_file_name="/home/joy/Desktop/image.csv")
"""for i in range(len(tests)):
    for j in range(len(tests[i])):
        if tests[i][j]=='-':
            list_im.append('line.jpg')
        if tests[i][j]=='control':
            list_im.append('control.jpg')
        if tests[i][j]=='target':
            list_im.append('target.jpg')

    vertical(list_im)
    list_im=['Trifecta.jpg','Trifecta_vertical.jpg']
    horizon(list_im)
    list_im[:]=[]"""

