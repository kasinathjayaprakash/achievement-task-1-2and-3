#author - kasinath jayaprakash
#task - 9

import os
#student info
class Student:
    def _init_(self, studentname , studentnumber ,courseregistered =[] ):
        self.studentname = studentname
        self.studentnumber = studentnumber
        self.courseregistered = courseregistered

    #registers more courses
    def Courses(self, courses):
        self.courseregistered += courses

    #showing the information of the student
    def _str_(self):
        Info =  f"Student Name: {self.studentname}\n"
        Info += f"Student Number: {self.studentnumber}\n"
        Info += f"Total number of courses registered: {len(self.coursesregistered)}\n"
        Info += "-----------------------------------------------------------\n"
        Info += " registration has been confirmed for the following courses:\n"
        Info += "\n".join(f'Course #{i+1}: {self.courseregistered[i]}' for i in range(len(self.courseregistered)))
        return Info

#course
class Course:
    def _init_(self, coursename, coursecode):
        self.course_name = coursename
        self.course_code = coursecode
        
   
    def _str_(self):
        return f"{self.coursename} - {self.coursecode}"

#available cources
Availablecourses ={
    "PROG7685": Course("PROG7685", "Process quality engineering"),
    "PROG3465": Course("PROG3465", "IT Business analysis"),
    "PROG7845": Course("PROG7845", "computer system technician"),
    "PROG8467": Course("PROG8467", "software engineering technician"),
}

def main():
    student = Student(input("Enter the name of student: "), input("Enter the student number: "))
    while True:
        print("the available courses are:\n\n"+"\n".join(Availablecourses))
        registeredCourseIds = list(input("\n\nEnter the courses for registration: ").split())
        invalidCourses = []
        validCourses = []
        for courseid in registeredCourseIds:
            if courseid in Availablecourses.keys():
                validCourses.append(Availablecourses[courseid])
            else:
                invalidCourses.append(courseid)
        if len(invalidCourses) > 0:
            print("invalid codes: "+", ".join(invalidCourses))
            student.Courses(validCourses)
            break
        if len(validCourses) == 0:
            print("please provide a course")
        else:
            student.Courses(validCourses)
        choice = input("Do you want to exit the program (type '1' if yes) or want to continue with course registration(type '2'): ")
        if(choice == "1"):
            break

    #output
    print(student)
    Output = "student.txt"
    open(Output, "w").write(str(student))
    print(f"\nStudent info written to {os.path.abspath(Output)}")

main()
