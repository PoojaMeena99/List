# names_list=["annu","shivam","deepu","pooja","rupa"]
# names_list[0]="abhishek"
# print(names_list)

# num=[50,40,23,70,56,12,5,10,7]
# count=0
# i=0
# while i<len(num):
#     count=count+1
#     i=i+1
# print(count)



# a=["anhisek","shivam","deepu","pooja","rupa"]
# a[3]="rishav"
# print(a)


# a=["shivani","pooja","simmi","veera"]
# a[2]="bulubul"
# print(a)


# names_list=["annu","shuvam","deepu","pooja","rupa"]   ["OUT OF RANGE"]
# names_list[8]="priti"
# print(names_list)

# index=0    
# name_list=["a","s","b","p","g",]
# a=len(name_list)
# print((name_list)[index])


# student_list=["rohit","anamika","faisal","valmiki","waseem","sanjay"] 
# print(student_list.index("faisal"))

# student_list=["rohit","anamika","faisal","valmiki","waseem","amara"]
# list_length=len(student_list)
# index=0
# while index<list_length:
#     print(student_list[index])
#     index=index+1



# student=[23,45,89,90,56,80]
# length=len(student)
# index=0
# marks=0
# while index<len(student):
#     marks=student[index]+marks
#     index=index+1
#     print("marks :"+str(marks))


# str=["robin","anamika","faisal","valmiki","waseem","amara"]
# list=len(str)
# index=0
# while index<len(str):
#     print(str[index])
#     index=index+1



# from operator import index

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# marks=0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:             
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
# index = index + 1
# print("Marks more than 50: " + str(more_than50))
# print("Marks less than 50: " + str(less_than50)) 


# txt = " Hello World "
# x = txt.strip()
# print(x)

# LIST A AND LIST B ELEMENT APPEND IN EMPTY LIST

# a=[1,2,3,4,5,6,]
# b=[2,3,1,0,6,7]
# i=0
# s=[]
# while i<len(a):
#     if a[i] not in b:
#         s.append(a[i])
#     i=i+1
# print(s)       

# TOTAL SUM OF LIST

# a=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1 
# print(sum)       



# SUM OF ALL LIST

# a =[[78,76,94,86,88],[91,71,98,65],[95,45,78]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
#     print(sum)


# BIG NUMBER IN A LIST

# a=[[3,4,5,1],[33,6,1,2]]
# b=a[0][0]
# for i in  a:
#     for j in i:
#         if j>b:
#             b=j
# print(b)

# BIG NUMBER IN A LIST

# a=[[3,4,5,1],[33,6,1,2]]
# m=a[0][0]
# i=0
# count=0
# while i<len(a):
#     j=0
#     count=count+1
#     while j<i:
#         count=count+1
#         if a[i][j]>m:
#             m=a[i][j]
#         j+=1
#     i+=1
# print(m)

# BIG NUMBER IN A LIST

# a=[[3,4,5,1],[33,6,1,2]]
# v=a[0][0]
# for i in a:
#     for element in i:
#      if v> element:
#         v=element
# print(v)


 
#BIG NO. IN A LIST

# a=a[0][0]
# i=0
# m=0
# while i<len(a):
#     j=0
#     while j<i:
#         if v<i:
#             v=a[i][j]
#         j=j+1
#     i=i+1
# print(v)



# v=[[3,4,5,1],[33,6,1,2]]
# alist=["pynative",[4,8,12,16]]
# print(alist[0][1])
# print(alist[1][3])

# FIND AVG

# a = [
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65, 76],
# [95, 45, 78, 52, 49]
# ]
# i=0
# while i<len(a):
#     j=0 
#     sum=0
#     while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1
#     s=sum/len(a[i])
#     i=i+1
#     print(s)



#BIG NO. IN A LIST 

# a=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# while i<len(a):
#     count=count+1
#     i=i+1
# print(count)    



# FINE LESDEN AND MOREDEN NO. OF 20 TO 40

# num=[50,40,23,70,56,12,5,10,7]
# i=0
# count=0
# b=[]
# while i<len(num):
#     if  num[i]>20 and num[i]<40:
#         # count=count+1
#         b.append(num[i])
#     i=i+1
# # print(count)
# print(b)



# FIND MAXIMUM NO.

# num=[50,40,23,70,56,12,5,10,7]
# index=0
# max=0
# while index<len(num):
#     if num[index]>max:  
#        max=num[index]
#     index=index+1
# print(max)  

# APPEND FUN USE IN LIST

# a=[1,2,3,4,5]
# b=[6,7,3,2,1]
# index=0
# count=0
# p=[]
# while index<len(a):
#     if a[index] not in b:
#         p.append(a[index])
#         count=count+1
#     index=index+1
# print(p)   
# print(count)     

        
# FIND AVG

# a = [
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78]
# ]
# i=0
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#             sum=sum+(a[i][j])
#             j=j+1    
#     p=sum/len(a[i])
#     i=i+1
#     print(p)


# marks = [
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65],
# [95, 45, 78],
# [87, 67, 49, 68, 88]
# ]
# i=0
# while i<len(marks):
#     j=0 
#     sum=0
#     while j<len(marks[i]):
#             sum=sum+(marks[i][j])
#             j=j+1
#     s=sum/len(marks[i])  
#     i=i+1
#     print(s)


#SECOND MEXIMUM QUESTION
# num = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# max=0    
# m1=0 
# while i<len(num):    ["ERROR IN QUESTION"]
#     if num[i]<max:        
#         max!=m1
#     else: 
        
#     i=i+1
# print(m1)    



# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# s=[]
# while i<len(n):
#     j=0
#     b=[]
#     while j<len(n):
#         if n[i]+n[j]==number:
#             b.append(n[i])
#             b.append(n[j])
#             s.append(b)
#         j=j+1
#     i=i+1
# print(s)        




# a=int(input("inter no"))
# b=int(input("inter no"))
# while a<=b:
#     if a%2==0:
#         print(a)
#     a=a+1




# a=int(input("enter the no  "))
# for i in range(1,11):
#     print(a*i)




# for i in range(8,81,8): 
#     print(i)

    

# a=[0,1,2,0,3,4,0,5,0,]
# i=0
# b=[] 
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(c+b)    


# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# i=0
# b=[]
# while i<len(students):
#     b.append((students[i]+"=",str(marks[i])))
#     i=i+1
# print(b)    
# print(len(students))
# print(len(marks))



# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks=[20,45,76,19,20,54]
# c=0
# b=[]
# while c < len(students):
#        b.append([students[c] +"=" ,str(marks[c])])
#        c+=1
# print(b)



# a = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# count=0
# count1=0
# s=0
# p=0
# while i<len(a):
#     if a[i]%2==0:
#         count=count+1
#     else:
#         count1=count1+1
        
#     i=i+1
# print(count)   
# print(count1)  



# e= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# p=0
# s=0
# while i<len(e):
#     if e[i]%2==0:
#         p=p+e[i]
#     else:
#         s=s+e[i]
#     i=i+1
# print(p)  
# print(s) 
        


# e= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# count=0
# count1=0
# while i<len(e):
#     if e[i]%2==0:
#         sum=sum+e[i]
#         count=count+1
#     else:
#         sum1=sum1+e[i]
#         count1=count1+1
#     i=i+1
# print(sum/count)
# print(sum1/count1)   



    # ["AVG+SUM+COUNT"]

# e= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# sum1=0
# count=0
# count1=0
# while i<len(e):
#     if e[i]%2==0:
#         sum=sum+e[i]
#         count=count+1
#     else:
#         sum1=sum1+e[i]
#         count1=count1+1
#     i=i+1
# print(sum/count)
# print(sum1/count1)   
# print(sum)
# print(sum1)
# print(count)
# print(count1)
# 
# 


# kbc=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
# i=0
# count=0
# count1=0
# count2=0
# while i < len(kbc):
#     if  kbc[i]>=10000000:
#         print("carodpati")
#         count=count+1
#     elif kbc[i]>=100000:
#         print("lakhpati")
#         count1=count1+1
#     else:
#         print("dilbale")
#         count2=count2 +1 
#     i=i+1
# print(count,"crorpati")
# print(count1,"lakhpati")
# print(count2,"dilvale")






a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
b=[]
while i<len(a):
    c=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    if a[i] not in b:
            b.append(a[i])
            print([a[i],c],end="")
    i+=1




# a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     f=[]
#     while j<len(a):
#         c=a.count(a[i])
#         j=j+1
#     if a[i] not in f:
#         f.append (a[i])
#         f.append(c)
#     if f not in b:    
#         b.append(f)
#     i=i+1
# print(b)        






# char_list=[]
# print(char_list)



# n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i=0
# b=[]
# p=[]
# while i<len(n):
#     c=n.count(n[i])
#     if c==1:
#         b.append(n[i])
#     else:
#         p.append(n[i])
#     i=i+1
# print(b)
# print(p)
# # print(b+p)




# n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i=0
# b=[]
# while i<len(n):
#     if (n[i]) not in b:
#         b.append(n[i])
#     i=i+1
# print(b)        



# str="the quick brown fox jumped over the lazy dog .the dog slept  over the verandah . "
# sub="over"
# a=str.split()
# # print(a)                 ["not right"]
# print(len(str))
# del  str[5]
# print(str)



# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# s= 0
# i= 0
# while i< len(marks):
#     s = s+int((marks[i]))
#     i= i+ 1
# print(s)



# name = ["Savitri", "Phule", "26"]
# # p=(name[0]+name[1]+name[2])
# # print(p.split())
# print(name)


# index=[]
# c=0
# while i<len(grocery_list):
#     if grocery_list==index:
#         index.append(grocery_list)
#         c=c+1
#     i=i+1
# print(str(grocery_list)+str(index))    








