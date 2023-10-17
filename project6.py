list1 = [1,2,3,4,5]
a=int(input("Enter a no."))
if a in list1:
   for i in range(0,a):
    for i in range(0,i+1):
        print("*",end=" ")
    print("")
else:
    for i in range(0,a):
        for i in range(0,a-i):
             print("*",end=" ")
        print("")

