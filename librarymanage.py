pas = {'username':'user','password':'ppp'}
print(" 1. Admin ","\n","2. User")
option=int(input("Enter your option : "))

if option==1:
    print("LOGIN")
    userA=input("Enetr Username: ")
    passwA=input("Enetr Password: ")
    if userA==pas['username'] and passwA==pas['password']:
        print("Welocome Admin !")
    else: 
        print("INCORRECT PASSWORD OR USER NAME ! try again ..") 
    print(' 1. Add book\n','2. Update book\n','3. Delete book\n','4. Display all books\n','5. Exit')
    op=int(input("Enter your option: "))
    # if op==1:





