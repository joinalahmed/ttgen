n = int(input('level'))

b = raw_input('line')
with open('main.txt', 'r') as file:
# read a list of lines into data
    data = file.readlines()
# insert fault
if b in data[0]:
    data.insert(n+1, '0'+','+b+'\n')

# and write everything back
with open('main.txt', 'w') as file:
     file.writelines(data)