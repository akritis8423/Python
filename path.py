n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
if(n1>n2):
    if(n1>n3):
        print("n1 is greatest")
    else:
        print("n3 is greatest")
elif(n2>n3):
    print("n2 is greatest")
else:
    print("n3 is gratest among these three")