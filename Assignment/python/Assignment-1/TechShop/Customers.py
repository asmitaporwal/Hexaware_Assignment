class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.CustomerID = customer_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.Phone = phone
        self.Address = address
    @property
    def getter(self):
        return  self.CustomerID,self.FirstName, self.LastName, self.Email , self.Phone, self.Address
    
    @getter.setter
    def setter(self, customer_id, first_name, last_name, email, phone, address):
         self.CustomerID = customer_id,
         self.FirstName = first_name,
         self.LastName = last_name,
         self.Email = email,
         self.Phone = phone,
         self.Address = address

    def CalculateTotalOrders(self):
        pass
    
    def GetCustomerDetails(self):
        print("Customerid =",self.CustomerID,end="\n")
        print("Name =",self.FirstName+" "+self.LastName,end="\n")
        print("Email =",self.Email,end="\n")
        print("Phone =",self.Phone,end="\n")
        print("Address =",self.Address,end="\n")
        

    
    def UpdateCustomerInfo(self, new_email, new_phone, new_address):
        self.Email=new_email
        self.Address=new_address
        self.Phone=new_phone
        print("Updated customer info")  

 