n=int(input("enter the number of lines"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*", end=" ")
    print()
