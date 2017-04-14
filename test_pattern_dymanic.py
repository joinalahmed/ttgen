import re, os, math
import itertools
from setuptools.package_index import unique_everseen

count = 0
test_set = []
name = '/home/joy/Desktop/test/a.tfc'
ads1 = 0
ff = open('output.csv', 'w')
ff.close()

with open('/home/joy/Desktop/test/a.tfc', 'r') as datafile:
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
print test_set
