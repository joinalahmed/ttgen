import pandas as pd
import csv,sys,operator

data = csv.reader(open('../../Desktop/test/reverse_output.csv'), delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(-1))
print sortedlist
with open("../../Desktop/test/reverse_output", "wb") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)
