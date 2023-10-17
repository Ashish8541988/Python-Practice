li =[ i for i in range (100) if i%5==0]
print(li)
dic1={ i: f"item:{i}" for i in range (5)}
print(dic1)
dic2={ value:key for key,value in dic1.items()}
print(dic2)
dress={ deress for deress in [ "dress1","dress1","dress2","dress2"]}
print(dress) # class set
evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

for item in evens:
    print(item)