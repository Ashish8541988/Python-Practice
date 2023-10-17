def function1(n):
    if n==1:
        return 1
    else:
        return n*function1(n-1)
n=int(input("Enter a no."))
factorial = function1(n)
print("the factorial of the no. is = ",factorial)