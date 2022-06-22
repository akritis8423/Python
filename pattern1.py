n=int(input("enter no of lines"))
for i in range(n):
    if i%2==0:
        for j in range(i*2+1):
            print("*", end=" ")
            break
    else:
         for k in range(i*2+2):
             print("@", end=" ")
    print()
