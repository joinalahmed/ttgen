import pandas as pd
import subprocess
import pyexcel

subprocess.call(['python ../../Desktop/test/sort_sim.py'], shell=True)
with open('../../Desktop/test/state_smart.txt', 'rb') as state_smart:
    state=state_smart.readlines()
val_1=int(state[0])
val_2=int(state[1])
f = pd.read_csv("../../Desktop/test/smart.csv")
keep_col=[]
tl= len(f.columns)
for i in range(val_1,val_2):
    leveldel="Level-"+str(i)
    keep_col.append(leveldel)

keep_col=keep_col[::-1]
new_f=f[keep_col]
new_f.to_csv("../../Desktop/test/smart.csv",index=False)
sheet = pyexcel.get_sheet(file_name="../../Desktop/test/smart.csv")
print sheet
outs=open('../../Desktop/test/smart_output.txt','w')
outs.write(str(sheet.content))

sheet.save_as('../../Desktop/test/smarts.csv')
outs.close()