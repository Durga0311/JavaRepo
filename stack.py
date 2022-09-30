import sys
from array import *
a=array("i",[])
while True:
    print("1.PUSH 2.POP 3.DISPLAY 4.EXIT")
    ch=int(input("enter your choice:"))
    if ch==1:
        for i in range(10):
            a.append(i)
        print("inserted",a)
    elif ch==2:
        if len(a)==0:
            print("stack is full")
        else:
            print("removed element",a.pop())
    elif ch==3:
        if len(a)==0:
            print("stack is full")
        else:
            for i in range(10):
                print(i)
    elif ch==4:
        sys.exit()
    else:
        print("invalid choice")
    