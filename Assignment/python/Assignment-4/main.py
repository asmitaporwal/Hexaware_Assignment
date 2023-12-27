
from user import User
from courier import Courier
from Employee import Employee
from serviceprovider import serviceprovider
class Main:
   
    def main():
        s=serviceprovider()
        while True:
            print("\n----------Courier Management System Menu----------")
            print("\nPress-1 Place Courier Order")
            print("Press-2 Create User")
            print("Press-3 check courier status")
            print("Press-4 update courier status")
            print("Press-5 cancel courier order")
            print("Press-6 Get assigned orders")
            print("Press-7 Add employee")
            print("Press-8 Exit")
            i = int(input())

            if i == 1:
                user_id = int(input("Enter user ID: "))
                if s.check_user_existence(user_id):
                    username = input("Enter username: ")
                    password = input("Enter password: ")

       
                    if s.check_username_password(user_id, username, password):
                        courier_id = int(input("Enter courier ID: "))
                        sender_name = input("Enter sender's name: ")
                        sender_address = input("Enter sender's address: ")
                        receiver_name = input("Enter receiver's name: ")
                        receiver_address = input("Enter receiver's address: ")
                        weight = float(input("Enter package weight: "))
                        status = "Pending" 
                        trackingNumber=input("Enter trackingNumber: ") 
                        delivery_date = input("Enter delivery date (YYYY-MM-DD): ")
                        c=Courier(courier_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, trackingNumber, delivery_date, user_id)
                        tracking_number=c.place_order()
                        print(f"Courier order placed successfully. Tracking number: {tracking_number}")

                    else:
                       print("Invalid username or password.")
                else: 
                   print("User does not exist. Please create a user first.")
            elif i == 2:
                user_id = int(input("Enter user ID: "))
                if not s.check_user_existence(user_id):
                    user_name = input("Enter user's name: ")
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                    contact_number = input("Enter contact number: ")
                    address = input("Enter address: ")
                    user = User(user_id, user_name, email, password, contact_number, address)
                    user.create_user()
                    print("User created successfully.")
                else:
                    print("User already exists.")
            elif i == 3:
             tracking_number = input("Enter tracking number: ")
             status = s.getOrderStatus(tracking_number)
             if status is not None:
                print(f"The status of courier with tracking number {tracking_number} is: {status}")
             else:
               print("Failed to retrieve courier status.") 
            elif i == 4:
               tracking_number = input("Enter tracking number to update status: ")
               new_status = input("Enter new status: ")
               if s.update_courier_status(tracking_number, new_status):
                print("Courier status updated successfully.")
               else:
                print("Failed to update courier status.")
            elif i == 5:
               tracking_number = input("Enter tracking number to cancel order: ")
               if s.cancelOrder(tracking_number):
                print("Courier order cancelled successfully.")
               else:
                print("Failed to cancel courier order.") 
            elif i == 6:
                employee_id = int(input("Enter employee ID to fetch assigned orders: "))
                assigned_orders = s.getAssignedOrder(employee_id)
                if assigned_orders is not None:
                    if len(assigned_orders) > 0:
                        print(f"Orders assigned to EmployeeID {employee_id}:")
                        for order in assigned_orders:
                            print("Order ID:", order[0])
                            print("Sender:", order[1])
                            print("Sender Address:", order[2])
                            print("Receiver:", order[3])
                            print("Receiver Address:", order[4])
                            print("Weight:", order[5])
                            print("Status:", order[6])
                            print("Tracking Number:", order[7])
                            print("Delivery Date:", order[8])
                            print("Employee ID:", order[10])
                            print("-------------------------------------")
                    else:
                        print(f"No orders found for EmployeeID {employee_id}.")
                else:
                    print("Failed to fetch assigned orders.") 
            elif i == 7:
               id=int(input("Enter employee id: "))
               employee_name = input("Enter employee's name: ")
               employee_email = input("Enter employee's email: ")
               employee_contact = input("Enter employee's contact number: ")
               employee_role = input("Enter employee's role: ")
               employee_salary = float(input("Enter employee's salary: "))
               new_employee = Employee(id, employee_name, employee_email, employee_contact, employee_role, employee_salary)

               if new_employee.addCourierStaff():
                    print("Courier staff added successfully.")
               else:
                   print("Failed to add employee.")                
            elif i == 8:
                print("\nThank You\n")
                break

            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n')

if __name__ == "__main__":
    Main.main()