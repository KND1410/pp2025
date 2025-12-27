import curses
from student import number_student, student_iD, student_name, student_birth, list_student
from course import number_course, course_iD, course_name, list_course, course_credit
from mark import mark_student

class Main():
    def __init__(self, stdscr):
        self.__numberStudents = number_student(stdscr)
        self.__idStudent = student_iD(stdscr)
        self.__nameStudent = student_name(stdscr)
        self.__birthStudent = student_birth(stdscr)
        self.__listStudent = list_student(stdscr)
        
        self.__num_students = 0
        self.__student_ids = []
        self.__student_names = []
        self.__student_births = []
        self.__students_info = []
        
        self.__numberCourse = number_course(stdscr)
        self.__courseID = course_iD(stdscr)
        self.__courseName = course_name(stdscr)
        self.__listCourse = list_course(stdscr)
        self.__creditCourse = course_credit(stdscr)
        
        self.__course_info = []
        self.__num_courses = 0
        self.__course_ids = []
        self.__course_names = []
        self.__course_credits = []
        
        self.__markStudent = mark_student(stdscr)
        self.__marks = []

    def get_numberStudents(self): return self.__numberStudents
    def get_idStudent(self): return self.__idStudent
    def get_nameStudent(self): return self.__nameStudent
    def get_birthStudent(self): return self.__birthStudent
    def get_listStudent(self): return self.__listStudent
    
    def get_numberCourse(self): return self.__numberCourse
    def get_courseID(self): return self.__courseID
    def get_courseName(self): return self.__courseName
    def get_listCourse(self): return self.__listCourse
    def get_markStudent(self): return self.__markStudent
    def get_creditCourse(self): return self.__creditCourse

    def get_num_students(self): return self.__num_students
    def set_num_students(self, value): self.__num_students = value

    def get_student_ids(self): return self.__student_ids
    def set_student_ids(self, value): self.__student_ids = value

    def get_student_names(self): return self.__student_names
    def set_student_names(self, value): self.__student_names = value

    def get_student_births(self): return self.__student_births
    def set_student_births(self, value): self.__student_births = value

    def get_students_info(self): return self.__students_info
    def set_students_info(self, value): self.__students_info = value

    def get_num_courses(self): return self.__num_courses
    def set_num_courses(self, value): self.__num_courses = value

    def get_course_ids(self): return self.__course_ids
    def set_course_ids(self, value): self.__course_ids = value

    def get_course_names(self): return self.__course_names
    def set_course_names(self, value): self.__course_names = value

    def get_course_info(self): return self.__course_info
    def set_course_info(self, value): self.__course_info = value

    def get_course_credits(self): return self.__course_credits
    def set_course_credits(self, value): self.__course_credits = value

    def get_marks(self): return self.__marks
    def set_marks(self, value): self.__marks = value

def main(stdscr):
    m = Main(stdscr)
    curses.curs_set(0)
    option = ["Student", "Course", "Mark", "Exit"]
    selected = 0

    while True:
        stdscr.clear()
        
        stdscr.addstr(5, 5, "Use arrow key to move\n\n")
        for i in range(len(option)):
            if i == selected:
                stdscr.addstr(f"{option[i]}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"{option[i]}\n")
        key = stdscr.getch()
        
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        if key == curses.KEY_DOWN and selected < len(option) - 1:
            selected += 1
        elif key == 10:

            if selected == 0:
                stdscr.clear()
                option1 = ["Number of the student", "Student\'s ID", "Student\'s name", "Student\'s birth", "List of student", "Exit"]
                selected1 = 0
                stdscr.clear()
                while True:    
                    stdscr.addstr(5, 5, "Use arrow key to move\n\n")
                    for i in range(len(option1)):
                        if i == selected1:
                            stdscr.addstr(f"{option1[i]}\n", curses.A_REVERSE)
                        else:
                            stdscr.addstr(f"{option1[i]}\n")
                    key1 = stdscr.getch()
                    
                    if key1 == curses.KEY_UP and selected1 > 0:
                        selected1 -= 1
                    if key1 == curses.KEY_DOWN and selected1 < len(option1) - 1:
                        selected1 += 1
                    #Options
                    elif key1 == 10:
                        if selected1 == 0:
                            m.set_num_students(m.get_numberStudents().numberStudent())
                        elif selected1 == 1:
                            m.set_student_ids(m.get_idStudent().studentID(m.get_num_students()))
                        elif selected1 == 2:
                            m.set_student_names(m.get_nameStudent().studentName(m.get_num_students(), m.get_student_ids()))
                        elif selected1 == 3:
                            m.set_student_births(m.get_birthStudent().studentBirth(m.get_num_students(), m.get_student_ids(), m.get_student_names()))
                        elif selected1 == 4:
                            m.set_students_info(m.get_listStudent().studentList(m.get_num_students(), m.get_student_ids(), m.get_student_names(), m.get_student_births()))
                        elif selected1 == 5:
                            break

            elif selected == 1:
                option2 = ["Number of course", "Course ID", "Course name","Course credit", "List of course", "Exit"]
                selected2 = 0
                stdscr.clear()
                while True:
                    stdscr.addstr(5, 5, "Use arrow key to move\n")
                    for i in range(len(option2)):
                        if i == selected2:
                            stdscr.addstr(f"{option2[i]}\n", curses.A_REVERSE)
                        else:
                            stdscr.addstr(f"{option2[i]}\n")

                    key2 = stdscr.getch()

                    if key2 == curses.KEY_UP and selected2 > 0:
                        selected2 -= 1
                    if key2 == curses.KEY_DOWN and selected2 < len(option2) - 1:
                        selected2 += 1

                    # OPTIONS
                    elif key2 == 10:
                        if selected2 == 0:
                            m.set_num_courses(m.get_numberCourse().numberCourse())

                        elif selected2 == 1:
                            m.set_course_ids(m.get_courseID().courseID(m.get_num_courses()))

                        elif selected2 == 2:
                            m.set_course_names(m.get_courseName().courseName(m.get_num_courses(), m.get_course_ids()))

                        elif selected2 == 3:
                            m.set_course_credits(m.get_creditCourse().courseCredit(m.get_num_courses(), m.get_course_ids(), m.get_course_names()))

                        elif selected2 == 4:
                            m.set_course_info(m.get_listCourse().courseList(m.get_num_courses(), m.get_course_ids(), m.get_course_names(), m.get_course_credits()))
                        elif selected2 == 5:
                            break


            elif selected == 2:
                m.set_marks(m.get_markStudent().markEnter(m.get_num_courses(), m.get_student_names(), m.get_course_names(), m.get_course_ids(),  m.get_course_credits(), m.get_num_students(), m.get_student_ids(), m.get_student_births()))

            elif selected == 3:
                break

curses.wrapper(main)