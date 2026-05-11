# Dictionaries
dict = {
    "name":"Rohit",
    "age": 18,
    "gender":"male",
    "class":12,
    13.44 : 34,
    "name" : "no name"
}
print (dict)
print(type(dict))
print(len(dict))
lis = list(dict)
print (lis)
print(type(lis))
print (dict["name"],(dict[13.44]))
# changing a value in dictionary
dict ["name"] = "Virat" # This replaces the value in key
print (dict)
#adding  one more key value pair ind dictionary
dict ["surname"] = "KOHLI"
print (dict)
# we can also print an empty dictionary
empty_dict={}
print (empty_dict)
print (dict["name"])# this will print only first key "name "
# we can also print all the keys in dictionary
print (dict.keys())
# nesting in dictionary
student = {
    "name" : "Bhavya",
    "age":15,
    "marks":{
        "maths":97,
        "phy":90,
        "chem":99,
        "eng":89,
        "physical education":100,
    }
}
print (student)
print(student["marks"])
print (student.keys())
print(student["marks"]['maths'])#this will print the value of key "maths" in marks dictionary