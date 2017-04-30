import csv
import pyexcel as pe
file_1_tuples = []
file_1_tuples1 = []
with open("../../Desktop/test/tests.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples.append(tuple(row))
file_1_tuples=file_1_tuples[2:]
with open("../../Desktop/test/testsf.csv") as fh:
    csv_reader = csv.reader(fh)
    for row in csv_reader:
        file_1_tuples1.append(tuple(row))
file_1_tuples1=file_1_tuples1[2:]
length = len(file_1_tuples)
length1 = len(file_1_tuples)
sheet = pe.get_sheet(file_name="../../Desktop/test/updates.csv")
for row in range(length):
    if file_1_tuples[row][-1] != file_1_tuples1[row][-1]:
        a =''.join(file_1_tuples[row][0])
        sheet.column += [a]
sheet.save_as("../../Desktop/test/test_patterns.csv")
