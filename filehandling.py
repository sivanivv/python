# FILE HANDLING

# f=open('file.txt','x')

#------------------------------------creating

#=================read======================================

# f=open('file.txt','r')
# for i in f:
#     print(i)

#-------------------------------------reading

#ex1

# f=open('file.txt','r')
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.close()

#------------------------------------line by line reading

# print(f.read())  

#------------------------------------read file fully

# with open ('file.txt') as f:
#     data=f.read()
# print(data)

#-------------------------------------another way 

# f=open('file.txt','r')
# print(f.read(7))

#-------------------------------------to print first 7 characters

# with open ('file.txt') as f:
#     data=f.readlines()
# for line in data:
#     word=line.split()
#     print(word)

#--------------------------------------split() 

#====================create==========================

# f=open('file.txt','w')
# f.write("I'm sivani\n")
# f.write("Nice to meet you")
# f.close()

#---------------------------------------------writing (can also use with)


# f=open('file.txt','a')
# f.write("\nHow are you?!")

# f.close()

#---------------------------------------------append (adds without changing the file)





