import itertools
import pyexcel as pe

outs = open('../../Desktop/test/correct_output.txt', 'w')
a = 2 ** 3
total = list()


def truth_push(input_result):
    newstring = str(input_result[0])
    for ch in range(1,len(input_result)):
        newstring += str(input_result[ch])
    levels.append(newstring)


def truth_fix(input_result):
    for n, i in enumerate(input_result):
        if i == True:
            result[n] = 1
        if i == False:
            result[n] = 0


def getheader(cc):
    che=['Level-0']
    for ch in range(cc+1):
        che.append('Level-'+str(ch+1))
    return che

def getheaders(cc,lines):
    che=[lines]
    for ch in range(cc):
        che.append(lines)
        if ch == cc-1:
            che.append(lines)
    return che


lines = str('a,b,c')
lines = lines.replace(',','')
testPatterns = table = list(itertools.product([0, 1], repeat=3))
for p in testPatterns:
    levels = list()
    a,b,c = p
    #constant
    result = [a,b,c]
    truth_push(result)

    c=not c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c=a^c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    b=c^b
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    a=(b and c)^a
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c=(a and b)^c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c=b^c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)
    total.append(levels)
count = 5

che=list()

che=getheader(count)

ches=getheaders(count,lines)

total.insert(0,che)

total.insert(1,ches)

sheet=pe.Sheet(total)

outs.write(str(sheet.content))

sheet.save_as('../../Desktop/test/tests.csv')

sheet.save_as('../../Desktop/test/smart.csv')
sheet.save_as('../../Desktop/test/output.csv')
value=len(sheet.column_range())
sheet.column.select([0,value-1])
sheet.save_as('../../Desktop/test/correct_output.csv')
