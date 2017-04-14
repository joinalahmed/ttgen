import csv
import pyexcel as pe
file_1_tuples = []
file_1_tuples1 = []
with open("tests.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples.append(tuple(row))

file_1_tuples=file_1_tuples[2:]
with open("testsf.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples1.append(tuple(row))
file_1_tuples1=file_1_tuples1[1:]
length = len(file_1_tuples)
length1 = len(file_1_tuples)
#print length
sheet = pe.get_sheet(file_name="updates.csv")

for row in range(length):
    #print row
    #print file_1_tuples[row][-1]
    #print file_1_tuples1[row][-1]
    if file_1_tuples[row][-1] != file_1_tuples1[row][-1]:
        a =''.join(file_1_tuples[row][0])
        sheet.column += [a]
	#print 'no match'
sheet.save_as("test_patterns.csv")
print sheet
