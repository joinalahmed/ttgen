n = int(input('level'))
b = raw_input('lines')
with open('main.txt', 'r') as file_main:
    data = file_main.readlines()
data.insert(n, '&{0} \n'.format(b))
with open('main.txt', 'w') as file_main:
    file_main.writelines(data)
