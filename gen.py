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
    che=['Input']
    for ch in range(cc):
        che.append('Level'+str(ch))
        if ch == cc-1:
            che.append('Output')
    return che


testPatterns = table = list(itertools.product([0, 1], repeat=4))
for p in testPatterns:
    levels = list()
    a,b,c,d = p
    result = [a,b,c,d]
    truth_push(result)

    c = a ^ c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = c ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    a = d ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = (b and d) ^ c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = a ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = (c and d) ^ b
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

    b = not b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = not c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    d = a ^ d
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = (b and d) ^ c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    a = (b and c) ^ a
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    b = (a and c) ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)

    c = not c
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)
    truth_push(result)
    total.append(levels)
count = 15

che=list()

che=getheader(count)

total.insert(0,che)

sheet=pe.Sheet(total)

outs.write(str(sheet.content))

sheet.save_as('test.csv')