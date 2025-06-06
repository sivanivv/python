# print('1) Create new account \n','2) Deposit money \n','3) Withdraw money\n','4) Display account details \n ','5) Exit \n',)

data={}
option=()
while option!=5:
    print('1) Create new account\n','2) Deposit money\n','3) Withdraw money\n','4) Display account details\n ','5) Exit\n',)

    option=int(input("What is your need? enter your option : "))
    if (option==1):
        details={}
        name=str(input('Enter your name : '))
        details['name']=name

        acc=int(input('Enter your account number : '))
        
        while  acc< 0 or acc in data :
           
              print("Enter valid account number!!")
              acc=int(input('Enter your account number '))
           
        else:
            details['account_no']=acc

    
        bal=int(input('Enter initial balance : '))
        while bal<0:
            print("Enter valid  amount!!")
            bal=int(input('Enter initial balance : '))
        else:
            details['balance']=bal

        data[acc]=details
        print("Account created successfully!!!",details)


    elif option == 2:
        acc = int(input('Enter account number: '))
        if acc in data:
            deposit = int(input("How much money do you want to deposit? :  "))
            data[acc]['balance']+=deposit
            
        else:
            print("Account number not found !! Try again.")
        print("Your current balance : ",data[acc]['balance'])


    elif option==3: 
        acc = int(input('Enter account number: '))
        if acc in data :
            wthd = int(input("How much money do you want to withdraw? : "))
            
            if data[acc]['balance'] > wthd:
                data[acc]['balance']-=wthd
            else:
                print("Enter valid amount !! Try again")

        else:
            print("Account number not found !! Try again.")
        print("Your current balance : ",data[acc]['balance'])


    elif option==4:
       acc = int(input('Enter account number : '))
       if acc in data:
           print("your account details: ",data[acc])
    
    elif option==5:
        print("EXITED!!")
    

    else:
        print("INVALID OPTION!! TRY AGAIN")
        
          



    # elif option==7:
    #    print(data) 
    
    # print("invalid input : ")











