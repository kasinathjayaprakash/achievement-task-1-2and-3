# author - kasinath jayaprakash
#task- 7

#welcome message
print("hi\nwelcome to course registration")
#asking user to enter the first name
firstname = input("enter your first name:\n")
#asking user to enter the second name
lastname= input("enter your last name:\n")
#asking the user to enter the student id
studentid = input("enter your your student ID:\n")
#dictionary containing the courses available
course = {
    "PROG7685": "Process quality engineering",
    "PROG3465": "IT Business analysis",
    "PROG7845": "computer system technician",
    "PROG8467": "software engineering technician"
}
print("course code     course name" )
for key in course:
    print(key + "   " +course[key])
#asking the user the course to register
registration = input("enter the course code to register:\n").split(",")
#final output
print(firstname + "  " + lastname + "  " + studentid)
for code in registration:
    print(code + "  " + course[code])
    