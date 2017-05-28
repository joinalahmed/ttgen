import re
import subprocess
import os
import sys
from wand.image import Image

input_list = []
input_list1 = list
input_list2 = list
beta = list
tora = list
helium = list
delta = []
a3 = []
my_file = open('../../Desktop/test/qasm2circ-v1.4/image.qasm', 'w')
my_file.close()


with open('../../Desktop/test/converted_image.real', 'r+') as file:
    with open('../../Desktop/test/qasm2circ-v1.4/image.qasm', 'a') as file_1:
        for line in file:
            input_list.append(line)
        a1 = input_list.index('.begin\n')
        input_list1 = input_list[0:a1]
        for i in range(len(input_list1)):
            a2 = str(input_list1[i])
            if 'input' in a2:
                a3 = re.split(' ', a2)
                a3 = a3[1:-1]
                for iii in range(len(a3)):
                    file_1.write('        qubit   {0}\n'.format(str(a3[iii])))
        a4 = input_list.index('.begin\n')
        input_list2 = input_list[a4+1:-1]
        file_1.write('\n\n')

with open('../../Desktop/test/qasm2circ-v1.4/image.qasm', 'a') as lime:
    for i in range(len(input_list2)):
        alpha = input_list2[i]
        alpha = re.split('\\s', alpha)
        del alpha[-1]
        first_counter = a3[0]
        second_counter = a3[-1]
        if len(alpha) >= 3:
            beta = alpha
            gamma = str(beta[0])
            print gamma
            if len(gamma) == 2:
                if gamma[0] == 'T' or 't' and gamma[1] == '2':
                    var1 = beta
                    print var1
                    lime.write('        ' + 'cnot' + '   ' + str(var1[-3]) + ',' + str(var1[-2]) + '\n')

                if gamma[0] == 'v' and gamma[1] == '+':
                    var2 = beta
                    lime.write('        ' + 'c-z' + '    ' + var2[-2] + ',' + var2[-1] + '\n')

            if len(gamma) == 1:
                if gamma[0] == 'v':
                    var3 = beta
                    lime.write('        ' + 'c-x' + '    ' + var3[-2] + ',' + var3[-1] + '\n')

        if len(alpha) == 2:
            helium = alpha[0]
            if len(helium) == 2:
                if helium[0] == 'v' and helium[1] == '+':
                    vrigo = alpha
                    lime.write('        ' + 'S' + '      ' + vrigo[-1] + '\n')

                if len(helium) == 2:
                    if helium[0] == 't' or 'T' and helium[1] == '1':
                        qwerty = alpha
                        lime.write('        ' + 'not' + '    ' + str(qwerty[-1]) + '\n')

            if len(helium) == 1:
                myvar = alpha
                lime.write('        ' + 'X' + '      ' + myvar[-1] + '\n')

os.system('../../Desktop/test/qasm2circ-v1.4/qasm2png')
img=Image(filename="../../Desktop/test/qasm2circ-v1.4/image.eps")
with img.convert('jpg') as converted:
    converted.save(filename='../../Desktop/test/qasm2circ-v1.4/converted1.jpg')
