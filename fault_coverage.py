import csv
import itertools
from more_itertools import unique_everseen
import numpy as np
import ttpat
import pyexcel as pe
golbal_cts = list()

def searchers(search_list, n):
    #print search_list
    #print your_list2
    local_cts=list()
    for vec in range(len(search_list)):
        cd=your_list2[n+1].index(search_list[vec])
        local_cts.append(your_list2[0][cd])
    #print local_cts
    return local_cts


def searcher(search_list, n):
    #print search_list
    n -= 1
    local_cts = list()
    #print temp_list
    for s in range(len(temp_list[n])):
        try:
            #print temp_list[n][s]
            cd = search_list.index(temp_list[n][s])
            #local_cts.append(your_list2[0][cd])
            local_cts.append(temp_list[n][s])
        except:
            pass
    #print local_cts
    return local_cts


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
    # liter.sort()
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


with open('/home/joy/Desktop/finals.csv', 'r') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)
del (your_list1[0])
del (your_list1[0])
x = np.array(your_list1)
your_list1 = x.T
your_list2 = your_list1.tolist()
with open('/home/joy/Desktop/finals.csv', 'r') as f:
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
temp_list = list()
for j in range(len(your_list)):
    lists = your_lists[j]
    temp = your_lists[j]
    temp_list.append(temp)

for r in range(1, len(your_list2)):
    golbal_cts.append(searcher(your_list2[r], r))
#print golbal_cts
golbal_cts = ttpat.start(golbal_cts)
#print golbal_cts
global_cts=list()
for r in range(len(golbal_cts)):
    global_cts.append(searchers(golbal_cts[r], r))
print global_cts
golbal_cts=global_cts
golbal_cts = list(itertools.chain(*golbal_cts))
golbal_cts = list(unique_everseen(golbal_cts))
print golbal_cts
golbal_cts=np.array(golbal_cts).reshape(1,len(golbal_cts))
golbal_cts=golbal_cts.tolist()
sheet=pe.Sheet(golbal_cts)
sheet.save_as('/home/joy/Desktop/test/test_patterns_minimised.csv')