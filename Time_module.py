import time
intial = time.time()
k=0
while(k<5):
    print("Ashish")
    k=k+1
    time.sleep(5) # example of time.sleep function
print("while loop take",time.time()-intial,"sec")
intial2 = time.time()
for i in range (5):
    print("Ashish")
print("for loop taks",time.time()-intial2,"sec")

#---------for local time--------------
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
#-----------time.sleep function provide dealy in the program------------