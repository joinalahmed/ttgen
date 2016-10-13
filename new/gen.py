import itertools
import pyexcel as pe

outs=open('correct_output.txt', 'w')
a = 2 ** 5
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
    che=['Input']
    for ch in range(cc):
        che.append('Level'+str(ch))
        if ch == cc-1:
            che.append('Output')
    return che


testPatterns = table = list(itertools.product([0, 1], repeat=5))
for p in testPatterns:
    levels = list()
    a1,a2,a3,a4,a5 = p
    result = [a1,a2,a3,a4,a5]
    truth_push(result)


    a1 = not a1
    result = [a1,a2,a3,a4,a5]
    truth_fix(result)
    truth_push(result)

    a5 = (a3 and a4) ^ a5
    result = [a1,a2,a3,a4,a5]
    truth_fix(result)
    truth_push(result)

    a2 = (a2 and a3 and a5) ^ a2
    if a3 == 1: a3 = not a3
    if a5 == 1: a5 = not a5
    result = [a1,a2,a3,a4,a5]
    truth_fix(result)
    truth_push(result)

    a2 = (a2 and a3 and a5) ^ a2
    if a1 == 1: a1 = not a1
    result = [a1,a2,a3,a4,a5]
    truth_fix(result)
    truth_push(result)
    truth_push(result)
    total.append(levels)
count = 4

che=list()

che=getheader(count)

total.insert(0,che)

sheet=pe.Sheet(total)

outs.write(str(sheet.content))

sheet.save_as('test.csv')