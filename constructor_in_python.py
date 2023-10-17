class employ:
    def __init__(self,name,salery,role):
        self.name = name
        self.salery=salery
        self.role=role


    def printdetails(self):
        return f"name :{self.name},salery : {self.salery}, role : {self.role}"
    
Ashish=employ("Ashish",1200,"student")
a=Ashish.printdetails()
print(a)
print(type(a))