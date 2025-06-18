#TUPLES

#creating tuble

# tuple_data=(0,1,2,3,4)
# print(tuple_data)


#empty tuple
# my_tuple=()
# print(my_tuple)


#nested tuple
# my_tuple=("mouse",[3,5,7],(4,5,7))
# print(my_tuple)


#indexing
# letters=('a','b','i','n','r','a','j')
# print(letters[0])
# print(letters[4])
# print(letters[-2]) #negative indexing
# print(letters[-3]) #negative indexing


#repetition tuples
# tuple_n=("Python","Tuples")
# print("Oringinal Tuple is : ",tuple_n)
# tuple_n=tuple_n*3
# print("New Tuple is : ",tuple_n)



#tuple methods
# my_tuple=('d','i','a','r','y','y')
# print(my_tuple.count('a'))
# print(my_tuple.count('y'))


#iterating through tuple
# languages=("python","swift",'c++')
# for languages in languages:
#     print(languages)


#check if an item exists in tuple
# languages=("python","swift",'c++')
# print('c' in languages)
# print('python' in languages)


  


#SETS

#set() keyword method
# Days=set(["Tuesday","Wednesday","Thursday","Friday"])
# print(Days)
# print(type(Days))
# for i in Days:
#     print(i)



#adding items to set

#1. Using add() method
# months=set(['april','may','june','july','august','september'])
# print(months)
# months.add('october')
# print(months)

#2. Using update() method
# months=set(['april','may','june','july','august','september'])
# print(months)
# months.update(["november","december"])
# print(months)



#adding items to set

#1. Using discard() method
# months=set(['april','may','june','july','august','september'])
# months.discard("april")
# print(months)


#2. Using remove() method
# months=set(['april','may','june','july','august','september'])
# months.remove("april")
# print(months)


#set operations

#1.union of 2 sets
# days1={'tuesday','wednesday','thursday','friday'}
# days2={'saturday','sunday','monday'}
# print(days1|days2)

#2.intersection of 2 sets
# days1={'tuesday','wednesday','thursday','friday'}
# days2={'saturday','sunday','monday','tuesday'}
# print(days1&days2)




#set comparison
days1={'wednesday','thursday','friday','saturday'}
days2={'saturday','thursday'}
days3={"wendesday",'thursday','sunday'}

print(days1>days2) #days1 is superset of days2
print(days1<days2) #days2 is not superset of days1
print(days2==days3) #days2 and days3 is not equal


