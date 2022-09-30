import sys
from array import *
a=array("i",[])
def enqueue():
    for i in range(5):
        a.append(i)
    print("inserted",a)
def dequeue():
    if len(a)==0:
        print("is full")
    else:
        print("removed element is:",a.pop(0))
def show():
    if len(a)==0:
        print("is full")
    else:
        for i in range(5):
            print(i)
while True:
    print("1.ADD 2.REMOVE 3.SHOW 4.QUIT")
    ch=int(input("enter your choice:"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("invalid choice")
        
        