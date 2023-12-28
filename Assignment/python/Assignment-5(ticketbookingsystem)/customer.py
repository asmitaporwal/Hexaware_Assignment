class Customer:
    def __init__(self, customer_id,customer_name, email, phone_number):
        self.customer_id=customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number


    def get_customer_id(self):
        return self.customer_id
    
    def get_customer_name(self):
        return self.customer_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number
    
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number