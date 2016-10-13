import itertools
outs = open("a.txt", "w")
#var_name = a1,a2,a3,a4,a5
no_of_var = 5
alo = 2 ** 5
testPatterns = table = list(itertools.product([0,1], repeat=no_of_var))
for p in testPatterns:
    a1,a2,a3,a4,a5= p
    a3 = a1 ^ a3
    a5 = (a3 and a4) ^ a5
    a5 = (a2 and a3) ^ a5
    if a3 == 1: a3 = not a3
    a3 = a1 ^ a3
    if a1 == 1: a1 = not a1
    result = [a1,a2,a3,a4,a5]
    for n, i in enumerate(result):
        if i == 1:
            result[n]=1
        if i == 0:
            result[n]=0
        outs.write('Input Vector::'+str(p)+'\n')
        for io in range(len(result)):
            print('Level'+'['+str(io)+']')
            print(str(p) + '=>' + str(result))
            outs.write('Level'+'['+str(io)+']')
            outs.write(str(p) + ' => '+ str(int(result)))
            outs.write('\n')
            print('\n')
            break
        outs.write('##########################################################')
        outs.write('\n')
outs.close()
