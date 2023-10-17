def dec1(fun1):
    def execute():
        print("Executing now")
        fun1()
        print("Executed")
    return execute
# def fun2():
#     print("Ashish Arya")
# fun2=dec(fun2)
# fun2()
#----------Decorator in python--------------
@dec1
def fun2():
    print("Ashish Arya")
fun2()