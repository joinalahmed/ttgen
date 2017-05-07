import re
cc=list()
cd=0
bias=0
def dels(cc,bias):
    readFile = open("/home/joy/Desktop/test/gen.py")

    lines = readFile.readlines()
    readFile.close()
    data = 0
    for i in range(len(lines) - 1):
        if lines[i] == '    #constant\n':
            data = i
            break
    with open("/home/joy/Desktop/test/gen.py",'r')as writefile:
        text=writefile.readlines()
        for i in range(len(cc)):
            print data
            text.insert(data,'    '+str(cc[i]+'='+str(bias)+"\n"))
            #text.insert(data+1,'\n')

    print text
    with open("/home/joy/Desktop/test/gen.py", 'w')as writefile:
        writefile.writelines(text)

with open('../../Desktop/test/a.tfc', 'r') as datafile:
    for line in datafile:
        line1 = line.strip()
        if '.c' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            ce = re.split(',', bb)
            cd=len(ce)
            bias=ce[0]
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            cc = re.split(',', bb)
    if cd >0:
        a=len(cc)
        cc=cc[a-cd:a]
        dels(cc,bias)



