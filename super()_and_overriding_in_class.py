class student:
    name="Preetam"
    def __init__(self):
        self.name="Roshan"
        self.roll=100
class teacher(student):
    def __init__(self):
        self.name="Ashish"
        self.marks=200
        super().__init__() #--overrite consructor 1st
A=student()
B=teacher()
print(B.name)
        