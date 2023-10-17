l = 5
def function1():
    global l #-----How to Change a global variable inside a function
    l=l+6
    m=9
    print(l,m)
   
function1()
print(l)