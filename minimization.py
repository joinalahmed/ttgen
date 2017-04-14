import csv,itertools
from more_itertools import unique_everseen

with open('/home/joy/Desktop/final.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
for i in range(len(your_list)):
    del(your_list[i][0])
del(your_list[0])
del(your_list[0])

your_list= sum(your_list, [])
your_list=list(unique_everseen(your_list))
print your_list