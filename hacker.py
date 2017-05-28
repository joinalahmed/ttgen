import itertools
def anagrams(word):
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if not letter in word[:i]:
                for j in anagrams(word[:i]+word[i+1:]):
                    yield j+letter
val =int( raw_input())
for i in range(val):
     num1,num2= raw_input().split()
     num1=str(num1)
     num2=int(num2)
     a=list(anagrams(num1))
     b=list(set(a))
     b.sort(key=a.index)
     b.sort()
     print b[num2 - 1]
