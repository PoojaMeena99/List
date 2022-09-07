a=[6,2,3,8]
i=0
s=0
s1=0
c=0
c1=0
while i<len(a):
    if a[i]%2==0:
        s=s+a[i]
        c=c+1
    else:
        s1=s1+a[i]
        c1=c1+1
    i=i+1
print(s,c)
print(s1,c1)