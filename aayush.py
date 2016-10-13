import re
import sys


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
        mx = open('tt_generator.py', 'a')
        mx.write('    '+lo + '\n')
        mx.close()


qw = open('main1.txt', 'w')
qw.close()
res = open('tt_generator.py', 'w')
res.close()


with open('a.tfc', 'r+') as file:
    for line in file:
        if line.strip() == 'BEGIN':
            break
    for line in file:
        if line.strip() == 'END':
            break
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
        ff = open('main1.txt', 'a')
        ff.write(line_final1)
        ff.write('\n')
        ff.close()


with open('a.tfc', 'r') as datafile:
    for line in datafile:
        line1=line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            rt = open('tt_generator.py', 'a')
            rt.write('import itertools' + '\n')
            rt.write('outs = open("a.txt", "w")')
            rt.write('\n')
            rt.write('#var_name = '+bb+'\n')
            cc = re.split(',', bb)
            asd = len(cc)
            asd1 = str(asd)
            rt.write('no_of_var = '+asd1+'\n')
            rt.write('alo = 2 ** '+asd1+'\n')
            rt.write('testPatterns = table = list(itertools.product([0,1], repeat=no_of_var))'+'\n')
            rt.write('for p in testPatterns:'+'\n')
            rt.write('    '+bb +'= p'+'\n')
            rt.close()
            break


with open('main1.txt', 'r+') as exp:
    for lenn in exp:
        if len(lenn) == 1:
            if lenn[0] == '\n':
                continue
        ax = lenn
        axx = re.split(',', ax)
        mn = len(axx)
        mn -= 1
        axx1 = str(axx[mn])
        axx2 = re.split('\n', axx1)
        axx[mn] = axx2[0]
        mn1 = len(axx)
        mn2 = mn1-1
        axx[mn2] = axx2[0]
        lenn = axx
        linen = list()
        for ii in range(len(lenn)):
            linen.append(lenn[ii])
            linen.append(',')
        del linen[-1]
        lenn = linen
        if len(lenn) == 1:
            benn = list(lenn)
            benn.append(' =')
            benn.append(' not')
            benn.append(' ')
            benn.append(benn[0])
            benn1 = ''.join(benn)
            tenn = open('tt_generator.py', 'a')
            tenn.write('    '+benn1+'\n')
            tenn.close()
        if len(lenn) == 3:
            tren = list(lenn)
            nn = len(tren)
            tren1 = list(tren[nn-1])
            ty = len(tren1)
            ty -= 1
            if tren1[ty] == ' ':
                del tren1[ty]
            tren1.append(' = ')
            tren1.append(tren[0])
            tren1.append(' ')
            tren1.append('^')
            tren1.append(' ')
            tren1.append(tren[nn-1])
            tren2 = ''.join(tren1)
            if "'" in tren2:
                al = list(tren2)
                al.remove("'")
                al1 = ''.join(al)
                tren2 = al1
            tren3 = open('tt_generator.py', 'a')
            tren3.write('    '+tren2+'\n')
            tren3.close()
            if "'" in str(lenn):
                neg_ctl(lenn)
        if len(lenn) > 3:
            list1 = list(lenn)
            num = len(list1)
            insert1 = num-1
            list2 = list1[insert1]
            list3 = list(list2)
            list3.append('=')
            list3.append('(')
            hg = len(list1)
            la_el = list1[hg-1]
            list1.insert(0, la_el)
            list1.insert(1, ' = ')
            list1.insert(2, '(')
            hg1 = len(list1)
            list1[hg1-2] = ' ^ '
            list1.insert(hg1-2, ')')
            z = 4
            ven = len(list1)
            for i in list1:
                list1[z] = ' and '
                z += 2
                if z == ven-3:
                    break
            qwerty = ''.join(list1)
            vs = ''.join(list1)
            if "'" in vs:
                vss = re.split("'", vs)
                vss1 = ''.join(vss)
                qwerty = vss1
            qwerty1 = open('tt_generator.py', 'a')
            qwerty1.write('    '+qwerty+'\n')
            qwerty1.close()
            if "'" in str(lenn):
                neg_ctl(lenn)


ml = open('tt_generator.py', 'a')
ml.write('    '+'result = '+'['+bb+']'+'\n')
ml.write('    '+'for n, i in enumerate(result):'+'\n')
ml.write('        '+'if i == 1:'+'\n')
ml.write('            '+'result[n]=1'+'\n')
ml.write('        '+'if i == 0:'+'\n')
ml.write('            '+'result[n]=0'+'\n')
ml.write('        '+"outs.write('Input Vector::'+str(p)+'\\n')"+'\n')
ml.write('        '+'for io in range(len(result)):'+'\n')
ml.write('            '+"print('Level'+'['+str(io)+']')"+'\n')
ml.write('            '+'print(str(p) + ' +"'=>'"+ ' + str(result))'+'\n')
ml.write('            '+"outs.write('Level'+'['+str(io)+']')"+'\n')
ml.write("            " + "outs.write(str(p) + " + "' => '" + "+ str(int(result)))"+'\n')
ml.write('            '+"outs.write('\\n')"+'\n')
ml.write('            '+"print('\\n')"+'\n')
ml.write('            '+"break"+'\n')
ml.write('        '+'outs.write('+"'##########################################################'"+')'+'\n')
ml.write('        '+"outs.write('\\n')"+'\n')
ml.write('outs.close()'+'\n')
ml.close()
