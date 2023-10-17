# Set is a collection of well define objects it will retain a uniqe value
#Creation of a set it will support all properties related to sets in Mathematics
s= set()
print(type(s))
# Creation of a set with the help of list
s_from_list = set([1,2,3,4,])
print(s_from_list)
l = [12,23,34,33]
s=set(l)
print(s)

# How to add elements in a set
s.add(22)  
print(s)
s1=s.union({11,44,55})
print(s1)