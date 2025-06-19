# CLASS

# class Employee:
#     id=10
#     name = "Demon"
#     def display(self):
#         print("ID: %d \nName: %s"%(self.id,self.name))
# emp=Employee()
# emp.display()

#----------------------------------------------------------------


# class Employee:
#     id=10
#     name = "Elena"
#     def display(self):
#         print("ID: %d \nName: %s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name   #--------------------------------------------- del to delete
# emp.display()

#------------------------------------------------------------ deleting object


# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=Car('Toyota',2016)
# c1.display()

#------------------------------------------------ constructor

# class Student:
#     def __init__(self):
#         print("This is non parametrized constructor")
#     def show(self,name):
#         print('Hello!',name)
# student=Student()
# student.show('Caroline')

#-------------------------------------------------------- non parametrized constructor

# class Student:
#     roll_no=101
#     name="Bonnie"

#     def display(self):
#         print(self.roll_no,self.name)

# st=Student()
# st.display()

#--------------------------------------------- default constructor

# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age

# s=Student("Matt",101,19)

# print(getattr(s,'name'))  #----------------------- to get attribute (specific or not)

# setattr(s,"age",18)       #----------------------- update attribute 
# print(getattr(s,'age'))  


# print(hasattr(s,'id'))    #----------------------- prints true if student contains attribute id

# delattr(s,'age')          #----------------------- for deleting attributes
# print(s.age)

#--------------------------------------------------------------------------------------------- attributes
#---------------------------------------------------------------------------------------------


#QUESTIONS

#1.Create a class Student with attributes name, roll_number, and marks.Add a method to display student details

# class Student:
#     def __init__(self,name,roll_number,marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#     def display(self):
#         print(' Name:',self.name ,'\n','Roll no:',self.roll_number,'\n','Marks:',self.marks)

# st=Student('Kamal',4,24)
# st.display()

#------------------------------------------------------------------------------------------------------


#2.Create a class Rectangle with attributes length and width.Add a method to calculate and display the area

        
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print('Area: ',self.length*self.width)
# ar=Rectangle(2,24)
# ar.area()

#-----------------------------------------------------------


#3.Create a class Car with attributes brand, model, and year.Add a method to display full details of the car


# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display(self):
#         print('Brand:',self.brand ,'\nModel:',self.model,'\nYear:',self.year)
# c=Car('Porsche','911 GT3 RS',2022)
# c.display()


#------------------------------------------------------------------------------------------


#4.Create a class Person with attributes name and age.Add a method to check if the person is eligible to vote (age ≥ 18)


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def votee(self):
#         if self.age<18:
#             print(self.name,'is not eligible to vote !!')
#         else:
#           print(self.name,'is  eligible to vote !!')  

# pv=Person('Sia',)
# pv.votee()

#----------------------------------------------------------------------


#5.Create a class BankAccount with attributes account_holder and balance.Add methods to deposit, withdraw, and check balance.


# option=()
# while option!=4:
#     print('1) Deposit money\n','2) Withdraw money\n','3) Display account details\n ','4) Exit\n',)

#     option=int(input("What is your need? enter your option : "))

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#     def deposit(self,dep):
#         if dep<0:
#             print('Invalid Amount!!')
#         else:
#             self.balance+=dep
#             print('Current balance:',self.balance)
#     def withdraw(self,wid):
#         if wid<0:
#             print('Invalid Amount!!')
#         else:
#             self.balance-=wid
#             print('Current balance:',self.balance)
#     def details(self):
#         print('Account details','\nAccount holder:',self.account_holder,'\nBalance:',self.balance)

# ab=BankAccount('Tina',1231)
# ab.deposit(9)
# ab.withdraw(1)
# ab.details()


        