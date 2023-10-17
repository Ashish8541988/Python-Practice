import random
import kivy
list1 = ['snake','water','gun']
i=0
c=0
u=0
while(i<10):
    a = random.choice(list1)
    b=input("Enter a Choice\n")
    if(a=='snake'and b=='water'):
        c=c+1
        print("You lost the match")
    elif(a=='snake'and b=='gun'):
        u=u+1
        print("You won the match")
    elif(a=="water"and b=="snake"):
        u=u+1
        print("You won the match")
    elif(a=='water'and b=='gun'):
        c=c+1
        print("You lost the match")
    elif(a=='gun'and b=='snake'):
        c=c+1
        print("You lost the match")
    elif(a=='gun'and b=='water'):
        u=u+1
        print("You won the match")
    elif(a=='water'and b=='water'):
        print("Drow!")
    elif(a=='snake'and b=='snake'):
        print("Drow!")
    elif(a=='gun'and b=='gun'):
        print("Drow!")
    else:
        print("You Enter the wrong choice")
    print("Enter your choice again")
    i=i+1
if(c<u):
     print("Finally you won the match and your score is :",u)
elif(c>u):
    print("You lost the match and your score is :",u)
else:
    print("Match drow! Play again! :",u)