def nk(mylist,n,k):
    kelem=[]
    for i  in mylist:
        if i>k:
            kelem.append(i)
    kelem=kelem[::-1]
    print(kelem[n-1])
  
        
        
        
mylist=[1,2,3,4,5,6,7,8]
nk(mylist,3,5)


