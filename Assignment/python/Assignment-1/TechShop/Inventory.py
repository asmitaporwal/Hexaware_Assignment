class Inventory:
    def __init__(self,inventory_id,product,quantity_in_stock,last_stock_update):
        self.InventoryID=inventory_id
        self.Product=product
        self.QuantityInStock=quantity_in_stock
        self.LastStockUpdate=last_stock_update

    def GetProduct(self):
        pass
    
    def GetQuantityInStock(self):
        return self.QuantityInStock
    
    def AddToInventory(self, quantity):
        self.QuantityInStock += quantity
    
    def RemoveFromInventory(self, quantity):
        pass
     
    
    def UpdateStockQuantity(self, new_quantity):
        self.QuantityInStock = new_quantity
    
    def IsProductAvailable(self, quantity_to_check):
        if quantity_to_check <= self.QuantityInStock:
            print("Available")
        else:
            print("Not available")    
    
    def GetInventoryValue(self):
        pass
    
    def ListLowStockProducts(self, threshold):
      pass
    
    def ListOutOfStockProducts(self):
       pass
    
    def ListAllProducts(self):
       pass
