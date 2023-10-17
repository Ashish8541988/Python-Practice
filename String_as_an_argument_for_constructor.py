class employ:
    change_leaves=8
    def __init__(self,name,salery,role):
        self.name = name
        self.salery=salery
        self.role=role

    def printdetails(self):
        return f"name :{self.name},salery : {self.salery}, role : {self.role}"
#     @classmethod
#     def change_leaves(cls,newleaves):#-----it can we access anywhere-----------
#         cls.change_leaves = newleaves
    
# Ashish=employ("Ashish",1200,"student")
# a=Ashish.printdetails()
# print(a)
# print(type(a))
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
Rohan=employ.from_str("Rohan-456-Chairman")
print(Rohan.salery)
#class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# karan = Employee.from_dash("Karan-480-Student")

# Employee.printgood("Rohan")


# Previous
# Next

# CodeWithHarry
# Copyright © 2022 CodeWithHarry.com

