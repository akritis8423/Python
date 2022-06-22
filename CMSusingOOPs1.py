#BLL
class customer:
    cuslist=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        customer.cuslist.append(self)
        print("Customer Added Successfully")
    def searchCustomer(self):
        for e in customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return

    def modifyCustomer(self):

        for e in customer.cuslist:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                return
        print("Customer Modified Successfuly")
    def deletCustomer(self):
        customer.cuslist.remove(self)
        for e in customer.cuslist:
            if(e.id==self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                return
        print("Customer deleted successfully")







#PL
def showCustomer(c):
    print("Customer ID:",c.id,"Customer Name:",c.name,"Customer Age:",c.age,"Customer Mob:",c.mob)
while(1):
    choice=input("""1 for Add Customer, 2 for Search Customer"
3 for Modify, 4 for delete customer, 5 for Display all Customer,
0 for exist""")
    if(choice=="1"):
        cus=customer()
        cus.id=input("enter customer ID")
        cus.name = input("enter customer name")
        cus.age= input("enter customer age")
        cus.mob= input("enter customer mob")
        cus.addCustomer()
    elif(choice=="2"):
        cus=customer()
        cus.id=input("enter customer ID")
        cus.showCustomer()


    elif(choice=="3"):
        cus=customer()
        cus.id = input("enter customer ID")
        cus.name = input("enter customer updated name")
        cus.age = input("enter customer updated age")
        cus.mob = input("enter customer updated mob")
        cus.modifyCustomer()

    elif(choice=="4"):
        cus=customer()
        cus.id=input("enter the customer id")
        customer.deletCustomer()

    elif(choice=="5"):

        for e in customer.cuslist:
            showCustomer(e)



    elif(choice=="0"):
        break





