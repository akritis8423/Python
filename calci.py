#BLL
import math
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

#PL
n1=float(input("enter first number"))
n2=float(input("enter second number"))
ch=input("enter your choice +,-,*,/,pow,log")
if(ch=="+"):
    r=add(n1,n2)
elif(ch=="-"):
    r=sub(n1,n2)
elif(ch=="*"):
    r=mul(n1,n2)
elif(ch=="/"):
    r=div(n1,n2)
elif(ch=="pow"):
    r=math.pow(n1,n2)
elif(ch=="log"):
    r=math.log(n1,n2)
else:
    print("incorrect choice")
print("Result:", r)
