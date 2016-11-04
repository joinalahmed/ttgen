import itertools
import re

num_format = re.compile("[0-9]")


def fun(S, K):
    K = int(K)
    if K == 0:
        return S
    R = S + S[::-1]
    return fun(R, K - 1)
def substr(string):
    j=1
    a=set()
    while True:
        for i in range(len(string)-j+1):
            a.add(string[i:i+j])
        if j==len(string):
            break
        j+=1
    return a

kases = int(raw_input())
for kase in range(kases):
    a, b = raw_input().split()
    isnumber = re.match(num_format, a)
    if isnumber:
        s = fun(a, b)
        com =list(substr(s))
        c = 0
        for e in range(len(com)):
            if int(com[e]) % 3 == 0:
                c += 1
        print c
