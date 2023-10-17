from pickle import TRUE
#-----this will start the while loop from that postion which he left or we can say that program start from that postion where we left the excution

def sercher():
    import time
    book="This is Ashish kumar from Uttarakhand"
    time.sleep(4)

    while TRUE:
        text=(yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Your text not found in the book")
search=sercher()
next(search)
search.send("gggg")
search.send("from")