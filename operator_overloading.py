class A:
    def __init__(self,name,salery,role):
        self.name=name
        self.salery=salery
        self.role=role
    def printdetails(self):
        return f"Name : {self.name}, salery : {self.salery}, role : {self.role}"
    def __add__(self,other): # ----function define for operator overloading (also known as done done method )
        return f"Sum is : {self.salery + other.salery} "
    def __repr__(self):
        return f"employ ({self.name},{self.salery},{self.role})"
    def __str__(self):
        return f"Name : {self.name}, salery : {self.salery}, role : {self.role}"
    pass
emp1=A("Ashish",200,"teacher")
emp2=A("Roshan",300,"student")
print(emp1 + emp2)
print(emp1)
#-----Mapping operator to function (for searching special operator overloading function)