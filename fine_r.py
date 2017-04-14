import re
ff = open('image_tfc.txt', 'w')
name = '/home/joy/Desktop/test/a.tfc'
with open(name, 'r') as file_r:
    for line in file_r:
        if line.strip() == 'BEGIN':
            break
    for line in file_r:
        if line.strip() == 'END':
            break
        if line.strip() == '\n':
            continue
        line1 = re.split(',', line)
        length = len(line1)
        line2 = line1[0]
        line2 = re.split('\\s', line2)
        line2 = list(line2)
        line1[0] = line2[1]
        length1 = len(line1)
        line3 = line1[length1 - 1]
        length2 = len(line3)
        line3 = re.split('\n', line3)
        line1[length1 - 1] = line3[0]
        line_final = list()
        for ii in range(len(line1)):
            line_final.append(line1[ii])
            line_final.append(',')
        del line_final[-1]
        line_final1 = ''.join(line_final)
        ff.write(line_final1)
        ff.write('\n')


    ff.close()