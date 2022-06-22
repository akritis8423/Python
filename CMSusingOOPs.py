#new program to make CMS using OOPs
#BLL
class Customer:
    cuslist=[]
    #instance variable
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        Customer.cuslist.append(self)
        print("Customer Added Sucessfully")

    def searchCustomer(self):
        for e in Customer.cuslist:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return
    @staticmethod
    def deleteCustomer(id):
        for e in Customer.cuslist:
            if(e.id==id):
                Customer.cuslist.remove(e)
                return
        print("Customer deleted successfully")
    def modifyCustomer(self):
        for e in Customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return
        print("Customer Updaed Successfully")


#PL
def showCustomer(cus):
    print("CusID:",cus.id,"CusAge:",cus.age,"CusName:",cus.name,"CusMob:",cus.mob)

print("Welcome to CMS")
while(1):

    choice=input("""1 for add customer,2 for search customer,
3 for delete, 4 for modify, 5 for display all,0 for exist""")
    if (choice=="1"):
        cus=Customer()

        cus.id=input("enter cus ID")
        cus.name= input("enter cus name")
        cus.age= input("enter cus age")
        cus.mob= input("enter cus mob")
        cus.addCustomer()
    elif(choice=="2"):
        cus=Customer()
        cus.id=input("enter cus ID")
        cus.searchCustomer()
        showCustomer(cus)
    elif(choice=="3"):
        id=input("customer id")
        Customer.deleteCustomer(id)
    elif(choice=="4"):
        cus =Customer()
        cus.id = input("enter cus ID")
        cus.name = input("enter cus updated name")
        cus.age = input("enter cus updated age")
        cus.mob = input("enter cus updated mob")
        cus.modifyCustomer()
    elif(choice=="5"):
        for e in Customer.cuslist:
            showCustomer(e)
    elif(choice=="0"):
        break




