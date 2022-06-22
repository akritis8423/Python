str=input("enter any character")
temp=""
rev=""
for i in str:
    if i!=" ":
        temp=i+temp
    else:
        rev=rev+temp
        temp=""
print(rev)