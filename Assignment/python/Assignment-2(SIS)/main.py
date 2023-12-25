from Enrollment import Enrollment
from repo import Repository

class Main():
    def main():
        r=Repository()
        while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 Enroll in course")
            print("Press-2 Update student info")
            print("Press-3 Exit")
            i=int(input())
            if i==1:
                id=int(input("\nEnter enrollment id: "))
                s=int(input("\nEnter stundent id: "))
                c=int(input("\nEnter Course id: "))
                d=input("\nEnter enrollment date: ")
                enrollment=Enrollment(enrollment_id=id,student_id=s,course_id=c,enrollment_date=d).EnrollInCourse()
            elif i == 2:
                sid=int(input("\nEnter student id: "))
                fname=input("\nEnter New firstname: ")
                lname=input("\nEnter New lastname: ")
                dob=input("\nEnter new DOB: ")
                email=input("\nEnter new email: ")
                phoneno=input("\nEnter new phone no: ")
                r.UpdateStudentInfo(sid,fname,lname,dob,email,phoneno)  
            elif i == 3:
                print("\nThank You\n")
                break            
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n') 

if __name__ == "__main__":
    Main.main()                  



