#Slacing
import numbers
from re import A
from tkinter import N


d = "ashish Arya from kafanaul"
#number of string print and gap between the print gap 
print(d[0:5:3])
print(d[0:5:2])
print(d[0:5:1])
#To find the length of the string
print(len(d))
#To print in reverse order
print(d[-4:-1])
#Functions in string
print(d.isalnum()) #it check the spacing btween the string if it is than it is false
print(d.isalpha()) #it also check  the spacing btween the string if it is than it is false
print(d.endswith("kafanaul")) # it check the last word of the string
print(d.count("a")) #it count the latter accuring in the program
print(d.capitalize()) # it capitalize the first latter of the string
print(d.find("from")) # To find the the string starting index no.
print(d.lower()) # lower case to whole string
print(d.replace("from","for")) # Replace the word

#---------------------List--------------------

tank=["mobile","cable","mouse","pan","card",54]
print(tank)
print(tank[3]) # To print the 3rd element of list
numbers=[44,56,32,57,21,58,12]
numbers.sort()
numbers.reverse()
print(numbers)

#-------------------Append--------------------

tank.append("ashish") # this will add the items to the end of a list
print(tank)
 
numbers.append(98)

#-------------------insert Function--------------------

tank.insert(2,45) # It will add a new no. or items to the givin index locations
print(tank)
 
numbers.insert(2,5)
print(numbers)

#-------------------remove Function--------------------
numbers.remove(32)
print(numbers) # It will remove the desire no. from the list

#-------------------pop Function--------------------
numbers.pop()
print(numbers) # It will remove the last item from the list


#------------------- Function--------------------
#function are two types: Mutable : can be change like list
#immutable : can't change the value or items of that like tapple

#-------------------------Tapple------------------
tp=(12,23,45)
print(tp)

#------------------swaping of two no.---------------
a=45
b=23
a,b=b,a
print(a,b)