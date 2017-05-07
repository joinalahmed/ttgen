readFile = open("genf.py")

lines = readFile.readlines()
print 'EXE'
readFile.close()
w = open("genf.py",'w')
w.writelines([item for item in lines[:-3]])
w.close()
