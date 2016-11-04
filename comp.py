import csv
import pyexcel as pe
file_1_tuples = []
file_1_tuples1 = []
with open("tests.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples.append(tuple(row))
with open("testsf.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples1.append(tuple(row))
length = len(file_1_tuples)
sheet = pe.get_sheet(file_name="updates.csv")
for row in range(1, length):
    if file_1_tuples[row][-1] != file_1_tuples1[row][-1]:
        print file_1_tuples[row][-1]
        a =''.join(file_1_tuples[row][0])
        sheet.column += [a]
sheet.save_as("test_patterns.csv")