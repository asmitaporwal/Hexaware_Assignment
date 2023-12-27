from DBconnection import DBConnection

class serviceprovider(DBConnection):
    
    def check_user_existence(self, user_id):
        try:
            self.open()

            query = f"SELECT * FROM user WHERE userID = {user_id}"
            self.c.execute(query)
            result = self.c.fetchall()
            return bool(result)
        except Exception as e:
            print("Error occurred while checking user existence:", e)
            return False
        finally:
            self.close()

    def check_username_password(self, user_id, username, password):
        try:
            self.open()

            query = f"SELECT * FROM user WHERE userID = {user_id} AND Name = '{username}' AND password = '{password}'"
            self.c.execute(query)
            result = self.c.fetchall()

            return bool(result)
        except Exception as e:
            print("Error occurred while checking username and password:", e)
            return False
        finally:
            self.close() 

    def getOrderStatus(self, TrackingNumber):
        try:
            self.open()

            query = f"SELECT status FROM courier WHERE TrackingNumber = {TrackingNumber}"
            self.c.execute(query)
            result = self.c.fetchone()

            if result:
                return result[0]  # Return the status if the courier exists
            else:
                print("Courier order not found.")
                return None
        except Exception as e:
            print("Error occurred while fetching courier status:", e)
            return None
        finally:
            self.close()    

    def update_courier_status(self, tracking_number, new_status):
        try:
            self.open()

            query = f"UPDATE courier SET status = '{new_status}' WHERE trackingNumber = '{tracking_number}'"
            self.c.execute(query)
            self.mydb.commit()
            return True
        except Exception as e:
            print("Error occurred while updating courier status:", e)
            return False
        finally:
            self.close() 

    def cancelOrder(self, tracking_number):
        try:
            self.open()

            query = f"UPDATE courier SET status = 'Cancelled' WHERE trackingNumber = '{tracking_number}'"
            self.c.execute(query)
            self.mydb.commit()
            return True
        except Exception as e:
            print("Error occurred while cancelling courier order:", e)
            return False
        finally:
            self.close()

    def getAssignedOrder(self, employee_id):
        try:
            self.open()

            query = f"SELECT * FROM courier WHERE EmployeeID = {employee_id}"
            self.c.execute(query)
            result = self.c.fetchall()

            if result:
                return result 
            else:
                print("No orders found for this employee.")
                return None
        except Exception as e:
            print("Error occurred while fetching assigned orders:", e)
            return None
        finally:
            self.close()                                  