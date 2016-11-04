# with is like your try .. finally block in this case
with open('main1.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

# now inject fault in nth level, note that you have to add a newline
n=input('Enter Level in which fault is to be Injected (1-n) \n')
data[n-1] = '\n'

# and write everything back
with open('main1.txt', 'w') as file:
    file.writelines( data )