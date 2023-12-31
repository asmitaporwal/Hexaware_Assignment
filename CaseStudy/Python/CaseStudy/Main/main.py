import sys
sys.path.append('D:\\Hexaware_Assignment\\CaseStudy\\Python\\CaseStudy\\')
from  Dao.Service import serviceprovider
from  Entity.product import Product
from Entity.customers import Customer
from MyException.exception import CustomerNotFoundException,ProductNotFoundException,OrderNotFoundException


class  EcomApp:

    def main(): 
        s = serviceprovider()
        while True:
           print("\n----------Main Menu----------")
           print("Press-1 Add a new product")
           print("Press-2 Register Customer")
           print("Press-3 Delete Product")
           print("Press-4 Add To Cart")
           print("Press-5 Remove From Cart")
           print("Press-6 View Cart")
           print("Press-7 Place Order")
           print("Press-8 Get Orders By Customer")
           print("Press-9 Exit")
        

           ch = input("Enter your choice: ")

           if ch == '1':
            product_name = input("Enter product name: ")
            description = input("Enter description: ")
            price = float(input("Enter price: "))
            quantity=int(input("Enter stock quantity: "))
            product_id = Product(product_name, price,description,quantity).create_product()
            if product_id:
                print("Product added successfully!")
            else:
                print("Failed to add product.")


           elif ch == '2':
            name=input("Enter customer name: ")
            password=input("Enter password: ")
            if s.customer_exists(name,password) > 0:
               print("Customer already exists")
            else:
               email=input("Enter email: ")
               Customer(name,email,password).create_customer() 

           elif ch == '3':
               all_products = s.show_all_products()
               if all_products is not None:
                  print("All Products:")
                  for product in all_products:
                     product_id, name, price, description, stock_quantity = product 
                     print(f"Product id:{product_id},Product Name: {name},Price: {price},Description: {description},Stock Quantity: {stock_quantity}")
                  product_id = input("Enter product id: ")
                  exists = s.product_exists(product_id)
                  if exists:
                     s.delete_product(product_id)
                  else:
                     raise ProductNotFoundException("Product does not exist.")
               else:
                  print("Failed to retrieve products.")   

           elif ch == '4':
               customer_id=int(input("Enter customer id: ")) 
               name=input("Enter customer name: ")
               password=input("Enter password: ")
               if s.customer_exists(name,password) > 0:
                    print("Customer login successfully")
               else:
                    raise CustomerNotFoundException("Customer doesnot exist.") 
               all_products = s.show_all_products()
               if all_products is not None:
                 print("All Products:")
                 for product in all_products:
                    product_id,name, price, description, stock_quantity = product 
                    print(f"Product ID: {product_id},Product Name: {name},Price: {price},Description: {description},Stock Quantity: {stock_quantity}")    
                 product_id=int(input("Enter product id: "))
                 quantity=int(input("Enter quantity: "))
                 s.addToCart(customer_id,product_id,quantity)
               else:
                 print("Failed to add product")     
              
           elif ch == '5':
               customer_id = int(input("Enter customer id: "))
               name=input("Enter customer name: ")
               password=input("Enter password: ")
               if s.customer_exists(name,password) > 0:
                    print("Customer login successfully")
               else:
                    raise CustomerNotFoundException("Customer doesnot exist.") 
               products_in_cart = s.getAllFromCart(customer_id)
               if products_in_cart:
                  print("Products in Cart:")
                  for product in products_in_cart:
                     print(f"Product id: {product[0]} , Porduct Name: {product[1]}, price: ${product[2]}, description:{product[3]}, quantity: {product[4]}") 
        
                  product_id_to_remove = int(input("Enter product id to remove from cart: "))
                  success = s.removeFromCart(customer_id, product_id_to_remove)
                  if success:
                     print("Product removed from cart successfully!")
                  else:
                     print("Failed to remove product from cart.")
               else:
                  print("No products in the cart.")   

           elif ch == '6':
              customer_id = int(input("Enter customer id: "))
              name=input("Enter customer name: ")
              password=input("Enter password: ")
              if s.customer_exists(name,password) > 0:
                    print("Customer login successfully")
              else:
                    raise CustomerNotFoundException("Customer doesnot exist.") 
              products_in_cart = s.getAllFromCart(customer_id)
              if products_in_cart:
               print("Products in Cart:")
               for product in products_in_cart:
                  print(f"Product id: {product[0]} , Porduct Name: {product[1]}, price: ${product[2]}, description:{product[3]}, quantity: {product[4]}")  
              else:
               print("No products in the cart.")

           elif ch == '7':
               customer_id = int(input("Enter customer id: "))
               name=input("Enter customer name: ")
               password=input("Enter password: ")
               if s.customer_exists(name,password) > 0:
                    print("Customer login successfully")
               else:
                    raise CustomerNotFoundException("Customer doesnot exist.") 
               shipping_address = input("Enter shipping address: ")
               success = s.placeOrder(customer_id, shipping_address)
               if success:
                    print("Order placed successfully!")
               else:
                    print("Failed to place the order.")

           elif ch == '8':
                customer_id = int(input("Enter customer id: "))
                name=input("Enter customer name: ")
                password=input("Enter password: ")
                if s.customer_exists(name,password) > 0:
                    print("Customer login successfully")
                else:
                    raise CustomerNotFoundException("Customer doesnot exist.") 
                orders = s.getOrdersByCustomer(customer_id)
                if orders:
                    print("Orders By Customer:")
                    for order_id, products in orders.items():
                        for product_id, quantity in products:
                           print(f"Order ID:{order_id},Product ID: {product_id}, Quantity: {quantity}")
                else:
                    raise OrderNotFoundException("Order not found")

           elif ch == '9':
                print("Thank you")
                break

           else:
                print("Invalid choice. Please try again.")
 

if __name__ == "__main__":
    EcomApp.main()
