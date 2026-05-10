# lists are a set of functions that is used to store elements of different ypes like strings, int ,float.etc.
marks = [39.1,99.3,34.3,39.3]
print (marks)
print (type(marks))
print (len(marks))
print (marks[0:5]) #SLICING ACCESING SOME PART  OF THE LIST
student = ["Angad","age",15,"marks",100]
print (student)
hitesh = ["hitesh",15,"dwarkapuri"]
hitesh [0] = "TANNI" # lists are mutable it replaces tanni from hitesh
print (hitesh)
list1 = [3,2,1,4,5]
list1.append(6)#it adds 6 at the end of the list
print (list1)
list1.sort()#it sorts the list in ascending order
print (list1)
list1.sort(reverse=True) # it sorts the list in descending order
print (list1)
list1.reverse() # it reverses the list
list1.insert (2,10) # it adds 10 at index 2
print (list1)
list1.remove(10)# it removes 10 from the list
print (list1)
list1.pop(5) # it removes the element at index 6
print (list1)
