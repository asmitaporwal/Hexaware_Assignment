class Customer:
    def __init__(self, customer_id=None, customer_name=None, email=None, phone_number=None, booking_id=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.booking_id = booking_id

    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_name(self):
        return self.customer_name
    
    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_booking_id(self):
        return self.booking_id
    
    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def display_customer_details(self):
        print("Customer ID: ",self.customer_id)
        print("Customer Name: ",self.customer_name)
        print("Email: ",self.email)
        print("Phone Number: ",self.phone_number)
        print("Booking ID: ",self.booking_id)