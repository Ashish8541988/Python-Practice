def function1(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return function1(n-1)+function1(n-2)
n = int(input("Enter a no."))
a= function1(n)
print(a)