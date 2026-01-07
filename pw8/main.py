import gzip
import shutil
import curses
import os
import pickle
import threading
import time
from domain import number_student, student_iD, student_name, student_birth, list_student
from domain import number_course, course_iD, course_name, list_course, course_credit
from domain import mark_student, list_mark
from domain import infoManager

def compress_file_gzip(input_path, output_path):
    with open(input_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Compressed '{input_path}' to '{output_path}'")

class LoadThread(threading.Thread):
    def __init__(self, m, stdscr):
        threading.Thread.__init__(self)
        self.m = m
        self.stdscr = stdscr
        self.success = False
    
    def run(self):
        if os.path.exists("students.dat"):
            self.stdscr.addstr(1, 0, "Decompressing and loading data...")
            self.stdscr.refresh()

            time.sleep(1)
            
            with gzip.open("students.dat", "rb") as f:
                data = pickle.load(f)
            
            self.m.set_num_students(data["num_students"])
            self.m.set_student_ids(data["student_ids"])
            self.m.set_student_names(data["student_names"])
            self.m.set_student_births(data["student_births"])
            self.m.set_num_courses(data["num_courses"])
            self.m.set_course_ids(data["course_ids"])
            self.m.set_course_names(data["course_names"])
            self.m.set_course_credits(data["course_credits"])
            self.m.set_marks(data["marks"])
            
            self.stdscr.addstr(3, 0, f"Loaded {data['num_students']} students")
            self.stdscr.addstr(4, 0, f"Loaded {data['num_courses']} courses")
            self.stdscr.addstr(5, 0, f"Loaded {len(data['marks'])} marks")
            self.stdscr.refresh()
            
            self.success = True

def load_from_dat(m, stdscr):
    if os.path.exists("students.dat"):
        stdscr.clear()
        stdscr.addstr(0, 0, "Found students.dat file!")
        stdscr.refresh()

        load_thread = LoadThread(m, stdscr)
        load_thread.start()
        load_thread.join()
        
        stdscr.addstr(7, 0, "Press any key to continue...")
        stdscr.getch()
        return load_thread.success
    return False

class SaveThread(threading.Thread):
    def __init__(self, m):
        threading.Thread.__init__(self)
        self.m = m
    
    def run(self):
        print("Saving data in background...")
        
        time.sleep(1)
        
        data = {
            "num_students": self.m.get_num_students(),
            "student_ids": self.m.get_student_ids(),
            "student_names": self.m.get_student_names(),
            "student_births": self.m.get_student_births(),
            "num_courses": self.m.get_num_courses(),
            "course_ids": self.m.get_course_ids(),
            "course_names": self.m.get_course_names(),
            "course_credits": self.m.get_course_credits(),
            "marks": self.m.get_marks()
        }
        with gzip.open("students.dat", "wb") as f:
            pickle.dump(data, f)
        
        print("Finished saving data!")

def save_to_dat(m):
    save_thread = SaveThread(m)
    save_thread.start()
    save_thread.join()
    print("Save completed!")

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
        
        self.__listMark = list_mark(stdscr)
        self.__markStudent = mark_student(stdscr)
        self.__marks = []
        self.__mark_info = []

        self.__information = infoManager(stdscr)

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
    def get_listMark(self): return self.__listMark
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

    def get_mark_info(self): return self.__mark_info
    def set_mark_info(self, value): self.__mark_info = value

    def get_information(self): return self.__information
    def set_information(self, value): self.__information = value

def main(stdscr):
    m = Main(stdscr)
    curses.curs_set(0)

    load_from_dat(m, stdscr)
    
    option = ["Student", "Course", "Mark", "Student's information", "Exit"]
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
        
                            with open("Students.txt", "w") as f:
                                for i in range(m.get_num_students()):
                                    f.write(f"{i+1}. ID: {m.get_student_ids()[i]} | Name: {m.get_student_names()[i]} | Birth: {m.get_student_births()[i]}\n")

                            compress_file_gzip("Students.txt", "Students_info.gz")    
                        elif selected1 == 4:
                            m.set_students_info(m.get_listStudent().studentList(m.get_num_students(), m.get_student_ids(), m.get_student_names(), m.get_student_births()))

                        elif selected1 == 5:
                            break

            elif selected == 1:
                option2 = ["Number of course", "Course ID", "Course name","Course credit", "List of course", "Exit"]
                selected2 = 0
                stdscr.clear()
                while True:
                    stdscr.clear()
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

                            with open("Courses.txt", "w") as f:
                                for i in range(m.get_num_courses()):
                                    f.write(f"ID: {m.get_course_ids()[i]} | Name: {m.get_course_names()[i]} | Credits: {m.get_course_credits()[i]}\n")

                            compress_file_gzip("Courses.txt", "Courses_info.gz")

                        elif selected2 == 4:
                            m.set_course_info(m.get_listCourse().courseList(m.get_num_courses(), m.get_course_ids(), m.get_course_names(), m.get_course_credits()))

                        elif selected2 == 5:
                            break


            elif selected == 2:
                option3 = ["Enter student's mark", "List of mark", "Exit"]
                selected3 = 0
                stdscr.clear()
                while True:
                    stdscr.clear()
                    stdscr.addstr(5, 5, "Use arrow key to move\n")
                    for i in range(len(option3)):
                        if i == selected3:
                            stdscr.addstr(f"{option3[i]}\n", curses.A_REVERSE)
                        else:
                            stdscr.addstr(f"{option3[i]}\n")

                    key3 = stdscr.getch()

                    if key3 == curses.KEY_UP and selected3 > 0:
                        selected3 -= 1
                    if key3 == curses.KEY_DOWN and selected3 < len(option3) - 1:
                        selected3 += 1

                    #Option
                    elif key3 == 10:
                        if selected3 == 0:
                            m.set_marks(m.get_markStudent().markEnter(m.get_num_courses(), m.get_student_names(), m.get_course_names(), m.get_course_ids(),  m.get_course_credits(), m.get_num_students(), m.get_student_ids(), m.get_student_births()))
                            
                            with open("Marks.txt", "w") as f:
                                    for mark in m.get_marks():
                                        f.write(f"{mark['Student\'s name']} | {mark['Course']} | {mark['Mark']}\n")

                            compress_file_gzip("Marks.txt", "Marks_info.gz")
                        
                        elif selected3 == 1:
                            m.set_mark_info(m.get_listMark().markList(m.get_marks(), m.get_num_students(), m.get_student_names()))
                            
                        elif selected3 == 2:
                            break
            elif selected == 3:
                try:
                    info = m.get_information()
                    info.num_students = m.get_num_students()
                    info.student_ids = m.get_student_ids()
                    info.student_names = m.get_student_names()
                    info.student_births = m.get_student_births()
                    info.num_courses = m.get_num_courses()
                    info.course_ids = m.get_course_ids()
                    info.course_names = m.get_course_names()
                    info.course_credits = m.get_course_credits()
                    info.marks = m.get_marks()
                    info.show_data()
                except Exception as e:
                    stdscr.clear()
                    stdscr.addstr(0, 0, f"ERROR: {str(e)}")
                    stdscr.getch()

            elif selected == 4:
                save_to_dat(m)
                break


if __name__ == "__main__":
    curses.wrapper(main)