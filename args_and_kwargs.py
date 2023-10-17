def function1(key, *args,**kwargs):
    print(type(args)) # list is convert into a tupple when pass to a function
    print(key)
    for item in list1:
        print(item)
    # for key,value in kwargs.items():
    print(kwargs.get("Ashish"))
list1=["Ashish","Nitesh","Preetam,"]
normal = "This is bother list"
kwargs={"Ashish":"CIO","Abhi":"Manger"}
function1(normal,*list1,**kwargs)

#------------------Order of passing argument is: normal,args,kwargs----------------------