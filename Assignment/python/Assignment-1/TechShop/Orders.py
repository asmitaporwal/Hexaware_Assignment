from datetime import datetime
class Orders:
    def __init__(self, order_id, customer,orderDate,Totalamount):
        self.OrderID = order_id
        self.Customer = customer
        self.OrderDate = orderDate
        self.TotalAmount = Totalamount
    
    def CalculateTotalAmount(self):
        return self.TotalAmount
    
    def GetOrderDetails(self):
        print("Orderid =",self.OrderID,end="\n")
        print("OrderDate =",self.OrderDate,end="\n")
        print("TotalAmount =",self.TotalAmount,end="\n")
    
    def UpdateOrderStatus(self, new_orderdate,new_amount):
        self.OrderDate=new_orderdate
        self.TotalAmount=new_amount
        print("order updated")
    
    def CancelOrder(self):
        pass
