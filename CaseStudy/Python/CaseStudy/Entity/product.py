import sys
sys.path.append('D:\\Hexaware_Assignment\\CaseStudy\\Python\\CaseStudy\\')
from Util.DBconn import DBConnection
class Product(DBConnection):
    def __init__(self, name, price, description, stock_quantity):
        self.name = name
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def create_product(self):
        try:
            self.open() 
            query = f"INSERT INTO products (name, price,description,stockQuantity) VALUES ('{self.name}', '{self.price}','{self.description}', '{self.stock_quantity}')"
            self.c.execute(query)
            self.mydb.commit()
            product_id = self.c.lastrowid
            print(f"\nProduct '{self.name}' added to the database with ID: {product_id}\n")
            return product_id
        except Exception as e:
            print(e)
            return None
        finally:
            self.close()    