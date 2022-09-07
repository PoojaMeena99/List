# "DIVISIVALE VALUE"

# n=[2,3,4,6,7,89,12,43,64]
# i=0
# s=[]
# c=[]
# while i<len(n):
#     if n[i]%2==0:
#         s.append(n[i])
#     else:
#         c.append(n[i])
#     i+=1
# # print(s)
# # print(c)
# print(s+c)


# "2%N VALUE COME IN LAST"

# a=[2,3,4,6,7,89,12,43,64]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(1)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[1,2,[],5,[[],3,[]],6]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if a[i][j]!=[]:
#                 b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)                


# a=["simmi","pooja","veerpal","sivani"]
# i=0
# b=[]
# m=0
# while i<len(a):
#     if len (a[i])>m:
#         m=len(a[i])
#         b=a[i]
#     i=i+1
# print(b,m)    



# a=[1,[2,3,5],[7,6],8,4]
# i=0
# s=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             s=s+a[i][j]
#             j=j+1
#     else:
#         s=s+a[i]    
#     i=i+1
# print(s)    



# a=["s2001","p2000","v500","r350"]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     s=" "
#     while j<len(a[i]):
#         if a[i][j]>"a" and a[i][j]<"z":
#             s=s+a[i][j]
#         j=j+1
#     c.append(s)
#     i=i+1
# print(c)


a="pooja"
i=0
b=[]
c=5
while i<len(a):
    b.append(a[i])
    b.append(c)
    c=c+5
    i=i+1
print(b)    