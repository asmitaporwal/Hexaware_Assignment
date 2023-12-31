import sys
sys.path.append('D:\\CaseStudy\\')
import unittest
from Entity.product import Product
from Dao.Service import serviceprovider
from MyException.exception import CustomerNotFoundException,ProductNotFoundException,OrderNotFoundException


class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.ecommerce = serviceprovider()

  

    def test_add_to_cart(self):
       
        customer_id = 2  
        product_id = 4  
        quantity = 1
        added_to_cart = self.ecommerce.addToCart(customer_id, product_id, quantity)
        self.assertTrue(added_to_cart)
        

    def test_place_order(self):
        
        customer_id = 2
        shipping_address = "gwalior"
        placed_order = self.ecommerce.placeOrder(customer_id, shipping_address)
        self.assertTrue(placed_order)

    def test_create_product(self):

        
        name = "Car"
        price = 20.0
        description = "Red color"
        stock_quantity = 10
        product = Product(name, price, description, stock_quantity)
        product_id = product.create_product()
        self.assertEqual(product_id,12 )     

    def test_customer_or_product_not_found_exception(self):
        
        name="pa"
        password=12 

        with self.assertRaises(CustomerNotFoundException):
               name="hea"
               password=12
               if self.ecommerce.customer_exists(name,password) > 0:
                    print("Customer login successfully")
               else:
                    raise CustomerNotFoundException("Customer doesnot exist.")
               
        with self.assertRaises(ProductNotFoundException):       
               product_id = 89
               exists = self.ecommerce.product_exists(product_id)
               if exists:
                     self.ecommerce.delete_product(product_id)
               else:
                  raise ProductNotFoundException("Product does not exist.")  

      

if __name__ == '__main__':
    unittest.main()