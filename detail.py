from __future__ import print_function
import re
import re
import pyexcel as pe
import subprocess


def getheader():
    header_t = ['Gate', 'Controls', 'Target', 'Gate Type']
    return header_t


def truth_push(input_result):
    levels.append(input_result[0])
    levels.append(input_result[1])
    levels.append(input_result[2])
    levels.append(input_result[3])


main_li = []
sub_li = []
total = list()
che = getheader()

# GLOBAL VARIABLES AND FILES
gate1 = 'NOT GATE'
gate2 = 'C-NOT GATE'
gate3 = 'TOFFOLI GATE'
gate4 = 'FREDKIN GATE'
gate5 = 'SWAP GATE'
gate6 = 'PERES GATE'
var2 = []
count = 1
m11 = ''
my_fp = open("../../Desktop/test/tt_gen.py", "w")
my_fp.close()

qw = open("../../Desktop/test/main1.txt", "w")
qw.close()
ff = open('../../Desktop/test/test.txt', 'w')
ff.write('\n')
ff.close()


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
        mx = open('../../Desktop/test/tt_gen.py', 'a')
        mx.write(lo + '\n')
        mx.close()


# BLOCK FOR .tfc FILE PROCESSING , EXTRACTION OF DATA
with open('../../Desktop/test/a.tfc', 'r+') as file_tfc:
    for line in file_tfc:
        if line.strip() == 'BEGIN':
            break
    for line in file_tfc:
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
        ff = open('../../Desktop/test/test.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()


# LEVEL(S) DETAILS FUNCTION CALLER BLOCK


varn = var2
for inp in range(len(varn)):

    levels = list()
    varns = varn[inp]
    temp1 = varns[0]
    temp1 = str(temp1)
    r = re.compile("([a-zA-Z]+)([0-9]+)")
    m = r.match(temp1)
    m1 = m.group(1)
    m2 = m.group(2)

    # NOT GATE BLOCK
    if int(m2) == 1:
        gate = gate1
        control = 'NULL'
        target = varns[1]

        # C-NOT GATE BLOCK
    if (m1 == 't' or m1 == 'T') and int(m2) == 2:
        gate = gate2
        control = varns[-2]
        target = varns[-1]

        # TOFFOLI GATE BLOCK
    if m1 == 't' or m1 == 'T':
        if int(m2) > 2:
            gate = gate3
            del varns[0]
            for ii in range(len(varns) - 1):
                if ii == 0:
                    control = varns[ii]
                else:
                    control += ',' + varns[ii]
            target = varns[-1]

            # FREDKIN GATE BLOCK
    if (m1 == 'f' or m1 == 'F') and int(m2) > 2:
        del varns[0]
        gate = gate4
        for io in range(len(varns) - 2):
            control += ',' + varns[io]
        target = varns[-1]
        target += varns[-2]
        # SWAP GATE BLOCK
    if (m1 == 'f' or m1 == 'F') and int(m2) == 2:
        del varns[0]
        gate = gate5
        control = 'NULL'
        target = varns[0]
        target += varns[1]

        # PERES GATE BLOCK
    if m1 == 'p' or m1 == 'P':
        if int(m2) > 2:
            del varns[0]

            gate = gate6
    detail = [inp+1, control, target, gate]
    truth_push(detail)
    total.append(levels)
total.insert(0, che)
total.append(che)
sheet = pe.Sheet(total)
sheet.save_as('../../Desktop/test/details.csv')
res = subprocess.call(['python ../../Desktop/test/quantum.py'], shell=True)
