# F_string : Fast string
import math
me="Ashish"
a1 =3
a ="This is %s%s"%(me, a1)
print(a)
a = "this is {0} {1}"
b = a.format(me,a1)
print(b)
#-------Using F String
a =f"this is {me},{a1},{math.cos(20)}"
print(a)