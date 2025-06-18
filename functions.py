#   FUNCTIONS


# def sqr(n):
#     return n**2
# obj=sqr(4)
# print("Square of 4 is ",obj)




# j=int(input("Enter the number: "))
# def sqr(j):
#     return j**2
# obj=sqr(j)
# print("The squre of",j,"is",obj)


#----------------------------------------


# def a_fun(string):
#     return len(string)

# print(a_fun("makeup"))
# print(a_fun("think"))

#----------------------------------------calling a function


# def sqr (n):
#     return n*n
# result=sqr(5)
# print("Square: ",result)

#----------------------------------------with argument with return type

# def greet(name):
#     print("Hello",name+"!")
# greet("kriti")

#----------------------------------------with argument without return type

# def get_message():
#     return "welcome!!"
# msg=get_message()
# print(msg)

#----------------------------------------without argument with return type


# def print_num():
#     for i in range(1,6):
#         print(i)

# print_num()

#----------------------------------------without argument without return type



#--------------------------------------------------------------------------------tasks
#--------------------------------------------------------------------------------

#1. With argument, with return type
# Q1. Write a function that takes a number as an argument and returns its square.


# def sqr(j):
#     return j**2
# j=int(input("Enter the number: "))
# obj=sqr(j)
# print("The squre of",j,"is",obj)


#Q3. Write a function that takes a string and returns it in uppercase.

# def upp(s):
#     return s.upper()
# s=input("Enter the string: ")
# obj=upp(s)
# print("Upper case: ",obj)
 
#-----------------------------------------------------------------------

# 2. With argument, without return type
# Q4. Write a function that takes a name as an argument and prints a greeting message.

# def greet(name):
#     print("Hello",name+"!")
# greet("kriti")


#Q5. Write a function that takes two numbers and prints their multiplication.

# def multi(w,e):
#     print("Multiplication: ",w*e)
# multi(2,4)

#Q6. Write a function that takes a number and prints whether it is even or odd

# def oddeven(f):
#     if f%2==0:
#         print("Number is even")
#     else:
#         print("Number is odd")
# oddeven(int(input("Enter a number: ")))

#------------------------------------------------------------------------------------------------

# 3. Without argument, with return type
# Q7. Write a function that returns the current year

# def currenty():
#     return "current year is 2025!!"
# year=currenty()
# print(year)

 
# Q8. Write a function that returns a default welcome message.

# def get_message():
#     return "welcome!!"
# msg=get_message()
# print(msg)

#Q9. Write a function that returns the value of 5 factorial (5!)

# def fivef():
#     return 1*2*3*4*5
# fact=fivef()
# print(fact)

#----------------------------------------------------------------------


# Without argument, without return type
# Q10. Write a function that prints your name

# def name():
#     print("Sivani V V")
# name()


# Q11. Write a function that prints numbers from 1 to 10

# def print_num():
#     for i in range(1,11):
#         print(i)

# print_num()

#--------------------------------------------------------------------
#--------------------------------------------------------------------

#FUNCTION ARGUMENTS

# def fun(n1,n2=20):
#     print('Number 1: ',n1)
#     print('Number 2: ',n2)
# fun(30)

#---------------------------------- default argumnet

# def fun(n1,n2=20):
#     print('Number 1: ',n1)
#     print('Number 2: ',n2)
# fun(n1=65,n2=20)

#---------------------------------- keyword argumnet

#ANONYMOUS FUNCTIONS

# lamda_=lambda argument1,argument2:argument1+argument2
# print('Value of function is: ',lamda_(20,30))
# print('Value of function is: ',lamda_(40,50))


#----------------------------------------------------------



#PYTHON FUNCTION WITHIN ANOTHER FUNCTION

# def word():
#     string='BYE'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()

#------------------------------------------------------

#RECURSIVE FUNCTION
# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return (x*fact(x-1))
# num=int(input("Enter a number: "))
# print("The factorial of ",num,"is",fact(num))

#--------------------------------------------------------------------
#--------------------------------------------------------------------task

#1. Write a function that takes a list of numbers and returns the maximum

# def max(l):
#     m=l[0]
#     for i in l:
#         if i>m:
#             m=i
#     return m
# x=[10,230,4,6,33]  
# a=max(x)
# print("max:",a)

#-------------------------------------------------------------------

#2. Define a function that returns the reverse of a given string

# def rev(s):
#     a=''
#     for i in s:
#         a=i+a
#     return a

# ss=input("Enter a string : ")

# b=rev(ss)
# print("Reverse: ",b)

#-----------------------------------------

#3. Write a function that takes a string and counts the number of vowels

# string=input("Enter the string: ")
# def cvow(s):
#     vow=['a','e','i','o','u']
#     l=[]
#     for i in string:
#         if i in vow :
#             l.append(i)
#     return (len(l))
# print("Number of vowels in ",string,"is: ",cvow(string))

#----------------------------------------------------------------

#4. Create a function to check if a number is a palindrome

# num=int(input("Enter a number: "))

# def palindrome(m):
#     g=f"{num}"
#     o=''
#     for i in g:
#         o=i+o
#     if o==g:
#             print(num,"is palindrome ")
#     else:
#             print(num,"is not palindrome ")

# palindrome(num)

#----------------------------------------------------

#5. Define a function that accepts a list and returns a new list with only even numbers

# f=[1,2,3,4,5,6,7,8,9,10]
# def even(m):
#     j=[]
#     for i in f:
#         if i%2==0:
#             j.append(i)
#     return j
# print("Your list: ",f) 
# print("List of even number: ",even(f))

#------------------------------------------------------------------------------------------

#6. Write a function that calculates the power of a number (without using ** or pow).

# h=int(input("enter the base: "))
# a=int(input("enter the Power: "))

# def power(d):
#     j=1
#     for i in range(1,a+1):
#        j*=d
#     return j
# print("Power: ",power(h))

#-------------------------------------------

#7. Create a menu-driven program using functions:a) Add two numbers b) Subtract two numbers c) Multiply two numbers d) Divide two numbers e) Exit (Use functions for each operation.)

# def add(e,n):
#     g=e+n
#     return g
# def sub(e,n):
#     g=e-n
#     return g
# def mul(e,n):
#     g=e*n
#     return g
# def div(e,n):
#     g=e/n
#     return g

# print(' 1.Addition\n','2.Subtraction\n','3.Multiplication\n','4.Division\n')
# op=()
# while op!=5:
#     op=int(input("Enter your option: "))
#     if op==1:
#         l=int(input("Enter First number: "))
#         ll=int(input("Enter second number: "))
#         print("Addition: ",add(l,ll))
#     elif op==2:
#         l=int(input("Enter First number: "))
#         ll=int(input("Enter second number: "))
#         print("Subtraction: ",sub(l,ll))
#     elif op==3:
#         l=int(input("Enter First number: "))
#         ll=int(input("Enter second number: "))
#         print("Multiplication: ",mul(l,ll))
#     elif op==4:
#         l=int(input("Enter First number: "))
#         ll=int(input("Enter second number: "))
#         if(ll==0):
#                 print('canonot divide by zero!!')
#         else:
#             print("Division: ",div(l,ll))
#     elif op==5:
#         print("EXITED!!")
#     else:
#         print("Invalid option!! TRY AGAIN!!")


#--------------------------------------------------------------------
#--------------------------------------------------------------------task

#RECURSIVE

#1. Write a recursive function to print numbers from n to 1

# def series(l):
#     if l==1:
#         return 1
#     else:
#         print(l)
#         return  series(l-1)
    
# u=int(input("Enter a number: "))
# print(series(u))

#-----------------------------------------

#2. Write a recursive function to calculate the sum of first n natural numbers

# def sumn(z):
#     if z==1:
#         return 1
#     else:
        
#         return  (z+sumn(z-1))

# a=int(input("Enter a number: "))
# print("Sum of Series: ",sumn(a))

#------------------------------------------

#3. Write a recursive function to find the sum of digits of a number.

# def sumdig(b):
#     if b==0:
#         return 0
#     else:
#         return b%10+sumdig(b//10)
  
# ss=int(input("Enter the digit: "))
# print("Sum of digits: ",sumdig(ss))

#----------------------------------------------

#4. Write a recursive function to reverse a string.

# def reverse(y):

  




#--------------------------------------------------------------------
#--------------------------------------------------------------------task

#LAMDA

#1. Write a lambda function to find the square of a number

# squ=lambda argument1: argument1 * argument1
# y=int(input("Enter the number: "))
# print("Square: ",squ(y))

#--------------------------------------------------------------------

#2. Write a lambda function to check if a number is even or odd

# y=lambda argument1:"Number is Even" if argument1%2==0 else "Number is Odd"
# i=int(input("Enter the number: "))

# print(y(i))

#-----------------------------------------------------------------------------------

#3. Write a lambda function to find the maximum of two numbers

# maxf=lambda argument1,argument2:"Max number is first number " if argument1>argument2 else "Max number is second number"
# u=int(input("Enter the first number: "))
# g=int(input("Enter the second number: "))
# print(maxf(u,g))

#----------------------------------------------------------------------------------------------------------------------------------

#4. Write a lambda function to check if a string starts with the letter 'A

# startm=lambda argument1 : "String starts with A" if argument1[0]=='A' or argument1[0]=='a' else "String does not starts with A"
# i=input("Enter the String: ")
# print(startm(i))




    















            




















