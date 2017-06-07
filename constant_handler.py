import re
import fileinput
asd1 = 0
line=[]
with open('../../Desktop/test/a.tfc', 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.c' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc1 = re.split(',', bb)
            asd1 = len(cc1)
            break
with open('../../Desktop/test/a.tfc', 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
            asd2 = len(cc)
            break
if asd1 >= 1:
    with open('../../Desktop/test/gen.py', 'r') as datafile:
        lines=datafile.readlines()
        j=lines.index("    #constant\n")
        for i in range(1,asd1+1):
            data="    "+cc[asd2-i]+"="+cc1[i-1][0]+"\n"
            lines.insert(j,data)
    fo=open("../../Desktop/test/gen.py","rw+")
    liness=fo.writelines(lines)
    fo.close()