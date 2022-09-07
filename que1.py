# a=[1,2,4,5,2,3,5,2,6,2,7,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==2:
#         b.append(10)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)


# a=[1,2,3,2,1,2,3,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)   


# n=int(input("enter number"))
# b=[]
# i=1
# while i<=n:
#     num=int(input("enter numbers"))
#     b.append(num)
#     i=i+1
# print(b)


# a=[1,3,6,7,8]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# a=[1,3,6,7,8]
# i=0
# p=1
# while i<len(a):
#     p=p*a[i]
#     i=i+1
# print(p)

# a=[1,2,3,[4,5],[6,7,8]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     # else:
#     #     sum=sum+a[i]
#     i=i+1
# print(sum)



# a=[1,2,3,4,[5,6],1,2,[2,3,[5,6]]]

# a="shivani"
# i=0
# b=['a','e','i','o','u']
# while i<len(a):
#     if a[i] in b:
#         print("vowels",a[i])
#     else:
#         print("consonant",a[i])
#     i=i+1





# a=int(input("enter the no."))
# i=1
# b=[]
# while i<=(a):
#     num=int(input("enter the no."))
#     b.append(num)
#     i=i+1
# print(b)    


# a="shivi"
# i=0
# b=list(a)
# print(b)
    
# a='samiksha'
# b=0
# print(a[0])


# a=input("enter name")
# b=[]
# s=int(input("enter number"))
# i=0
# while i<len(a):
#     b.append(a[i])
#     i=i+1
#     b.append(s*i)
# print(b)    


# a=[1,2,3,4,5,6]
# i=0
# while i<len(a):
#     if a[i]==3:
#         print(i)
#     i=i+1    



# a=[1,2,-4,5,3,-7,8,-9,5,-4,3]
# i=0
# s=[]
# p=[]
# sum=0
# sum1=0
# while i<len(a):
#     if a[i]>0:
#         s.append(a[i])
#         sum=sum+a[i]
#     else:
#         p.append(a[i])
#         sum1=sum1+a[i]
#     i=i+1
# print(s,sum)
# print(p,sum1)            


#  a=[1,2,0,3,0,9,0,6,0,4,0]
# b=[]
# s=[]
# i=0
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         s.append(a[i])
#     i=i+1
# print(s+b)            




# n=input("enter the no ")
# a=["i","g","s","s","f","t","z"]
# i=0
# c=0
# while i<len(a):
#     if a[i]==n:
#         c=c+1
#     i=i+1 
# if c==1:    
#     print("present")



# a=["a","b","g","s","v","d","t","j","p","o","f"]
# b=["a","e","i","o","u"]
# i=0
# s=[]
# p=[]
# while i<len(a):
#     if a[i]not in b:
#         s.append(a[i])
#     else:
#         p.append(a[i])
#     i=i+1        
# print("cons",s)
# print("voble",p)






# a=["a","b","g","s","v","d","t","j","p","o","f"]
# b=["a","e","i","o","u"]
# i=0
# s=[]
# p=[]
# c=0
# c1=0
# while i<len(a):
#     if a[i]not in b:
#         s.append(a[i])
#         c=c+1
#     else:
#         p.append(a[i])
#         c1=c1+1
#     i=i+1        
# print("cons",s,c)
# print("voble",p,c1)





# a=[1,3,5,7,9,8,7,6,5,4,3,2,]
# b=[]
# c=0
# i=0
# while i<len(a):
#     if a[i]%1 and a[i]%i:
#         b.append(a[i])
#         c=c+1
#     else:
#         print(a[i])
#     i=i+1        
# print(b,c)




# a="hello world pooja"
# o=a.split()
# print(o)




a=["mom","race","wow","top","mahima"]
i=0
while i<len(a):
    