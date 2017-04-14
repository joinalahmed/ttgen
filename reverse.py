# This Program takes a .tfc file as input, generates all possible gate level equations,
# generates all possible input permutations and display all gate level output matrices
import re
before=list()
count=0
name = '/home/joy/Desktop/test/a.tfc'

def reverse(text):
    a=list()
    print(text)
    for i in range(len(text)-1):
        a.append(text[i])
        if text[i] == 'BEGIN\n':
            break
    return a

with open(name) as infile:
    before=reverse(infile.readlines())

with open(name) as infile, open('/home/joy/Desktop/test/reverse.txt', 'w') as outfile:
    copy = False
    for line in infile:

        if line.strip() == "BEGIN":
            copy = True
        elif line.strip() == "END":
            copy = False
        elif copy:
            outfile.write(line + '\n')
with open('/home/joy/Desktop/test/reverse.txt', 'r') as file_reverse:

    liness = file_reverse.readlines()
    #print(liness)
    print(liness[3])

    liness=liness[::-1]
    before=before+liness
    before.append('END\n')

    while '\n' in before:
        before.remove('\n')
    print(before)

    ab=open('/home/joy/Desktop/test/rev.tfc','w')
    for i in range(len(before)):

        ab.write(str(before[i]))
    ab.close()
execfile('/home/joy/Desktop/test/revsim.py')