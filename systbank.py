print('a) Create new account \n','b) Deposit money \n','c) Withdraw money\n','d) Display account details \n ','e) Exit \n',)

option=int(input("What is your need? enter option : "))
data={}

while option!=exit:
    option=int(input("What is your need? enter option : "))
    if (option==1):
    
        name=(input('Enter your name '))
        acc=int(input('enter account number '))
    
        bal=int(input('enter initial balance '))
        details={'name':'','account_no': '','balance':''}
        
        
        details['name']=name

        if acc not in details and acc> 0:
            details['account_no']=acc
        # if acc> 0:
            # details['account_no']=acc

        if bal>0:
            details['balance']=bal

        for i in acc:
           
           data[i]=details

        print(details)
    # print(data)
    elif option==2:
       deposit=int(input("How much money do you want to deposit? "))
       if deposit>0:
          bal+=deposit
          details['balance']=bal
        #   print(details)
    elif option==3: 
       wd=int(input("How much money do you want to withdraw? "))
       if wd>0 :
          bal-=wd
          details['balance']=bal
        #   print(details)
    elif option==4:
       print(details) 
    elif option==7:
       print(data) 
    
    # print("invalid input : ")
