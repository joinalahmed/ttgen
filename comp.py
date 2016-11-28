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
file_1_tuples1=file_1_tuples1[2:]
length = len(file_1_tuples)
sheet = pe.get_sheet(file_name="updates.csv")
a=len(file_1_tuples[0])
b=len(file_1_tuples1[0])

for row in range(0, length-1):
    if file_1_tuples[row][-1] != file_1_tuples1[row][-1]:
        a =''.join(file_1_tuples[row][0])
        sheet.column += [a]
sheet.save_as("test_patterns.csv")