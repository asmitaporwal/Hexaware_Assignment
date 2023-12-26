
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

    def DisplayStudentInfo(self, student_id):
        try:
            self.open()
            query = f"""
                SELECT *
                FROM students
                WHERE student_id = {student_id}
            """

            self.c.execute(query)
            student_info = self.c.fetchone()

            if student_info:
                print("Student Information:")
                print(f"Student ID: {student_info[0]}")
                print(f"First Name: {student_info[1]}")
                print(f"Last Name: {student_info[2]}")
                print(f"Date of Birth: {student_info[3]}")
                print(f"Email: {student_info[4]}")
                print(f"Phone Number: {student_info[5]}")
            else:
                print("Student not found.")
        except Exception as e:
            print("Error while displaying student information:", e)
        finally:
            self.close()  

    def GetEnrolledCourses(self, student_id):
        try:
            self.open()
            query = f"""
                SELECT c.course_name
                FROM courses c
                INNER JOIN enrollments e ON c.course_id = e.course_id
                WHERE e.student_id = {student_id}
            """

            self.c.execute(query)
            enrolled_courses = self.c.fetchall()

            if enrolled_courses:
                # Return the list of enrolled courses
                return enrolled_courses
            else:
                return []  # Return an empty list if no courses are enrolled
        except Exception as e:
            print("Error while retrieving enrolled courses:", e)
            return []  # Return an empty list in case of an error
        finally:
            self.close()

    def GetPaymentHistory(self, student_id):
        try:
            self.open()
            query = f"""
                SELECT amount, payment_date
                FROM payments
                WHERE student_id = {student_id}
            """

            self.c.execute(query)
            payment_history = self.c.fetchall()

            return payment_history
        except Exception as e:
            print("Error while retrieving payment history:", e)
            return [] 
        finally:
            self.close()   

    def AssignTeacher(self, course_id, teacher_id):
        try:
            self.open()
            query = f"""
                UPDATE courses
                SET teacher_id = {teacher_id}
                WHERE course_id = {course_id}
            """

            self.c.execute(query)
            self.mydb.commit()
            print("Teacher assigned to the course successfully.")
        except Exception as e:
            print("Error while assigning teacher to course:", e)
        finally:
            self.close()

    def UpdateCourseInfo(self, course_name, credits, teacher_id):
        try:
            self.open()
            query = f"""
                UPDATE courses
                SET credits = {credits},
                    teacher_id = {teacher_id}
                WHERE course_name = '{course_name}'
            """

            self.c.execute(query)
            self.mydb.commit()
            print("Course information updated successfully.")
        except Exception as e:
            print("Error while updating course information:", e)
        finally:
            self.close() 

    def DisplayCourseInfo(self, course_name):
        try:
            self.open()
            query = f"""
                SELECT *
                FROM courses
                WHERE course_name = '{course_name}'
            """

            self.c.execute(query)
            course_info = self.c.fetchone()

            if course_info:
                print("Course Information:")
                print(f"Course ID: {course_info[0]}")
                print(f"Course Name: {course_info[1]}")
                print(f"Credits: {course_info[2]}")
                print(f"Teacher ID: {course_info[3]}")
            else:
                print("Course not found.")
        except Exception as e:
            print("Error while displaying course information:", e)
        finally:
            self.close()

    def GetEnrollments(self, course_name):
        try:
            self.open()
            query = f"""
                SELECT s.first_name, s.last_name
                FROM students s
                INNER JOIN enrollments e ON s.student_id = e.student_id
                INNER JOIN courses c ON c.course_id = e.course_id
                WHERE c.course_name = '{course_name}'
            """

            self.c.execute(query)
            student_enrollments = self.c.fetchall()

            if student_enrollments:
                print("Student Enrollments for the Course:")
                for student in student_enrollments:
                    print(f"Student: {student[0]} {student[1]}")
            else:
                print("No student enrollments found for this course.")
        except Exception as e:
            print("Error while retrieving student enrollments:", e)
        finally:
            self.close()

    def GetTeacher(self, course_name):
        try:
            self.open()
            query = f"""
                SELECT t.first_name, t.last_name
                FROM teacher t
                INNER JOIN courses c ON c.teacher_id = t.teacher_id
                WHERE c.course_name = '{course_name}'
            """

            self.c.execute(query)
            teacher_info = self.c.fetchone()

            if teacher_info:
                print("Assigned Teacher for the Course:")
                print(f"Teacher: {teacher_info[0]} {teacher_info[1]}")
            else:
                print("No teacher assigned for this course.")
        except Exception as e:
            print("Error while retrieving assigned teacher:", e)
        finally:
            self.close()
              
    def GetStudent(self, enrollment_id):
        try:
            self.open()
            query = f"""
                SELECT s.first_name, s.last_name
                FROM students s
                INNER JOIN enrollments e ON s.student_id = e.student_id
                WHERE e.enrollment_id = {enrollment_id}
            """

            self.c.execute(query)
            student_info = self.c.fetchone()

            if student_info:
                print("Student Associated with the Enrollment:")
                print(f"Student: {student_info[0]} {student_info[1]}")
            else:
                print("No student associated with this enrollment.")
        except Exception as e:
            print("Error while retrieving student information:", e)
        finally:
            self.close()

    def GetCourse(self, enrollment_id):
        try:
            self.open()
            query = f"""
                SELECT c.course_name
                FROM courses c
                INNER JOIN enrollments e ON c.course_id = e.course_id
                WHERE e.enrollment_id = {enrollment_id}
            """

            self.c.execute(query)
            course_info = self.c.fetchone()

            if course_info:
                print("Course Associated with the Enrollment:")
                print(f"Course Name: {course_info[0]}")
            else:
                print("No course associated with this enrollment.")
        except Exception as e:
            print("Error while retrieving course information:", e)
        finally:
            self.close() 

    def UpdateTeacherInfo(self, teacher_id, email,first_name,last_name):
        try:
            self.open()
            query = f"""
                UPDATE teacher
                SET email = '{email}',first_name='{first_name}',last_name='{last_name}'
                WHERE teacher_id = {teacher_id}
            """

            self.c.execute(query)
            self.mydb.commit()
            print("Teacher information updated successfully.")
        except Exception as e:
            print("Error while updating teacher information:", e)
        finally:
            self.close()

    def DisplayTeacherInfo(self, teacher_id):
        try:
            self.open()
            query = f"""
                SELECT *
                FROM teacher
                WHERE teacher_id = {teacher_id}
            """

            self.c.execute(query)
            teacher_info = self.c.fetchone()

            if teacher_info:
                print("Teacher Information:")
                print(f"Teacher ID: {teacher_info[0]}")
                print(f"First Name: {teacher_info[1]}")
                print(f"Last Name: {teacher_info[2]}")
                print(f"Email: {teacher_info[3]}")
            else:
                print("Teacher not found.")
        except Exception as e:
            print("Error while displaying teacher information:", e)
        finally:
            self.close()

    def GetAssignedCourses(self, teacher_id):
        try:
            self.open()
            query = f"""
                SELECT c.course_name
                FROM courses c
                WHERE c.teacher_id = {teacher_id}
            """

            self.c.execute(query)
            assigned_courses = self.c.fetchall()

            if assigned_courses:
                print("Courses Assigned to the Teacher:")
                for course in assigned_courses:
                    print(f"Course Name: {course[0]}")
            else:
                print("No courses assigned to this teacher.")
        except Exception as e:
            print("Error while retrieving assigned courses:", e)
        finally:
            self.close()