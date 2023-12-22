class OrderDetails:
    def __init__(self,orderdetail_id,order,product,quantity):
        self.OderDetailId=orderdetail_id
        self.Order=order
        self.Product=product
        self.Quantity=quantity

    def CalculateSubtotal():
        pass
    
    def GetOrderDetailInfo(self):
        print("OrderDetailid: ",self.OderDetailId,end="\n")
        print("Order: ",self.Order,end="\n")
        print("Product: ",self.Product,emd="\n")
        print("Quantity: ",self.Quantity,end="\n") 
        
    def UpdateQuantity(self,new_quantity):
        self.Quantity=new_quantity 
        
    def AddDiscount(): 
        pass