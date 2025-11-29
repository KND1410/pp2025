def student():
    numberS = int(input("Enter the number of students: "))
    students = []
    for i in range(1, numberS+1):
        idS = input(f"Enter the id of student #{i}: ")
        nameS = input(f"Enter the name of student #{i}: ")
        birth = input(f"Date of birth of {nameS}: ")
        students.append({"Id": idS, "Student name": nameS, "birth": birth})
    print(students)
    return students

def course():
    numberC = int(input("Enter the number of course: "))
    courses = []
    for i in range(1, numberC+1):
        idC = input(f"Enter the id of the course #{i}: ")
        nameC = input(f"Enter the name of the course #{i}: ")
        courses.append({"ID's course": idC, "Name course": nameC})
    print(courses)
    return courses
    
        
name_course = course()
studentinfo = student()
course_names = [c["Name course"] for c in name_course]
finding = input("Choose a name of the course to enter mark for student: ")
if finding in course_names:
    for i in range(len(studentinfo)):
        mark = input(f"mark for {studentinfo[i]["Student name"]} {studentinfo[i]["Id"]}: ")
        studentinfo[i][finding] = mark
else:
    print("Don't have course")

for student in studentinfo:
    print(f"Sudent {student["Student name"]} mark:", end = ' ')
    print(student)