from Enrollment import Enrollment
from Payment import Payment
from service import Repository

class Main():
    def main():
        r=Repository()
        while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 Enroll in course")
            print("Press-2 Update student info")
            print("Press-3 Record payment")
            print("Press-4 Get student info")
            print("Press-5 student enrolled courses")
            print("Press-6 All payments")
            print("Press-7 Assign teacher to course")
            print("Press-8 update course info")
            print("Press-9 Get course info")
            print("Press-10 Get enrolled students in a course")
            print("Press-11 Get teacher of a particular course")
            print("Press-12  student associated with the enrollment")
            print("Press-13 course associated with the enrollment")
            print("Press-14 Update teacher info")
            print("Press-15 display teacher info")
            print("Press-16 display assigned course to teacher")
            print("Press-17 Exit")
            i=int(input())
            if i==1:
                id=int(input("\nEnter enrollment id: "))
                s=int(input("\nEnter stundent id: "))
                c=int(input("\nEnter Course id: "))
                d=input("\nEnter enrollment date: ")
                Enrollment(enrollment_id=id,student_id=s,course_id=c,enrollment_date=d).EnrollInCourse()
            elif i == 2:
                sid=int(input("\nEnter student id: "))
                fname=input("\nEnter New firstname: ")
                lname=input("\nEnter New lastname: ")
                dob=input("\nEnter new DOB: ")
                email=input("\nEnter new email: ")
                phoneno=input("\nEnter new phone no: ")
                r.UpdateStudentInfo(sid,fname,lname,dob,email,phoneno)  
            elif i == 3:
                id=int(input("\nEnter payment id: "))
                sid=int(input("\nEnter student id: "))
                a=float(input("\nEnter amount: "))
                p=input("\nEnter payment date: ")
                Payment(payment_id=id,student_id=sid,amount=a,payment_date=p).MakePayment()
            elif i == 4:
                id=int(input("\nEnter studentid: "))
                r.DisplayStudentInfo(id)
            elif i == 5:
                id=int(input("Enter student id: "))
                enrolled_courses=r.GetEnrolledCourses(id)
                if enrolled_courses:
                      print("Courses Enrolled:")
                      for course in enrolled_courses:
                           print(f"Course Name: {course[0]}")
                           print()  
                else:
                   print("No courses enrolled for this student.")
            elif i == 6:
               id=int(input("\nEnter studentid: "))
               payment_history=r.GetPaymentHistory(id)
               if payment_history:
                    print("Payment History:")
                    for payment_record in payment_history:
                        print(f"Amount: {payment_record[0]}")
                        print(f"Payment Date: {payment_record[1]}")
                        print()  # Empty line for separation
               else:
                print("No payment records found for this student.")
            elif i == 7:
                cid=int(input("\nEnter courseid: ")) 
                tid=int(input("\nEnter teacher: "))  
                r.AssignTeacher(cid,tid)
            elif i == 8:
               cname=input("\nEnter new course name: ")
               credit=int(input("\nEnter new credtis: "))
               tid=input("\nEnter new teacher id: ")
               r.UpdateCourseInfo(cname,credit,tid)
            elif i == 9:
                cname=input("\nEnter new course name: ")
                r.DisplayCourseInfo(cname)
            elif i == 10:
                cname=input("\nEnter new course name: ")
                r.GetEnrollments(cname)
            elif i == 11:
                cname=input("\nEnter new course name: ")
                r.GetTeacher(cname)        
            elif i == 12:
                id=int(input("\nEnter enrollment id: "))
                r.GetStudent(id) 
            elif i == 13:
                id=int(input("\nEnter enrollment id: "))
                r.GetCourse(id)
            elif i == 14:
                tid=int(input("\nEnter teacher id: "))
                tfname=input("\nEnter updated first name: ")
                tlname=input("\nEnter updated last name: ")
                email=input("\nEnter new email: ")
                r.UpdateTeacherInfo(tid,email,tfname,tlname)
            elif i == 15:
                tid=int(input("\nEnter teacher id: "))
                r.DisplayTeacherInfo(tid)
            elif i == 16:
                tid=int(input("\nEnter teacher id: "))
                r.GetAssignedCourses(tid)
            elif i == 17:
                print("\nThank You\n")
                break 
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n') 

if __name__ == "__main__":
    Main.main()                  



