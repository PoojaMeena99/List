a=[1,1,2,3,4,4,5,1]
i=0
b=[]
s=[]
while i<len(a):
    j=0
    c=0
    d=[]
    while j<len(a):
        if a[i]==a[j]:
            c=c+1
        j=j+1
    d.append(c)
    d.append(a[i])
    if d not in b:
        b.append(d)
        if c==1:
            s.append(a[i])
        else:
            s.append(d)
    i=i+1  
print(s)                   

