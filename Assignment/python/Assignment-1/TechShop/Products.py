class Products:
    def __init__(self, product_id, product_name, description, price):
        self.ProductID = product_id
        self.ProductName = product_name
        self.Description = description
        self.Price = price
    
    def GetProductDetails(self):
       print("ProductId: ",self.ProductID)
       print("ProductName: ",self.ProductName)
       print("Description: ",self.Description)
       print("Price: ",self.Price)
    
    def UpdateProductInfo(self, new_price, new_description):
        self.Price=new_price
        self.Description=new_description
        print("Product updated")
    
    def IsProductInStock(self):
        pass
      