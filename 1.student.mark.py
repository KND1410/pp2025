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
        nameC = str(input(f"Enter the name of the course #{i}: "))
        courses.append({"ID's course": idC, "Name course": nameC})
    print(courses)
    return courses
    
        
name_course = course()
studentinfo = student()
course_names = [c["Name course"] for c in name_course]

for j in range(len(name_course)):
    while True:
        finding = input("Choose a name of the course to enter mark for student: ")
        if finding in course_names:
            for i in range(len(studentinfo)):
                    mark = input(f"{course_names[j]}'s mark for {studentinfo[i]["Student name"]} {studentinfo[i]["Id"]}: ")
                    studentinfo[i][finding] = mark
            break
        else:
            line = "Don't have course, course available:\n"
            for i in name_course:
                print(f"- {i['Name course']}")
                

for student in studentinfo:
    print(f"Student {student["Student name"]} mark:\n", end = ' ')
    for course in course_names:
        if course in student:
            print(f"- {course}: {student[course]}")