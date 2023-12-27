
from DBconnection import DBConnection


class User(DBConnection):
    def __init__(self, userID, userName, email, password, contactNumber, address):
        self.userID = userID
        self.userName = userName
        self.email = email
        self.password = password
        self.contactNumber = contactNumber
        self.address = address

    def get_user_id(self):
        return self.userID

    def get_user_name(self):
        return self.userName

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_contact_number(self):
        return self.contactNumber

    def get_address(self):
        return self.address

    # Setters
    def set_user_id(self, userID):
        self.userID = userID

    def set_user_name(self, userName):
        self.userName = userName

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def set_contact_number(self, contactNumber):
        self.contactNumber = contactNumber

    def set_address(self, address):
        self.address = address

    def create_user(self):
        try:
            self.open()

            query = f"INSERT INTO user (userID, Name, email, password, contactNumber, address) VALUES ({self.userID}, '{self.userName}', '{self.email}', '{self.password}', '{self.contactNumber}', '{self.address}')"
            self.c.execute(query)
            self.mydb.commit()

            print("User created successfully.")
        except Exception as e:
            print("Error occurred while creating user:", e)
        finally:
            self.close()    

    