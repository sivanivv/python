pas = {'username':'admin','password':'ppp'}
print(" 1. Admin ","\n","2. User")
option=int(input("Enter your option : "))
data={}
if option==1:
    print("LOGIN")
    userA=input("Enetr Username: ")
    passwA=input("Enetr Password: ")
    if userA==pas['username'] and passwA==pas['password']:
        print("Welocome Admin !")
    else: 
        print("INCORRECT PASSWORD OR USER NAME ! try again ..") 
    print(' 1. Add book\n','2. Update book\n','3. Delete book\n','4. Display all books\n','5. Exit')
    op=()

    while op!=5:
        op=int(input("Enter your option: "))
        if op==1: #----------------------------------------------------------ADD BOOK
            lib={}
            print("Add Book ")


            book_id=int(input("Enter book id: "))

            while book_id<0 and book_id in data:
                print("Enter valid number!!")
                acc=int(input('Enter book id: '))
            else:
                lib['Book id ']=book_id



            title=(input("Enter title: "))

            if title in data[book_id]['title']:
                lib['Title']=title
            author=input("Enter Author name: ")
            lib['Author']=author
            quan=(input("Enter quantity: "))
            lib['Quantity']=quan
            data[book_id]=lib

            print(lib)
            print(data)








