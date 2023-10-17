#Built in function Sum and other
a=12
b=5
c=sum((a,b))
print(c)
#----------User define function-------------
def ashish(c,d):
    e = c%d
    print(e)
ashish(25,5)
#---------------Doc string-------------------
def averagw(c,d):
    """This function will give average of two no."""
    print((c+d)/2)
averagw(6,12)
print(averagw.__doc__)