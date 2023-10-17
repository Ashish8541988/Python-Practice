class student:
    var = 4
    def __init__(self,name,standard,roll_no):
        self.name=name
        self.standard=standard
        self.roll_no=roll_no

    def printdetail(self):
        return f"name:{self.name},standard:{self.standard},roll_no : {self.roll_no}"
    pass


class teacher:
    var =90
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id
    
    def printt(self):
        return f"name: {self.name},subject: {self.subject},id : {self.id}"


class principal(student,teacher): #----Constuctor should we used only 1st inhertated class-----
    pass

Ashish =student("Ashish",12,200117)
print(Ashish.printdetail())
Roshan=teacher("Roshan","Math",200116)
print(Roshan.printt())
Riyansh=principal("Riyansh",2,200117)
print(Riyansh.printdetail())
print(Riyansh.var)
#--acessed order 1st inherted class then next for a simllar variable name or function name--