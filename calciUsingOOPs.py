#Program for calculator using OOps
#BLL
class calci:
    def __init__(self):
        self.no1=0
        self.no2=0
        self.res=0
    def add(self):
        self.res=self.no1+self.no2
    def sub(self):
        self.res=self.no1-self.no2
    def mul(self):
        self.res=self.no1*self.no2
    def div(self):
        self.res=self.no1/self.no2
#PL
while(1):
    cal=calci()
    cal.no1=int(input("enter first number"""))
    cal.no2=int(input("enter second number"))
    ch=input("enter choice +,-,*,/")
    if(ch=="+"):
        cal.add()
        print("Result:", cal.res)
    elif(ch=="-"):
        cal.sub()
        print("result:", cal.res)
    elif (ch == "*"):
        cal.mul()
        print("result:", cal.res)
    elif (ch == "/"):
        cal.div()
        print("result:", cal.res)
    else:
        print("incorrect choice")
