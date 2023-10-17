from ast import operator


print("Enter First number")
a = int(input())
print("Enter the Operator")
oper = (input())
print("Enter the second number")
c = int(input())
if a==45 and c==34 and oper == '+':
     print(443)
elif a==46 and c==3 and oper == '-':
     print(47)
elif a==40 and c==3 and oper == '*':
     print(44)     
elif oper == '+':
     print(a+c)
elif oper== '-':
     print(a-c)
elif oper == '*':
     print(a*c)
elif oper == '/':
    print(a/c)
else:
     print ("Enter valid operator")