#LISTS

#append
# a=[11,0,3,45]
# print("Before append :",a)
# a.append(4)
# print("After append : ",a)


#insert
# i=['a','p','a','n','a']
# i.insert(3,'r')
# print("Inseted list",i)

#extend
# e=[9,8,9,5,4]
# b=[9,0,2,8,9]
# e.extend(b)
# print("Extended list: ",e)


#change list items
# c=['netflix','gpay','candycrush']
# c[2]='whatsapp'
# print('Changed list : ',c)



#Removing items

#using pop
# p=[1,1,19,44]
# removed_element=p.pop(1)
# print('Removed element',removed_element)
# print('Updated_list',p)

#using del
# d=['lilly','sunflower','rose','jasmine','lotus']
# del d[2] #index position 2
# del d[-1] #first from the last
# del d[0:2] betweem 0 and two
# print(d)


#using remove
# r=['sun','star','rainbow','flower','frog']
# r.remove("frog")
# print(r)


#Reversing list

# rev=['n','a','c']
# rev.reverse()
# print(rev)



#Operations

#1.Repeatation
# r=[1,1,4,0,4,2]
# l=r*2
# print(l)

#2.Concatenation
# c=[1,1,4,2,4,2]
# t=[5,6,3,7,4,7]
# l=c+t
# print(l)

#3.Length
# l=[11,4,2,3,2,2]
# length=len(l)
# print(length)
# print(len(l))   #other

#4.Iteration
# list=[1,1,4,0,4,1]
# for i in list:
#     print(i)

# list=['abin','meena','aiswarya','nila']
# for i in list:
#        print(i)

#5.Membership
# list=[11,53,41,54,15]
# print(15 in list)
# print(84 in list)


#6.Max & Min
# list=[11,55,4,1,54]
# print(max(list))
# print(min(list))


#Intersection (it will return in set) set is a datatype to avoid when there is dupicate

l1=[11,58,4,0,1]
l2=[1,15,84,0]
# intersection=set(l1).intersection(l2)
# print(intersection)                         # using intersection method


# intersection=set(l1)&set(l2)
# print(intersection)                         #using & operator
