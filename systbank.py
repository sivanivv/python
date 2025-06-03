print('a) Create new account \n','b) Deposit money \n','c) Withdraw money\n','d) Display account details \n ','e) Exit \n',)
menu=['a','b','c','d','e']
n=int(input("What is your need? enter option : "))
# for i in menu:
    
if (n==1):
    m=(input('Enter your name '))
    acc=input('enter account number ')
    bal=('enter initial balance ')
    
    a=['name','account_no','balance']
    d=[m,acc,bal]
    # b=list("Enter name , account number and initial balance ")
    details=zip(d,a)
    print(details)
else:
    print("invalid input : ")
