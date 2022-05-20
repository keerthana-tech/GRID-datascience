from collections import Counter
mylist="abcab"
count=Counter(mylist)
for i in count:
    if count[i]==1:
        print(i)
