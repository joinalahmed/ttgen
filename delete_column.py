import pandas as pd
import pyexcel
with open('../../Desktop/test/state_smart.txt', 'rb') as state_smart:
    state=state_smart.readlines()
val_1=int(state[0])
val_2=int(state[1])
f=pd.read_csv("../../Desktop/test/smart.csv")
keep_col=[]
tl= len(f.columns)
for i in range(val_1,val_2+1):
    #print i
    leveldel="Level-"+str(i)
    keep_col.append(leveldel)
new_f=f[keep_col]
new_f.to_csv("../../Desktop/test/smart.csv",index=False)
sheet = pyexcel.get_sheet(file_name="../../Desktop/test/smart.csv")
outs=open('../../Desktop/test/smart_output.txt','w')
outs.write(str(sheet.content))
outs.close()
