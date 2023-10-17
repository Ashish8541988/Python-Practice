#Dictnoary : It is a key value pair
# Dictnoary creation
d1 = {}
print(type(d1))

#Dictnoary with element
d2 = {"Ashish":"Piza" , "Rohit":"Egg" , "Mohit":"Fish"}
print(d2)
print(d2["Ashish"]) # the out put is pizza
# Dictonary Value can contain a dictonary, list, tapple
d3 = {"Ashish":"Pizza" , "Rohit":"Egg" , "Mohit":"Fish" , "Aman":{"B":"Maggi" , "L":"Rice" , "D": "Roti"}}
print(d3)
#how to access the members of a Dictonary
print(d3["Aman"])
print(d3["Aman"]["B"])

# How to update a dictonary
d2["Ankit"] = "Carrot" # Add a new key
print(d2)
del d2["Mohit"] #delete a key
print(d2)

#---------------------Functions in dictonary---------------------------
d3=d2
print(d3)
#del d3["Ashish"]
print(d2) #it will delete the Ashish from both dictonary

# Copy Function
d3=d2.copy()
del d3["Rohit"]
print( "key of d2 is",d2) # it will not delete the key of d2
# get Function
print(d2.get("Ashish")) #it will show the key value

# update Function : It will add a new key to the dictonary or it will update the list
d2.update({"Leena":"toffe"})
print(d2)
d2.update({"Ashish":"Shirt"})
print(d2)
 