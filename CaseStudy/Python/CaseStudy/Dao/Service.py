import sys
sys.path.append('D:\\Hexaware_Assignment\\CaseStudy\\Python\\CaseStudy\\')
from Util.DBconn import DBConnection
from datetime import datetime
from MyException.exception import CustomerNotFoundException

class serviceprovider(DBConnection):


    def customer_exists(self, name, password):
        try:
            self.open()  
            query = f"SELECT COUNT(*) FROM customers WHERE name = '{name}' AND password = '{password}'"
            self.c.execute(query)
            count = self.c.fetchone()[0]  
            return count
        
        except CustomerNotFoundException("Customer not found") as e:
            print(e)
            return False
        
        finally:
            self.close() 

    def product_exists(self, product_id):
        try:
            self.open()
            query = f"SELECT COUNT(*) FROM products WHERE product_id = {product_id}"
            self.c.execute(query)
            count = self.c.fetchone()[0]
            return count > 0  
        except Exception as e:
            print(e)
            return False
        finally:
            self.close()  

    def show_all_products(self):
        try:
            self.open()
            query = "SELECT * FROM products"
            self.c.execute(query)
            products = self.c.fetchall()
            return products
        except Exception as e:
            print(e)
            return None
        finally:
            self.close()              

    def delete_product(self, product_id):
        try:
            self.open()
            query = f"DELETE FROM products WHERE product_id = {product_id}"
            self.c.execute(query)
            self.mydb.commit()
            print(f"Product with ID: {product_id} deleted successfully!")
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.close() 

    def deleteCustomer(self, customerId):
        try:
            self.open()
            query = f"DELETE FROM customers WHERE customer_id = {customerId}"
            self.c.execute(query)
            self.mydb.commit()
            print(f"Customer with ID: {customerId} deleted successfully!")
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.close()                           

    def addToCart(self, customer_id,product_id,quantity):
        try:
            self.open()
            query = f"SELECT stockQuantity FROM products WHERE product_id = {product_id}"
            self.c.execute(query)
            current_stock = self.c.fetchone()[0]

            if current_stock >= quantity:
                cart_query = "INSERT INTO cart (customer_id, product_id, quantity) VALUES (%s, %s, %s)"
                cart_values = (customer_id, product_id, quantity)
                self.c.execute(cart_query, cart_values)

                update_query = f"UPDATE products SET stockQuantity = {current_stock - quantity} WHERE product_id = {product_id}"
                self.c.execute(update_query)

                self.mydb.commit()
                print(f"Product '{product_id}' added to the cart of customer '{customer_id}' successfully!")
                return True
            else:
                print("Insufficient stock!")
                return False
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            self.close()

    def removeFromCart(self, customer_id, product_id):
        try:
            self.open()
            query = f"DELETE FROM cart WHERE customer_id = {customer_id} AND product_id = {product_id}"
            self.c.execute(query)
            self.mydb.commit()
            print(f"Product '{product_id}' removed from the cart of customer '{customer_id}' successfully!")
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            self.close()

    def getAllFromCart(self, customer_id):
        try:
            self.open()
            query = query = f"SELECT products.product_id, products.name, products.price, products.description, cart.quantity FROM cart INNER JOIN products ON cart.product_id = products.product_id WHERE cart.customer_id = {customer_id}"
            self.c.execute(query)
            products = self.c.fetchall()
            return products
        except Exception as e:
            print(f"Error occurred: {e}")
            return []
        finally:
            self.close()

    def placeOrder(self, customer_id, shipping_address):
        try:
            self.open()

            
            cart_query = "SELECT p.product_id, p.price, c.quantity FROM cart c INNER JOIN products p ON c.product_id = p.product_id WHERE c.customer_id = %s"
            self.c.execute(cart_query, (customer_id,))
            cart_products = self.c.fetchall()

            if not cart_products:
                print("Cart is empty. Cannot place an order.")
                return False

            
            total_price = sum(product[1] * product[2] for product in cart_products)

            
            order_date = datetime.now().strftime("%Y-%m-%d")
            order_query = "INSERT INTO orders (customer_id, order_date, total_price, shipping_address) VALUES (%s, %s, %s, %s)"
            order_values = (customer_id, order_date, total_price, shipping_address)
            self.c.execute(order_query, order_values)
            order_id = self.c.lastrowid

           
            order_items_query = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)"
            for product in cart_products:
                product_id = product[0]
                quantity = product[2]
                item_values = (order_id, product_id, quantity)
                self.c.execute(order_items_query, item_values)

            
            clear_cart_query = "DELETE FROM cart WHERE customer_id = %s"
            self.c.execute(clear_cart_query, (customer_id,))

            self.mydb.commit()
            print(f"Total Price: {total_price}")
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            self.close()

    def getOrdersByCustomer(self, customer_id):
        try:
            self.open()

            
            order_query = "SELECT orders.order_id, order_items.product_id, order_items.quantity FROM orders INNER JOIN order_items ON orders.order_id = order_items.order_id WHERE orders.customer_id = %s"
            self.c.execute(order_query, (customer_id,))
            orders_data = self.c.fetchall()

            orders = {}
            for order_id, product_id, quantity in orders_data:
                if order_id not in orders:
                    orders[order_id] = []
                orders[order_id].append((product_id, quantity))

            return orders
        except Exception as e:
            print(f"Error occurred: {e}")
            return {}
        finally:
            self.close()        