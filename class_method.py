class employ:
    change_leaves=8
    def __init__(self,name,salery,role):
        self.name = name
        self.salery=salery
        self.role=role

    def printdetails(self):
        return f"name :{self.name},salery : {self.salery}, role : {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):#-----it can we access anywhere-----------
        cls.change_leaves = newleaves
    

#----------------------Inheritance----------------------------------------------
class programmer(employ):
    def __init__(self, name, salery, role , language):
        self.name = name
        self.salery=salery
        self.role=role
        self.language = language

    def printd(self):
        return f"name :{self.name},salery : {self.salery}, role : {self.role},language : {self.language}"
    pass
Rohan=programmer("Roshan",588,"progrmmer",['python','C++'])
print(Rohan.printd())

Ashish=employ("Ashish",1200,"student")
a=Ashish.printdetails()
print(a)
print(type(a))