# with is like your try .. finally block in this case
with open('main1.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

# now inject fault in nth level, note that you have to add a newline
n= input('Enter Level to  inject fault')
dappear= str(raw_input('And line to  inject fault'))
if dappear in data[0]:
    if dappear in data[n]:
        data[n]=data[n].replace(dappear,' ')
        data[n]=data[n].replace(', ','')
        data[n] = data[n].replace(' ,', '')

    print data[n]
# and write everything back
with open('main.txt', 'w') as file:
    file.writelines( data )