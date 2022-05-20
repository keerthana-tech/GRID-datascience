mylist=[1, 5, 3, 2]
count=0
for i in range(len(mylist)-1):
    for j in range(i+1,len(mylist)):
        if mylist[i]+mylist[j] in mylist:
            count+=1
print(count)
