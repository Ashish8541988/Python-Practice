#---------------tell function tell us file pointer location-------------
f=open("Ashish.txt")
print(f.readline())
print(f.tell())#--------it give us 25 because it tell that their are 25 Character in the first line---------
#---------------seek() function give the file pointer to starting value--------
f.seek(13)
print(f.readline())