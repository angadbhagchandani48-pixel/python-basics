# sets.add(element)will add the element to the set
storage = {"laptop","mobile",}
storage.add("tablet")
print(storage)
print(type(storage))
#sets.remove(element) remove the element from set
storage.remove("laptop")
print(storage)
#we can pass tuple , string , float , int in sets but we cannot pass list and dictionary in sets
storage.add((1,2,3,8,4))#adding tuple in sets but it adds only one element in sets
storage.add("hitesh")#str
storage.add(3.14)#float
storage.add(18)#int
print(storage)
#sets.clear() will clear the set
# # storage.clear()#it will remove whole set we can't choose
# print(storage)
#set.pop() will remove random element from set
print (storage.pop())
print(storage.pop())
#sets.union() will combine two sets and return a new set
collector = {"judge","lawyer","doctor",}
print(storage.union(collector))
print(storage.intersection(collector))#it will return common element in both sets
print(storage.difference(collector))#it will return element which is only in storage set not in collector set
print(collector.difference(storage))