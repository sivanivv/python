#WHILE LOOP 1 2 5
# count=1
# while count<=5:
#     print(count)
#     count+=1

#with else
# count=1
# while count<=5:
#     print(count)
#     count+=1
# else:
#     print("Loop completed successfully")


#----------------------------------------------------------------------------------------------------------------



#1.Print numbers from 10 to 1,Write a Python program using a while loop to print numbers from 10 down to 1.

# f=10
# while f>=1:
#         print(f)
#         f-=1




#2.Sum of digits,Write a program that takes a number as input and calculates the sum of its digits using a while loop.
# a=int(input("Enter the Number : "))
# s=0
# add=0
# while a>0:
#     # print("sum of Digits:",s+d)
#     s=a%10
#     add+=s
#     a=a//10
# print("sum of Digits:",add)
    


#3.Check if a number is a palindrome,Write a Python program using a while loop to check if the entered number is a palindrome (same forwards and backwards)
# a=int(input("Enter a number : "))
# s=0
# add=0
# while a>0:
#     s=a%10
#     add+=s
#     a=a//10
#     if a==add:
#         print(a,"is Palindrome")
#     else:
#         print(a,"is not Palindrome")


    



#4.Count the number of digits,Input a number and count how many digits it has using a while loop.
# a=int(input("Enter a number : "))
# while a>0:
    







#5.Keep asking input until user enters ‘quit’,Write a program that keeps asking the user to enter a word, and stops only when they type 'quit'.
# a=input("Enter a word : ")
# while a!='quit':
#     a=input("Enter a word : ")
# else:
#     print("STOPPED")





#6 . Count how many times a digit appears,Input a number and a digit, then count how many times that digit appears in the number using a while loop.

# t=int(input("Enter a number  : "))
# r=int(input("Enter a number to check : "))
# while t==r:
#     print()

#------------------------------------------------------------------------------------------------------------------------------
#addition
# dd=int(input("Enter a Number : "))
# c=0
# while dd!=-1:
#     c+=dd
#     dd=int(input("Enter a Number : "))
# print(c)



# nested loop
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" " )
#     print()


# n=5
# c=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(c,end=" " )
#         c+=1
#     print()


#------------------------------------------------------------------------------------------------------------------------------


# Right half pattern
# n=6
# for i in range(0,n):
#     for j in range(0,i):
#         print("* ",end=" " )
#     print()
# ----------------------------------------- Right half pattern



# n=6
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("",end="   " )
#     for k in range(i):
#         print("* ",end=" " )
#     print()
# ----------------------------------------- Left half pattern


# n=6
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i):
#         print("* ",end="  " )
#     print()
# ----------------------------------------- full pyramid




# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("* ",end=" " )
        
#     print()
#------------------------------------------ inverted right half




# n=6
# for i in range(0,n):
#     for j in range(0,i):
#         print("",end="   " )
#     for k in range(n-i):
#         print("* ",end=" " )
#     print()
#------------------------------------------ inverted left half


# n=6
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" " )
#     for k in range(n-i):
#         print("* ",end="  " )
#     print()
#------------------------------------------ inverted pyramid



# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print("  ",end=" " )
#     for k in range(0,n):
#         print("* ",end="  " )
#     print()
# ------------------------------------------ rhombus pattern


# n=6
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i):
#         print("* ",end="  " )
#     print()
# n=6
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" " )
#     for k in range(n-i):
#         print("* ",end="  " )
#     print()
# ------------------------------------------ diamond pattern




# n=6
# for i in range(0,n):
#     if i==0:
#             continue
#     for j in range(0,i):
#         print(" ",end=" " )
#     for k in range(n-i):
#         print("* ",end="  " )
#     print()
# for i in range(0,n):
#     if i==0:
#          continue
#     if i==1:
#             continue
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i):
        
#         print("* ",end="  " )
#     print()
# ------------------------------------------ hourglass pattern


# n=5
# for i in range(0,n):
#     for j in range(0,n):
        
#             if i==0 or i==n-1 or j==0 or j==n-1:
#                 print("* ",end="  " )
            
#             else :
#                 print("  ",end="  ")
#     print()
#--------------------------------------------- hollow square pattern






# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i+1):
#          if k==0 or k==i or  i==n-1 :
#             print("* ",end="  " )
#          else :
#                 print("  ",end="  ")
       
#     print()
#---------------------------------------------hollow pyramid




# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for k in range(0,n-i):
#         if i==0 or k==0 or k==n-i-1:
#           print("* ",end="  ")
#         else:
#              print(" ",end="   ") 
#     print()
#---------------------------------------------hollow inverted pyramid



# n=5
# for i in range(0,n):
#     if i==n-1:
#         break
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i+1):
#          if k==0 or k==i or  i==n-1 :
#             print("* ",end="  "   )
#          else :
#                 print(" ",end="   ")
       
#     print()
# n=5
# for i in range(0,n):
#     if i==0:
#         continue
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for k in range(0,n-i):
#         if i==0 or k==0 or k==n-i-1:
#           print("* ",end="  ")
#         else:
#              print(" ",end="   ") 
#     print()
# ---------------------------------------------hollow inverted pyramid





# n=5
# c=1
# for i in range(0,n):
#     for j in range(0,i):
#         print(c,end=" " )
#         c+=1
#     print()
# ---------------------------------------------floyd's triangle




# n=5
# c=1
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" " )
#     for k in range(i):
#         print(c,end="   " )
#     print()