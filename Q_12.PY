# 12 should return "10+2"
# 42 should return "40+2"
"70304 should return 70000+300+4"

# a="70304"
# i=0
# while i<len(a):
#     j=len(a)-(i+1)
#     b=int(a[i])*10**j
#     print(b,"+",end=" ")
#     i=i+1




a=[1,2,[2,4],4,7]
i=0
sum=0
while i<len(a):
    j=0
    b=[]
    while j<len(a):
        sum=sum+1
        b.append(sum)
        j=j+1
    i=i+1
    print(sum)        

