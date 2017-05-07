import pandas as pd
import csv

df = pd.read_csv('../../Desktop/test/smart.csv')
df = df.sort('Level-0')
df.to_csv('../../Desktop/test/Full_List_sorted.csv', index=False)
with open('../../Desktop/test/Full_List_sorted.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

row_ins=your_list[-1]
your_list.insert(1,row_ins)
your_list.pop()
print your_list
with open('../../Desktop/test/smart.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(your_list)