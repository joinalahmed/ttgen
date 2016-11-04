n = int(input('level'))
b = raw_input('lines')
with open('main.txt', 'r') as file:
# read a list of lines into data
    data = file.readlines()
data.insert(n, '&{0} \n'.format(b))

# and write everything back
with open('main.txt', 'w') as file:
     file.writelines(data)