
from DBconnection import DBConnection


class Repository(DBConnection):
    def __init__(self):
        pass
    def UpdateStudentInfo(self, student_id, new_first_name, new_last_name, new_date_of_birth, new_email, new_phone_number):
        try:
            self.open()
            self.c.execute(f"UPDATE students SET first_name = ('{new_first_name}'), last_name = ('{new_last_name}'),date_of_birth = ('{new_date_of_birth}'),email = ('{new_email}'),phonenumber = ('{new_phone_number}') WHERE student_id =('{student_id}')")
            self.mydb.commit()
            print("Student information updated successfully.")
        except Exception as e:
            print("Error while updating student information:", e)
        finally:
            self.close()    