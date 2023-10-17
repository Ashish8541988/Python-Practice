list1=["Chips","Kurkura","Maza","Coce","Bear"]
i=1
for item in list1:
    if i%2 is not 0:
        print(f"Please buy the 1 {item}")
    i += 1
# with the help of enomrate function this problem can be done as:
for index, item in enumerate(list1):
    if index%2==0:
        print(f"Please buy the {item}")
