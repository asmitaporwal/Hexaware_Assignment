import sys
sys.path.append('D:\\Hexaware_Assignment\\CaseStudy\\Python\\CaseStudy\\')
from Util.DBconn import DBConnection
class Cart(DBConnection):
    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

       