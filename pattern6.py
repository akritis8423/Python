n=int(input("enter tne no of lines"))
for i in range(n):
    for j in range(n-i):
        print("* ",end="")
    for k in range((2*i)+0):
        print("  ",end="")
    for l in range(n-i):
       print("* ",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    for k in range(2*(n-i-1)):
        print("  ",end="")
    for l in range(i+1):
        print("* ",end="")
    print()
