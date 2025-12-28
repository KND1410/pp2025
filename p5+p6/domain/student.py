import curses
try:
    from ..input import get_string
except Exception:
    from input import get_string


class number_student:
    def __init__(self, stdscr):
        self.num_students = 0
        self.stdscr = stdscr

    def numberStudent(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== ENTER NUMBER OF STUDENTS ===\n\n")
        self.stdscr.refresh()
        s = get_string(self.stdscr, "Enter the number of students: ", 2, 0)
        try:
            self.num_students = int(s)
        except Exception:
            self.stdscr.addstr(4, 0, "Invalid number. Press any key to continue...")
            self.stdscr.getch()
            return self.num_students

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, f"Number of students set to: {self.num_students}")
        self.stdscr.addstr(2, 0, "Press any key to go back...")
        self.stdscr.getch()

        return self.num_students


class student_iD:
    def __init__(self, stdscr):
        self.student_ids = []
        self.stdscr = stdscr

    def studentID(self, num_students):
        if num_students == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "number of student" to enter the number of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []

        self.student_ids = []

        for i in range(num_students):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"=== ENTER STUDENT IDs ({i+1}/{num_students}) ===\n\n")
            s = get_string(self.stdscr, f"Enter student's ID {i+1}: ", 2, 3)
            self.student_ids.append(s)

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, f"Studens' id: {self.student_ids}")
        self.stdscr.addstr(2, 0, "Press any key to go back...")
        self.stdscr.getch()
        self.stdscr.clear()

        return self.student_ids

class student_name:
    def __init__(self, stdscr):
        self.student_names = []
        self.stdscr = stdscr
    
    def studentName(self, num_students, student_ids):
        if num_students == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "Number of the student" option to enter the number of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        elif not student_ids or len(student_ids) == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "Student\'s ID" option to enter the id of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        self.student_names = []

        for i in range(num_students):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"=== ENTER STUDENT NAMEs ({i+1}/{num_students}) ===\n\n")
            s = get_string(self.stdscr, f"Enter student's name {i+1}: ", 2, 3)
            self.student_names.append(s)

        self.stdscr.clear()
        students_name = []
        for i in range(len(self.student_names)):
            students_name.append({"Student's ID":student_ids[i], "Student's name":self.student_names[i]})
        self.stdscr.addstr(0, 0, f"Students' info: {students_name}")
        self.stdscr.addstr(2, 0, "Press any key to go back...")
        self.stdscr.getch()

        return self.student_names
class student_birth:
    def __init__(self, stdscr):
        self.student_births = []
        self.stdscr = stdscr
    def studentBirth(self, num_students, student_ids, student_names):
        if num_students == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "Number of the student" option to enter the number of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        elif not student_ids or len(student_ids) == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "Student\'s ID" option to enter the id of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        elif not student_names or len(student_names) == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, 'Please go to option "Student\'s name" option to enter the name of student')
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        
        for i in range(num_students):
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"=== ENTER STUDENT BIRTHs ({i+1}/{num_students}) ===\n\n")
            s = get_string(self.stdscr, f"Enter student's birth {i+1}: ", 2, 3)
            self.student_births.append(s)
        
        self.stdscr.clear()
        students_birth = []
        for i in range(len(self.student_births)):
            students_birth.append({"Student's ID":student_ids[i], "Student's name":student_names[i], f"{student_names[i]}'s Birth": self.student_births[i]})
        self.stdscr.addstr(0, 0, f"Students' info: {students_birth}")
        self.stdscr.addstr(2, 0, "Press any key to go back...")
        self.stdscr.getch()

        return self.student_births

class list_student:
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
    def studentList(self, num_students, student_ids, student_names, student_births):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== LIST OF STUDENTS ===\n\n")

        for i in range(num_students):
            line = f"{i+1}. ID: {student_ids[i]} | Name: {student_names[i]} | Birth: {student_births[i]}"
            self.stdscr.addstr(i + 2, 0, line)

        self.stdscr.addstr(num_students + 4, 0, "Press any key to go back...")
        self.stdscr.getch()

        return []
