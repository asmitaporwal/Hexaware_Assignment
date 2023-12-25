from DBconnection import DBConnection

class Enrollment(DBConnection):
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def EnrollInCourse(self):
        try:
            self.open()
            self.c.execute(f"INSERT INTO Enrollments (enrollment_id,student_id, course_id, enrollment_date) VALUES ('{self.enrollment_id}','{self.student_id}','{self.course_id}','{self.enrollment_date}')")
            self.mydb.commit()
            print("Enrolled student in the course successfully.")
        except Exception as e:
            print("Error while enrolling student in course:", e)
        finally:
            self.close()    