with open('/home/joy/Desktop/test/main.txt', 'r') as file1:
    data = file1.readlines()
with open('/home/joy/Desktop/test/faulty_data.txt', 'w') as file2:
    file2.writelines(data)