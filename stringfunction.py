poll= ("i am  devloper.")
print (poll.endswith("er.")) # the endswith() method checks if the string ends with the specified suffix and returns True or False accordingly.
dummy= "crazy=orld."
print (dummy.endswith("crazy.")) # it doesn't end with crazy.
#capitalize() method
pawn="i love it."
print (pawn.capitalize())#it capitalize my first letter of str.
print(pawn)# it doesn't change because it is original str.
#replace() method
str2= "i love coding language javascript."
print(str2.replace("javascript", "python"))# i replaced javascript with python.
print (str2) # it doesn't change because it is original str.
#find() method
str3= "i am a monstahhh"
print(str3.find("monstahhh"))# it exist in index 7
print (str3.find("crazy")) # it doesn't exist in the string so it will return -1    
#count() method
str4=("i am the god you must obey me fools.")
print(str4.count("o"))# it will count the word that how many times it exist in our string
name= input ("enter your name:")
print (name)
print (len(name))
print (name.upper()) # it will convert all the letters in uppercase

