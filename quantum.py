import re
import string
import pyexcel as pe

#import prettytable



var2 = []
count = 1
m11 = ''
my_fp = open("tt_generator.py", "w")
my_fp.close()

qw = open("main11.txt", "w")
qw.close()


# NEGATIVE CONTROL - HANDLER
def neg_ctl(hexo):
    for mns in range(len(hexo)):
        hu = str(hexo[mns])
        if hu == ",":
            continue
        mk = len(hexo)
        mk -= 1
        if mns == mk:
            break
        if "'" not in hu:
            continue
        hs = re.split("'", hu)
        hs_fin = list()
        hs_fin.append(hs[0])
        hs_fin.append(' = not ')
        hs_fin.append(hs[0])
        hs_fin.append(';')
        hss = ''.join(hs_fin)
        jk = 'if ' + hs[0] + ' == 1:'
        jk1 = ''.join(jk)
        lo = jk1 + hss
        mx = open('tt_generator.py', 'a')
        mx.write(lo + '\n')
        mx.close()


# BLOCK FOR LEVEL DETAILS

# BLOCK FOR .tfc FILE PROCESSING , EXTRACTION OF DATA
with open('/home/joy/Desktop/test/a.tfc', 'r+') as file:
    for line in file:
        if line.strip() == 'BEGIN':
            break
    for line in file:
        if line.strip() == 'END':
            break
        if '#' in line:
            continue
        line1 = re.split(',', line)
        var1 = str(line1[0])
        var1 = re.split(' ', var1)
        r_var = str(var1[0])
        r1112 = re.compile("([a-zA-Z]+)([0-9]+)")
        m123 = r1112.match(r_var)
        m11 = m123.group(1)
        for iy in range(1, len(line1)):
            var1.append(line1[iy])
        var2.append(var1)
        length = len(line1)
        line2 = line1[0]
        line2 = re.split('\\s', line2)
        line2 = list(line2)
        line1[0] = line2[1]
        length1 = len(line1)
        line3 = line1[length1 - 1]
        length2 = len(line3)
        line3 = re.split('\n', line3)
        line1[length1 - 1] = line3[0]
        line_final = list()
        for ii in range(len(line1)):
            line_final.append(line1[ii])
            line_final.append(',')
        del line_final[-1]
        line_final.insert(0, m11)
        line_final.insert(1, ',')
        line_final1 = ''.join(line_final)
        ff = open('main11.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()

# LEVEL WISE EQUATION GENERATOR
with open('main11.txt', 'r+') as exp:
    for lenn in exp:
        if len(lenn) == 1:
            if lenn[0] == '\n':
                continue
        if lenn[0] == '#':
            continue
        ax = lenn
        axx = re.split(',', ax)
        mn = len(axx)
        mn -= 1
        axx1 = str(axx[mn])
        axx2 = re.split('\n', axx1)
        axx[mn] = axx2[0]
        mn1 = len(axx)
        mn2 = mn1 - 1
        axx[mn2] = axx2[0]
        lenn = axx
        linen = list()
        for ii in range(len(lenn)):
            linen.append(lenn[ii])
            linen.append(',')
        del linen[-1]
        lenn = linen
        # lib_id LIBRARY IDENTIFIER
        lib_id = str(lenn[0])
        lenn = lenn[2:]
        #quantum cost calculation
        nl = sum(1 for line in open('main11.txt'))
        QC=0
        i=0
        with open("main11.txt", "r") as fo:
            for i in range(nl):

                data = fo.next()
                words = string.split(data)
                chars = 0
                for j in words:
                    chars = chars + len(j)
                if chars >= 3:
                    n = chars - ((chars + 1) / 2)
                    if ((lib_id == 't' or lib_id == 'T') and (n <= 2)):
                        QC = QC + 1
                    elif ((lib_id == 't' or lib_id == 'T') and n > 2):
                         QC = QC + ((2 ** n) - 3)
                    elif ((lib_id == 'f' or lib_id == 'F') and n == 2):
                         QC = QC + 3
                    elif ((lib_id == 'f' or lib_id == 'F') and n > 2):
                        QC = QC + ((2 ** n) - 3) + 2
                    elif ((lib_id == 'p' or lib_id == 'P') and n == 3):
                         QC = QC + 4
                    i=i+1

sheet = pe.get_sheet(file_name="/home/joy/Desktop/test/details.csv")
sheet.row[-1] = ['Quantum', 'Cost', '=',QC]
sheet.save_as("/home/joy/Desktop/test/details.csv")
