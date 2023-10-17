#Syntax for if and else conditions in python
var1 = 99
a = int(input())
if var1 > a:
    print("Greater")
elif var1==a:
    print("Equal")
else:
    print("Lesser")
#key words in if and else condition
# in keyword
l= [1,2,3,4,5]
print(2 in l)
if 2 in l:
    print("Yes it is in the list")
# not in : key word
print(2 not in l)
if 2 not in l:
    print("Yes it is not in the list")