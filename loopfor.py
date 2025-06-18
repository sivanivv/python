#LOOPS

#1.for loop
# numbers=[4,5,6,8,1,3,7]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The list of squares is ",squares)

#using else statement with for loop
# string="Python Loop"
# for s in string:
#     if s=="o":
#         print("if block")
# else:
#     print(s)






#range()

# print(range(15))
# print(list(range(16)))
# print(list(range(18,30)))
# print(list(range(18,30,11)))


# tupleF=('m','c','a','p','a')
# for i in range(len(tupleF)):
#     print(tupleF[i].upper())



#NUMBER SUM

# a=int(input("Enter the limit : "))
# add=0
# for i in range(0,a+1):
#     add += i
    
# print(add)


#MULTIPLICATION TABLE

# h=int(input("Enter the Number : "))
# for i in range(1,11):
#     print(i,"x",h,"=",i*h)

# h=int(input("Enter the Number : "))
# r=int(input("Enter the range : "))
# for i in range(1,r+1):
#      print(i,"x",h,"=",i*h)


#FACTORIAL
# a=int(input("Enter the Number : "))
# f=1
# for i in range(2,a+1):
#     f*=i
# print("Factorial of ",a,"=",f)


#FIB
# d=int(input("Enter the Limit : "))
# fib=[0]
# f1=0
# f2=1
# f3=0
# for i in range(1,d):
#     f3=f1+f2
    
#     fib.append(f2)
#     f1=f2
#     f2=f3     
# print(fib)

#========================================================================


# # 1.Find the sum of all even numbers between 1 and N
# b=int(input("Enter the Limit : "))
# add=0 
# for i in range(0,b+1,2):
#     add += i
# print("Sum is : " ,add)



# 2.Count vowels in a string
# s=(input("Enter a String : "))
# vowels=['a','e','i','o','u']
# f=[]
# c=0
# for i in s:
#     if i in vowels:
#         f.append(i)
# c=len(f)
# print("Number of Vowels in ",s,"is : ",c) 
    
   



#3.Find the maximum number in a list,Given a list of numbers, use a for loop to find the maximum number.
# t=[737,73,282,28]
# m=t[0]
# for i in t:
#      if i>m:
#         m=i
# print("Maximum Number is : ",m)


  



#4.Calculate the product of all numbers in a list Given a list of numbers, write a program to calculate the product (multiplication) of all the numbers using a for loop.
# n=[2,5,8,4,7]
# f=1
# for i in n:
#     f*=i
# print("Product of Numbers : ",f)




#5.Reverse a string using a for loop,Input a string and print its reverse using a for loop.
# g=(input("Enter the String : "))
# d=''
# for i in g:
#     d=i+d
# print("Reverse of ",g,"is : ",d)





#6.Print characters at even indices,Input a string and use a for loop to print characters at even positions (index 0, 2, 4, …).
# d=str(input("Enter the String : "))
# h=len(d)
# c=0
# for i in range(0,h,2):
#     print(d[i])

    


#7.Find common elements in two lists,Input two lists and use a for loop to print elements present in both.

# l1=list(input("Enter  First list elements : "))
# print("first list " ,l1)
# l2=list(input("Enter  Second list elements : "))
# print("Second list " ,l2)
# l3=[]

# for i in l1:
#   for j in l2:
#     if i==j and j not in l3:
#        l3.append(i)
# print("Common Elements : " ,l3[:])



#8. Number of digits
# n=int(input("Enter the number : "))
# a=f"{n}"
# b=0
# for i in range(0,len(a)):
#     b+=int(a[i])
# print(b)
    
    
    
 
