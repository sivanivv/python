# _________________EXCEPTION HANDLING_____________________


# t=5
# i='lly'
# z=t+i
#_______________________________________________________type error exception

# t=5
# i='lly'
# try:
#     z=t+i
# except TypeError:
#     print("ERROR: cannot add an int and a string")

#_______________________________________________________handling(try except)

# n=[11,2,3]
# try:
#     print("Second element: ",n[1])
#     print("Fourth element: ",n[3])
# except:
#     print("An error occurred")


# n=[11,2,3]
# try:
#     print("Second element: ",n[1])
#     print("Fourth element: ",n[3])
# except Exception as e:                #exception into a variable
#     print(e)

#______________________________________________________________with variable


# try:
#     raise NameError("Hi there")
# except NameError:
#     print("An exception")
#     raise

#_______________________________________________________________error raising