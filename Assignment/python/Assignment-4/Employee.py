from DBconnection import DBConnection
class Employee(DBConnection):
    def __init__(self, employeeID, employeeName, email, contactNumber, role, salary):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.email = email
        self.contactNumber = contactNumber
        self.role = role
        self.salary = salary

    def addCourierStaff(self):
        try:
            self.open()

            query = f"INSERT INTO employee (EmployeeID,Name, Email, ContactNumber, Role, Salary) VALUES ('{self.employeeID}', '{self.employeeName}', '{self.email}', '{self.contactNumber}', '{self.role}', '{self.salary}')"
            self.c.execute(query)
            self.mydb.commit()
            return True
        except Exception as e:
            print("Error occurred while adding courier staff:", e)
            return False
        finally:
            self.close()    