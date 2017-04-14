# This Program takes a .tfc file as input, generates all possible gate level equations,
# generates all possible input permutations and display all gate level output matrices
import re,os
import itertools
from setuptools.package_index import unique_everseen
#os.remove("/home/joy/Desktop/outputs.csv")
count = 0
test_set = []
name = '/home/joy/Desktop/test/rev.tfc'
ads1 = 0
ff = open('output.csv', 'w')
ff.close()

import itertools,math
from setuptools.package_index import unique_everseen


with open('/home/joy/Desktop/test/rev.tfc', 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
            asd = len(cc)
            asd1 = str(asd)
            #print asd1
            break
    ff = open('main.txt', 'w')
    ff.write(bb)
    ff.write('\n')
    ff.close()
ones = '1'
zeros = '0'
length = int(math.ceil(math.log(asd, 2)))
for i in range(1, length + 1):
    number = pow(2, int(i))
    number /= 2
    first = list()
    for p in range(1, asd + 1):
        for k in range(number):
            first.append(zeros)
        for j in range(number):
            first.append(ones)
        firsts = ''.join(first)
    firsts=firsts[:asd]
    test_set.append(firsts)


with open('/home/joy/Desktop/test/rev.tfc', 'r') as datafile:
    dis = list(datafile)
    #print dis
    for line in datafile:
        line1 = line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
            asd = len(cc)
            asd1 = str(asd)
            break
    ff = open('main.txt', 'w')
    ff.write(bb)
    ff.write('\n')
    ff.close()


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
        hss = ''.join(hs_fin)
        jk = 'if ' + hs[0] + ' == 1: '
        jk1 = ''.join(jk)
        lo = jk1 + hss
        garbage.write('    '+lo + '\n')


def strings(bc):
    bc = list(bc)
    for j in range(len(bc)):
        if bc[j] == ',':
            continue
        else:
            bc[j] = 'str(' + bc[j] + ')'


garbage = open('gentest.py', 'w')
garbage.write("import itertools" + "\n")
garbage.write("import pyexcel as pe" + "\n")
garbage.write("\n")
garbage.write("outs=open('output.txt', 'w')" + "\n")
garbage.write("a = 2 ** " + asd1 + "\n")
garbage.write("\n")
garbage.write("total=list()" + "\n")
garbage.write("\n")
garbage.write("test_sets=[")
for q in range(len(test_set)):
    garbage.write("tuple(map(int,str('"+test_set[q]+"')))")
    if q==len(test_set)-1:
        garbage.write("]")
    else:
        garbage.write(",")

garbage.write("\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("def truth_push(input_result):" + "\n")
garbage.write("    newstring = str(input_result[0])" + "\n")
garbage.write("    for ch in range(1,len(input_result)):" + "\n")
garbage.write("        newstring+=str(input_result[ch])" + "\n")
garbage.write("    levels.append(newstring)")
garbage.write("\n")
garbage.write("\n")
garbage.write("def truth_fix(input_result):" + "\n")
garbage.write("    for n, i in enumerate(input_result):" + "\n")
garbage.write("        if i == True:" + "\n")
garbage.write("            result[n] = 1" + "\n")
garbage.write("        if i == False:" + "\n")
garbage.write("            result[n] = 0" + "\n")
garbage.write("\n")
garbage.write("def getheader(cc):"+"\n")
garbage.write("    che=['Test Pattern']"+"\n")
garbage.write("\n")
garbage.write("    for ch in range(cc):"+"\n")

garbage.write("        ches=cc-1-ch"+"\n")
garbage.write("        che.append('Level-'+str(ches))"+"\n")
garbage.write("        if ch == cc-1:"+"\n")
garbage.write("            che.append('Level-'+str(cc-1))"+"\n")
garbage.write("    return che")
garbage.write("\n")
garbage.write("def getheaders(cc,lines):"+"\n")
garbage.write("    che=[lines]"+"\n")
garbage.write("    for ch in range(cc):"+"\n")
garbage.write("        che.append(lines)"+"\n")
garbage.write("        if ch == cc-1:"+"\n")
garbage.write("            che.append(lines)"+"\n")
garbage.write("    return che")
garbage.write("\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("lines =str('"+bb+"')")
garbage.write("\n")
garbage.write("lines=lines.replace(',','')")
garbage.write("\n")
garbage.write("testPatterns = table = test_sets" + "\n")
garbage.write("for p in testPatterns:" + "\n")
garbage.write("    levels = list()" + "\n")
garbage.write('    ' + bb + ' = p' + '\n')
garbage.write("    result = [" + bb + "]\n")
garbage.write("    truth_push(result)" + "\n")
qw = open('main.txt', 'a')
ff = open('main1.txt', 'w')
with open(name, 'r') as file_r:
    for line in file_r:
        if line.strip() == 'BEGIN':
            break
    for line in file_r:
        if line.strip() == 'END':
            break
        if line.strip() == '\n':
            continue
        line1 = re.split(',', line)
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
        line_final1 = ''.join(line_final)
        ff.write(line_final1)
        ff.write('\n')
        qw.write(line_final1)
        qw.write('\n')
    ff.close()
with open('main1.txt', 'r+') as exp:
    for lenn in exp:
        count += 1
        garbage.write("\n")

        if len(lenn) == 1:
            if lenn == '\n':
                count -= 1
                continue
        ui = len(lenn)
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
        final_len = len(lenn)
        if len(lenn) == 1:
            benn = list(lenn)
            benn.append(' =')
            benn.append(' not')
            benn.append(' ')
            benn.append(benn[0])
            benn1 = ''.join(benn)
            garbage.write('    ' + benn1 + '\n')

        if len(lenn) == 3:
            tren = list(lenn)
            nn = len(tren)
            tren1 = list(tren[nn - 1])
            tren1.append(' = ')
            tren1.append(tren[0])
            tren1.append(' ')
            tren1.append('^')
            tren1.append(' ')
            tren1.append(tren[nn - 1])
            tren2 = ''.join(tren1)
            if "'" in tren2:
                vss = re.split("'", vs)
                vss1 = ''.join(vss)
                tren2 = vss1
            garbage.write('    ' + tren2 + '\n')
            if "'" in str(lenn):
                neg_ctl(lenn)
        if len(lenn) > 3:
            list1 = list(lenn)
            num = len(list1)
            insert1 = num - 1
            list2 = list1[insert1]
            list3 = list(list2)
            list3.append(' =')
            list3.append(' (')
            hg = len(list1)
            la_el = list1[hg - 1]
            list1.insert(0, la_el)
            list1.insert(1, ' =')
            list1.insert(2, ' (')
            hg1 = len(list1)
            list1[hg1 - 2] = '^ '
            list1.insert(hg1 - 2, ') ')
            z = 4
            ven = len(list1)
            for i in list1:
                list1[z] = ' and '
                z += 2
                if z == ven - 3:
                    break
            qwerty = ''.join(list1)
            vs = ''.join(list1)
            if "'" in vs:
                vss = re.split("'", vs)
                vss1 = ''.join(vss)
                qwerty = vss1
            garbage.write('    ' + qwerty + '\n')
            if "'" in str(lenn):
                neg_ctl(lenn)
        garbage.write("    result = [" + bb + "]\n")
        garbage.write("    truth_fix(result)" + "\n")
        garbage.write("    truth_push(result)" + "\n")
    garbage.write("    truth_push(result)"+"\n")
    garbage.write("    total.append(levels)" + "\n")
garbage.write('count = {0}'.format(str(count)))
garbage.write("\n")
garbage.write("\n")
garbage.write("che=list()")
garbage.write("\n")
garbage.write("\n")
garbage.write("che=getheader(count)")
garbage.write("\n")
garbage.write("\n")
garbage.write("ches=getheaders(count,lines)")
garbage.write("\n")
garbage.write("\n")
garbage.write("total.insert(0,che)")
garbage.write("\n")
garbage.write("\n")
garbage.write("total.insert(1,ches)")

garbage.write("\n")
garbage.write("\n")
garbage.write("sheet=pe.Sheet(total)")
garbage.write("\n")
garbage.write("\n")
garbage.write("outs.write(str(sheet.content))")
garbage.write("\n")
garbage.write("\n")
garbage.write("sheet.save_as('tests.csv')")

garbage.write("\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("\n")
garbage.write("value=len(sheet.column_range())")
garbage.write("\n")
garbage.write("sheet.column.select([0,value-1])")

garbage.write("\n")
garbage.write("sheet.save_as('/home/joy/Desktop/output.csv')")
garbage.write("\n")
garbage.write("\n")
#garbage.write("print(sheet)")
garbage.write("\n")
garbage.write("value=len(sheet.column_range())")
garbage.write("\n")
garbage.write("sheet.column.select([0,value-1])")

garbage.write("\n")

garbage.write("sheet.save_as('/home/joy/Desktop/outputs.csv')")
garbage.write("\n")
#garbage.write("print(sheet)")
garbage.write("\n")
garbage.close()
execfile('gentest.py')
