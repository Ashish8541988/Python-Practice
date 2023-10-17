from abc import ABC, abstractmethod #-- This modual is used when we need a function in every class it will tell the class that you have not create a function which is essiential for it. Which is define in super class abstract.
class shape(ABC):
    @abstractmethod
    def printarea():#--here printarea function is must to be define in that class which inheriate the shape class
        return 0
class ractangle(shape):
    def __init__(self):
        self.l=4
        self.b=8
    def printarea(self):
        return self.l *self.b
    
Ab=ractangle()
print(Ab.printarea())
#---we can't make a object for abstract base class