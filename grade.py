m1=int(input("enter marks of subject1"))
m2=int(input("enter marks of subject2"))
m3=int(input("enter marks of subject3"))
sum=m1+m2+m3
g=sum/3
if(g<25):
    print("Grade is F")
elif(25>=g and g<45):
    print("Grade is E")
elif(45>=g and g<50):
    print("grade is D")
elif(50>=g and g<60):
    print("Grade is C")
elif(60>=g and g<80):
    print("Grade is B")
else:
    print("Grade is A")
