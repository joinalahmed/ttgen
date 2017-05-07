def dels():
    readFile = open("/home/joy/Desktop/test/genf.py")

    lines = readFile.readlines()
    readFile.close()
    data = 0
    for i in range(len(lines) - 1):
        if lines[i] == '    #Bridging\n':
            data = i
    if data > 1:
        a = lines[:data]

        b = lines[data + 2:]
        lines = a + b
        print lines


dels()
