import sys
sys.path.append('D:\\CaseStudy\\')
import unittest
from Dao.Service import serviceprovider
from Entity.product import Product
from MyException.exception import CustomerNotFoundException,ProductNotFoundException,OrderNotFoundException


class TestEcommerceSystem(unittest.TestCase):
    def setUp(self):
        self.ecommerce = serviceprovider()

  

    def test_add_to_cart(self):
       
        customer_id = 1  
        product_id = 1   
        quantity = 2
        added_to_cart = self.ecommerce.addToCart(customer_id, product_id, quantity)
        self.assertTrue(added_to_cart)
        

    def test_place_order(self):
        
        customer_id = 1 
        shipping_address = "Test Address"
        placed_order = self.ecommerce.placeOrder(customer_id, shipping_address)
        self.assertTrue(placed_order)
        

    # def test_customer_or_product_not_found_exception(self):
    #     # Test if the correct exception is thrown when customer or product is not found
    #     invalid_customer_id = 9999  # Replace with a non-existent customer ID in your test database
    #     invalid_product_id = 9999   # Replace with a non-existent product ID in your test database

    #     with self.assertRaises(CustomerNotFoundException):
    #         self.ecommerce.CustomerNotFoundException(invalid_customer_id)

    #     with self.assertRaises(CustomerOrProductNotFoundException):
    #         self.ecommerce.customerOrProductNotFound(invalid_product_id)
    #     # Add more assertions or test cases for exception handling

if __name__ == '__main__':
    unittest.main()