# For protected member a it should start with (_)
# For private member it should be start with (__)
from unicodedata import name


class student:
    __game=8
    _fun=9
    def __init__(self,name,roll,_Marks,__sex):
        self.name=name
        self._Marks= _Marks # protected member 
        self.sex= __sex # private member
        pass
Ashish=student("Ashish",200,12,"Male")
print(Ashish._student__game) # To acess a private member syntax shoud be object_class__variable name This method is known as name angling
