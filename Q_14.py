a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
b=[]
c=[]
min=1
max=0
while i < len(a):
    if len(a[i])>max:
        max=len(a[i])
        b=a[i]
    if len(a[i])<min:
        min=len(a[i])
        c=a[i]
    i+=1
print(max,b)
print(min,c)
