import sys
sys.path.append('D:\\Hexaware_Assignment\\CaseStudy\\Python\\CaseStudy\\')
from Util.DBconn import DBConnection

class Customer(DBConnection):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def create_customer(self):
        try:
            self.open() 
            query = f"INSERT INTO customers (name, email, password) VALUES ('{self.name}', '{self.email}', '{self.password}')"
            self.c.execute(query)
            self.mydb.commit()
            customer_id = self.c.lastrowid
            print(f"\nCustomer '{self.name}' added to the database with ID: {customer_id}\n")
            return customer_id
        except Exception as e:
            print(e)
            return None
        finally:
            self.close()     