import itertools
import pyexcel as pe

outs=open('correct_output.txt', 'w')
a = 2 ** 4
total=list()


def truth_push(input_result):
    newstring = str(input_result[0])
    for ch in range(1,len(input_result)):
        newstring+=str(input_result[ch])
    levels.append(newstring)

def truth_fix(input_result):
    for n, i in enumerate(input_result):
        if i == True:
            result[n] = 1
        if i == False:
            result[n] = 0

def getheader(cc):
    che=['Level-'+str(cc+1)]
    for ch in range(cc):
        ches=cc-1-ch
        che.append('Level-'+str(ches+1))
        if ch == cc-1:
            che.append('Level-0')
    return che
def getheaders(cc,lines):
    che=[lines]
    for ch in range(cc):
        che.append(lines)
        if ch == cc-1:
            che.append(lines)
    return che


lines =str('a,b,c,d')
lines=lines.replace(',','')
testPatterns = table = list(itertools.product([0, 1], repeat=4))
for p in testPatterns:
    levels = list()
    a,b,c,d = p
    result = [a,b,c,d]
    truth_push(result)

    a = c ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = d ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = d ^ c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = not d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = a ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    a = (b and d) ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = b ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = c ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = (a and b) ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = (a and d) ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = (a and c) ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = (a and b and c) ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    a = c ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = (a and d) ^ c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    a = c ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = (a and c and d) ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)
    total.append(levels)
count = 15

che=list()

che=getheader(count)

ches=getheaders(count,lines)

total.insert(0,che)

total.insert(1,ches)

sheet=pe.Sheet(total)
tl=len(total[0])
print tl
outs.write(str(sheet.content))

sheet.save_as('../../Desktop/test/rev.csv')    



print sheet
sheet.save_as('../../Desktop/test/smart.csv')
execfile('../../Desktop/test/delee_column_rev.py')