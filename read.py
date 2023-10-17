# Reading Opertion with Input and Output stream
f=open("Ashish.txt")
content = f.read()
print(content)

f.close()
# to read 3 Character
f=open("Ashish.txt")
content = f.read(3)
print(content)

f.close()
#Print line by line
f=open("Ashish.txt","rt")
#content = f.read()
for line in f:
    print(line,end="")

f.close()
#-------------Read line function--------------
f=open("Ashish.txt","rt")
# content = f.read(3)
print(f.readline())
f.close()