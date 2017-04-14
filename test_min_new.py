# This Program takes a .tfc file as input, generates all possible gate level equations,
# generates all possible input permutations and display all gate level output matrices
import re,os,subprocess
#os.remove("/home/joy/Desktop/final.csv")


import pandas as pd
data_input=1
sheet1=''
merged=''
before = list()
count = 0
name = '/home/joy/Desktop/test/a.tfc'
line_num = 0
end_num = 0
def line_nums():
    for n, line in enumerate(open("rev.tfc")):
      if "END" in line:
        line_num = n+1
      if "end" in line:
        line_num = n+1
    return line_num
def reverse(text):
    a = list()
    for i in range(len(text) - 1):
        a.append(text[i])
        if text[i] == 'BEGIN\n':
            break
    return a


with open(name) as infile:
    before = reverse(infile.readlines())

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
    before = before + liness
    before.append('END\n')
    while '\n' in before:
        before.remove('\n')
    ab = open('/home/joy/Desktop/test/rev.tfc', 'w')
    for i in range(len(before)):
        ab.write(str(before[i]))
    ab.close()

for n, line in enumerate(open("rev.tfc")):
    if "END" in line:
        line_num = n+1
    if "end" in line:
        line_num = n+1
num_lines = sum(1 for line in open('rev.tfc'))

for i in range(num_lines):


    if i == 0:
        execfile('/home/joy/Desktop/test/xys.py')
        sheet1 = pd.read_csv("/home/joy/Desktop/level_output.csv")
        data_input=0
        continue

    end_lines = sum(1 for line in open('rev.tfc'))

    rever = list()

    with open("rev.tfc", "r") as textobj:
        rever = list(textobj)
    line_num=line_nums()
    del rever[line_num-2]
    if (rever[-1] == 'end\n' or rever[-1] == 'END\n') and (rever[-2] == 'begin\n' or rever[-2] == 'BEGIN\n'):
        break
    with open("rev.tfc", "w") as textobj:
        for n in rever:
            textobj.write(n)
    execfile('/home/joy/Desktop/test/xys.py')
    sheet2 = pd.read_csv("/home/joy/Desktop/outputz.csv")
    sheet2 = sheet2.dropna(axis=1)
    sheet1 = sheet1.merge(sheet2, on='Test Pattern')
sheet1.to_csv("/home/joy/Desktop/final.csv", index=False)
print "Forward Simulation of CTS:"
print sheet1
