class grandfather:
    var=3
    dance = "Garwali"
def printdetails(self):
    return f"Yes I can dance in :{self.Garwali}"
class dad(grandfather):
    var=44
    play = "football"
    def printdetails(self):
        return f"Yes I can dance in :{grandfather.dance},I also can play:{self.play}"
class son(dad):
    drive="Car"
    def printdetails(self):
        return f"Yes I can dance in :{grandfather.dance},I also can play:{self.play},I also can drive a:{self.drive}"
Ashish=son()
print(Ashish.printdetails())
print(Ashish.var) #--order of acessing a variable is down to top apporach----