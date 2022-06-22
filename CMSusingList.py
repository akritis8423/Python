#BLL
idlist=[]
agelist=[]
namelist=[]
def addCust(id,age,name):
    if(id in idlist):
        return 0
    else:
        idlist.append(id)
        agelist.append(age)
        namelist.append(name)
        return 1
def searchCust(id):
    if(id in idlist):
        i=idlist.index(id)
        return i
    else:
        return -1

#PL
def showCustomer(i):
    print("Cust ID:",idlist[i],"Cust Age:",agelist[i],"Cust Name:",namelist[i])
print("Welcome to Deepak's CMS")
while(1):
    print("1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    print("5 for Display All Cust, 6 for Exit")
    ch=input("Enter Choice 1 to 6: ")
    if(ch=="1"): #Add Customer
        id=input("Enter Cust ID:")
        age=input("Enter Cust Age:")
        name=input("Enter Cust Name:")
        flag=addCust(id,age,name)
        if(flag==0):
            print("Duplicate ID")
        else:
            print("Cust Added Successfully")
    elif(ch=="2"): #Search Customer
        id = input("Enter Cust ID:")
        i=searchCust(id)
        if(i==-1):
            print("Id not found")
        else:
            showCustomer(i)
    elif (ch == "5"):  # Display All Customer
        for i in range(len(idlist)):
            showCustomer(i)

