# tupules iives error because tupules are immutable
# print (tup[0], tup[-1])s built in data type that is immutbale not changeable 
# tup = (94,34,44,84,48)
# print (tup)
# print (type(tup))
# # tup[0] = 33 # it g
# tup1 = ()#empty tupule it is a valid tupule
# print (tup1)
# tup2 = (1,)# to appoint a one element in tupule we have to put a comma after the element otherwise it will be considered as an int
# print (tup2)
# print (tup [1:4]) # slicing in tupules
# print (tup.count(34)) # it counts the number of times 34 is present in the tupule
# print (tup.index(34))
# movies = input ("ENTER YOUR FAVOURITE MOVIES :")
# list = movies.split(",")
# print (list)
# list1 = [1,2,3,2,1]
# if list1 == list1[::-1]: # it checks whether the list is palindrome or not
#     print ("palindrome")
# else:
    # print ("not a palindrome")
tup5=("C","D","E","A","B","C","D","E","A")
print(tup5.count ("A"))
list5 = [tup5]
print (list5)
list5[0] = sorted(list5[0])
print(list5)