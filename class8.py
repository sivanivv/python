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
    
 
