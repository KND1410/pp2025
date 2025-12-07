import math
import numpy as np

class Student:
    def _set_student(self, numbersStudent, idS, nameS, birth):
        self.__numberStudent = numbersStudent
        self.__idS = idS
        self.__nameS = nameS
        self.__birth = birth
    def _get_numberStudent(self):
        return self.__numberStudent
    def _get_idS(self):
        return self.__idS
    def _get_nameS(self):
        return self.__nameS
    def _get_birth(self):
        return self.__birth
    def __init__(self):
        self.numbersStudent = int(input("Enter the number of students: "))
        self.students = []
        for i in range(1, self.numbersStudent+1):
            self.idS = input(f"Enter the id of student #{i}: ")
            self.nameS = input(f"Enter the name of student #{i}: ")  
            self.birth = input(f"Date of birth of {self.nameS}: ")
            self.students.append({"Id": self.idS, "Student name": self.nameS, "birth": self.birth})
        print(self.students)

class Course:
    def _set_course(self, numberCourse, idC, ):
        self.__numberCourse = numberCourse
        self._idC = idC
    def _get_numberCourse(self):
        return self.__numberCourse
    def __init__(self):
        self.numberCourse = int(input("Enter the number of course: "))
        self.courses = []
        for i in range(1, self.numberCourse+1):
            self.idC = input(f"Enter the id of the course #{i}: ")
            self.nameC = str(input(f"Enter the name of the course #{i}: "))
            self.courses.append({"ID's course": self.idC, "Name course": self.nameC})
        print(self.courses)
    
name_course = Course()
studentinfo = Student()
course_names = [c["Name course"] for c in name_course.courses]

class Mark(Student, Course):
    marks = []
    for j in range(len(name_course.courses)):
        while True:
            finding = input("Choose a name of the course to enter mark for student: ")
            if finding in course_names:
                for i in range(len(studentinfo.students)):
                        mark = math.floor(float(input(f"{course_names[j]}'s mark for {studentinfo.students[i]["Student name"]} {studentinfo.students[i]["Id"]}: ")) * 10)/10
                        studentinfo.students[i][finding] = mark
                        marks.append(mark)
                break
            else:
                line = "Don't have course, course available:\n"
                for i in name_course.courses:
                    print(f"- {i['Name course']}")
                    

    for student in studentinfo.students:
        print(f"Student {student["Student name"]} mark:")
        student_marks = []
        for course in course_names:
            if course in student:
                print(f"- {course}: {student[course]}")
                student_marks.append(student[course])
    
    print("List of average sorted DES")
    print(f"Student average marks:")
    student_averages = []
    for student in studentinfo.students:
        student_avg = []
        for course in course_names:
            if course in student:
                student_avg.append(student[course])

        if student_avg:
            avg = math.floor(sum(student_avg) / len(student_avg) *10)/10
            student_averages.append((student['Student name'], avg))
    student_averages.sort(key=lambda x: x[1], reverse=True)
    for name, avg in student_averages:
        print(f"{name}: {avg}")