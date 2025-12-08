import math
import numpy as np
import curses
from curses import wrapper

def get_string(stdscr, promt, row, col):
    stdscr.addstr(row, col, promt)
    stdscr.refresh()

    curses.echo()
    input_string = stdscr.getstr(row, col + len(promt), 20)
    curses.noecho()

    return input_string.decode('utf-8')


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
    def __init__(self, stdscr):
        self.numbersStudent = int(get_string(stdscr, "Enter the number of students: ", 0, 0))
        self.students = []
        for i in range(1, self.numbersStudent+1):
            self.idS = get_string(stdscr, f"Enter the id of student #{i}: ", 1, 0)
            self.nameS = get_string(stdscr, f"Enter the name of student #{i}: ", 2, 0)  
            self.birth = get_string(stdscr, f"Date of birth of {self.nameS}: ", 3, 0)
            self.students.append({"Id": self.idS, "Student name": self.nameS, "birth": self.birth})
        stdscr.addstr(4, 0, str(self.students))

class Course:
    def _set_course(self, numberCourse, idC, ):
        self.__numberCourse = numberCourse
        self._idC = idC
    def _get_numberCourse(self):
        return self.__numberCourse
    def __init__(self, stdscr):
        self.numberCourse = int(get_string(stdscr, "Enter the number of course: ", 5, 0))
        self.courses = []
        for i in range(1, self.numberCourse+1):
            self.idC = get_string(stdscr, f"Enter the id of the course #{i}: ", 6,0)
            self.nameC = str(get_string(stdscr, f"Enter the name of the course #{i}: ", 7, 0))
            self.courses.append({"ID's course": self.idC, "Name course": self.nameC})
        stdscr.addstr(8, 0, str(self.courses))
def main(stdscr): 
    curses.curs_set(1)
    name_course = Course(stdscr)
    # stdscr.clear()
    studentinfo = Student(stdscr)
    course_names = [c["Name course"] for c in name_course.courses]

    marks = []
    for j in range(len(name_course.courses)):
        while True:
            finding = get_string(stdscr, "Choose a name of the course to enter mark for student: ", 9, 0)
            if finding in course_names:
                for i in range(len(studentinfo.students)):
                        mark = math.floor(float(get_string(stdscr, f"{course_names[j]}'s mark for {studentinfo.students[i]["Student name"]} {studentinfo.students[i]["Id"]}: ", 10, 0)) * 10, )/10
                        studentinfo.students[i][finding] = mark
                        marks.append(mark)
                break
            else:
                line = stdscr.addstr(11, 0, "Don't have course, course available:\n")
                for i in name_course.courses:
                    stdscr.addstr(12, 0, f"- {i['Name course']}")
                    
    stdscr.clear()
    for student in studentinfo.students:
        stdscr.addstr(10, 0, f"Student {student["Student name"]} mark:")
        student_marks = []
        for course in course_names:
            if course in student:
                stdscr.addstr(13, 0, f"- {course}: {student[course]}")
                student_marks.append(student[course])
    
    stdscr.addstr(14, 0, "List of average sorted DES")
    stdscr.addstr(15, 0,f"Student average marks:")
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
        stdscr.addstr(16, 0, f"{name}: {avg}")
    stdscr.getch()
wrapper(main)