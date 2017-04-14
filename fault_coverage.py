import csv, itertools
from more_itertools import unique_everseen
import numpy as np


def compliment_0(lens):
    a = list()
    for n in range(lens):
        a.append('1')
    return ''.join(a)


def compliment_1(lens):
    a = list()
    for m in range(lens):
        a.append('0')
    return ''.join(a)


def checker(liter):
    #liter.sort()
    check_list = list()
    q = len(liter)
    for k in range(q):
        abc = list(liter[k])
        test = list()
        for l in range(len(abc)):
            if abc[l] == '0':
                test.append('1')
            if abc[l] == '1':
                test.append('0')
        abcd = ''.join(test)
        if abcd not in check_list:
            check_list.append(liter[k])
    return check_list


with open('/home/joy/Desktop/final.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
for i in range(len(your_list)):
    del (your_list[i][0])
del (your_list[0])
del (your_list[0])
x = np.array(your_list)
your_list = x.T
your_lists = your_list.tolist()
for i in range(len(your_list)):
    length = len(your_list[i][0])
    elem = compliment_1(length)
    elems = compliment_0(length)
    try:
        index_value = your_lists[i].index(elem)
    except ValueError:
        index_value = 'a'
    if index_value != 'a':
        del (your_lists[i][index_value])
    try:
        index_value = your_lists[i].index(elems)
    except ValueError:
        index_value = 'a'
    if index_value != 'a':
        del (your_lists[i][index_value])
temp_list=list()
for j in range(len(your_list)):

    lists=your_lists[j]
    temp=checker(your_lists[j])
    temp_list.append(temp)

print temp_list
