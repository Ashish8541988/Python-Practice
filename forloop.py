# Syntax of For Loop
list1 = [["Ashish",1],["Roshan",23],["Aman",34],["Himanshu",45]]
for item,Marks in list1:
    print(item,"Marks is",Marks)
#------------print a number from a list which is greater than 6---------------
list2 = [34,56,23,5,"Ashish","Harry","Rohan"]
for item in list2:
    if str(item).isnumeric() and item> 6:
        print(item)
# Syntax For While Loop
i=0
while(i<13):
    print(i)
    i = i+1
# Syntax for break statment
j=0
while(True):
    print(j,end=" ")
    j=j+1
    if j==14:
        break
