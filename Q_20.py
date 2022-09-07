a=([1,1,1,1],2)
b=([20,37,20,21],1)
i=0
c=[]
c1=0
while i<len(a):
    c=a.count(a[i])
    if c==3:
        c.append(a[i])
    i=i+1
print(c)        

