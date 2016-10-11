import itertools

outs=open('correct_output.txt', 'w')
a = 2 ** 3


def truth_push(input_result):
    levels.append('=>')
    levels.append(input_result)


def truth_fix(input_result):
    for n, i in enumerate(input_result):
        if i == True:
            result[n] = 1
        if i == False:
            result[n] = 0


testPatterns = table = list(itertools.product([0, 1], repeat=3))
for p in testPatterns:
    levels = list()
    a,b,c = p
    result = [a,b,c]
    levels.append(result)

    c = not c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = a ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    b = c ^ b
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    a = (b and c) ^ a
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = (a and b) ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = b ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = not c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = a ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    b = c ^ b
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    a = (b and c) ^ a
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = (a and b) ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    c = b ^ c
    result = [a,b,c]
    truth_fix(result)
    truth_push(result)

    outs.write(str(levels))  
    outs.write('\n')
