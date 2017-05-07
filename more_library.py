import re
import prettytable

# GLOBAL VARIABLES AND FILES
var2 = []
count = 1
m11 = ''
my_fp = open("tt_generator.py", "w")
my_fp.close()

qw = open("main_new.txt", "w")
qw.close()

with open('../../Desktop/test/a.tfc', 'r') as datafile:
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
    ff = open('../../Desktop/test/main.txt', 'w')
    ff.write(bb)
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
        mx = open('tt_generator.py', 'a')
        mx.write(lo + '\n')
        mx.close()

# BLOCK FOR .tfc FILE PROCESSING , EXTRACTION OF DATA
with open('a.tfc', 'r+') as file:
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
        ff = open('main_new.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()


with open('tt_generator.py', 'a') as garbage:
 with open('main_new.txt', 'r+') as exp:
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

        # FREDKIN GATE AND SWAP GATE LIBRARY HANDLER
        if lib_id == 'F' or lib_id == 'f':
            lk = lenn
            # SWAP GATE HANDLER
            if len(lk) == 3:
                lk.remove(',')
                bn1 = 'temporary_variable' + ' = ' + str(lk[0])
                bn2 = str(lk[0]) + ' = ' + str(lk[1])
                bn4 = str(lk[1]) + ' = ' + 'temporary_variable'
                garbage.write('    '+bn1 + '\n')
                garbage.write('    '+bn2 + '\n')
                garbage.write('    '+bn4 + '\n')
                garbage.write('\n')

            # FREDKIN GATE HANDLER
            if len(lk) >= 3:
                ins = ''
                for lh in range(len(lk)):
                    ins += str(lk[lh])
                ins = re.split(',', ins)
                for il in range(len(ins) - 2):
                    mi = str(ins[il])
                    mi = mi + ' = ' + mi
                    garbage.write('    '+str(mi) + '\n')
                varx = list(ins[-2])
                varx.append(' = (')
                varx.append('(not (')
                varx1 = list(ins[-1])
                varx1.append(' = (')
                varx1.append('(not (')
                if len(ins) == 3:
                    varx.append(ins[0] + ')')
                    varx.append(') and ')
                    varx.append(ins[1])
                    varx.append(') ^ ')
                    varx.append('(')
                    varx.append(ins[0])
                    varx.append(' and ')
                    varx.append(ins[-1])
                    varx.append(')')
                    varxx = ''.join(varx)
                    varx1.append(ins[0] + ')' + ') ')
                    varx1.append('and ')
                    varx1.append(ins[-1] + ') ')
                    varx1.append('^ ' + '(' + ins[0] + ' and ' + ins[1] + ')')
                    vaxy = ''.join(varx1)
                    garbage.write('    '+varxx + '\n')
                    garbage.write('    '+vaxy + '\n')

                if len(ins) > 3:
                    tem = []
                    for ui in range(len(ins) - 1):
                        tem.append(ins[ui])
                        tem.append(' and ')
                    tem[-1] = '^ ('
                    tem.insert(0, ins[-2] + ' = (((not(')
                    tem.insert(-3, '))')
                    tem.insert(-1, ') ')
                    tem1 = []
                    for io in range(len(ins) - 2):
                        tem1.append(ins[io])
                        tem1.append(' and ')
                    tem1.append(ins[-1])
                    tem1.append('))')
                    tem = tem + tem1
                    vart = ''.join(tem)
                    garbage.write('    '+vart + '\n')
                    rt = []
                    for ik in range(len(ins) - 2):
                        rt.append(ins[ik])
                        rt.append(' and ')
                    rt.append(ins[-1])
                    rt.insert(0, ins[-1] + ' = (((not(')
                    rt.insert(-2, '))')
                    rt.append(') ^ (')
                    for zx in range(len(ins) - 2):
                        rt.append(ins[zx])
                        rt.append(' and ')
                    rt.append(ins[-2] + '))')
                    rt1 = ''.join(rt)
                    garbage.write('    '+rt1 + '\n')

        # PERES GATE LIBRARY HANDLER
        if lib_id == 'P' or lib_id == 'P':
            temp = list(lenn[2])
            temp.append('=' + lenn[0])
            temp.append('^' + lenn[2])
            temp123 = ''.join(temp)
            temp = list(lenn[4])
            temp.append('=')
            temp.append('(' + lenn[0])
            temp.append(' and ' + lenn[2])
            temp.append(')')
            temp.append('^' + lenn[4])
            temp223 = ''.join(temp)
            garbage.write('    '+temp123 + '\n')
            garbage.write('    '+temp223 + '\n')

        # NCT AND GT LIBRARY HANDLER
        if lib_id == 'T' or lib_id == 't':
            if len(lenn) == 1:
                benn = list(lenn)
                benn.append(' =')
                benn.append(' not')
                benn.append(' ')
                benn.append(benn[0])
                benn1 = ''.join(benn)
                garbage.write('    '+benn1 + '\n')
            if len(lenn) == 3:
                tren = list(lenn)
                nn = len(tren)
                tren1 = list(tren[nn - 1])
                ty = len(tren1)
                ty -= 1
                if tren1[ty] == ' ':
                    del tren1[ty]
                tren1.append(' =')
                tren1.append(tren[0])
                tren1.append('')
                tren1.append('^')
                tren1.append('')
                tren1.append(tren[nn - 1])
                tren2 = ''.join(tren1)
                if "'" in tren2:
                    al = list(tren2)
                    al.remove("'")
                    print(al)
                    al1 = ''.join(al)
                    tren2 = al1
                garbage.write('    '+tren2 + '\n')
                if "'" in str(lenn):
                    neg_ctl(lenn)

            if len(lenn) > 3:
                list1 = list(lenn)
                num = len(list1)
                insert1 = num - 1
                list2 = list1[insert1]
                list3 = list(list2)
                list3.append(' =')
                list3.append('(')
                hg = len(list1)
                la_el = list1[hg - 1]
                list1.insert(0, la_el)
                list1.insert(1, ' = ')
                list1.insert(2, '(')
                hg1 = len(list1)
                list1[hg1 - 2] = ' ^ '
                list1.insert(hg1 - 2, ')')
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
                print qwerty
                garbage.write('    '+qwerty + '\n')
                if "'" in str(lenn):
                    neg_ctl(lenn)
        garbage.write("    result = [" + bb + "]\n")
        garbage.write("    truth_fix(result)" + "\n")
        garbage.write("    truth_push(result)" + "\n")