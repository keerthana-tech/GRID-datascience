mylist=[1,0,3,9,0,0,4,8]
for i in mylist:
    if i==0:
        mylist.remove(i)
        mylist.append(i)
print(mylist)
