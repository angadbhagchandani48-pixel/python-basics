# Dictionary methods
# first printing keys
employee = {
    "name":"rinku",
    "age":18,
    "profession":"employee",
    "salary": 50000,
} 
print(employee.keys())
# printing values
print(employee.values())
print (list(employee))
print (type(employee))
# changing a type of dictionary to list
employ = str(employee)
print (type(employ))
print (str(employee))
# printing length of dictionary
print (len(employee))
#dict.items()method this will return all key and values as tupule
print (employee.items())
#using slicing and indexing in dictionary
prince = (list(employee))
print (prince[0:4])
#using get method to get value of key
print(employee.get("name")) # agr ye method me 
print (employee["name"]) #agr is name me mene 2 lga diya "name2" to ye error dega
print(employee.get("name2")) #agr is name me mene 2 lga diya "name2" to ye none dega
#dict.update() method is used to update the value of key
employee.update({"hobby":"coding",
                 "city":"Delhi",})
print (employee)
#2nd method of update is
my_employee = {"car":"bmw",
               "wife name ":"priya",}
employee.update(my_employee)
print (employee)