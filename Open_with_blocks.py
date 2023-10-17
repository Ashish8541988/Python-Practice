with open("Ashish.txt") as f: #----------it will automatically handle the open and close statements
    a = f.readlines()
    print(a)
f=open("Ashish.txt")
print(f.readline())
f.close()