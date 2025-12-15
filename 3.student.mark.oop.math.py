import math
import numpy as np
import curses

def get_string(stdscr, prompt, row, col):
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()

    curses.echo()
    input_string = stdscr.getstr(row, col + len(prompt), 20)
    curses.noecho()

    return input_string.decode('utf-8')

class Student:
    def __init__(self, numberStudent = 0, id = " ", name = " ", birth = " "):
        self.numberStudent = numberStudent
        self.__id = id
        self.__name = name
        self.__birth = birth
        self.info = []

    def _get_numberStudent(self):
        return self.numberStudent
    def _get_ID(self):
        return self.__id
    def _get_name(self):
        return self.__name
    def _get_birth(self):
        return self.__birth

    def input(self, stdscr):
        stdscr.clear()
        self.numberStudent = int(get_string(stdscr, "Enter the number of students: ", 0, 0))
        self.info = []

        for i in range(1, self.numberStudent+1):
            base_row = i * 4 + 1
            self.id = str(get_string(stdscr, f"Enter the student #{i} id: ", base_row, 0))
            self.name = str(get_string(stdscr, f"Enter the name of the student ({self.id}): ", base_row+1, 0))
            self.birth = int(get_string(stdscr, f"Enter birthday of {self.name}: ", base_row+2, 0))
            self.info.append({"Name": self.name, "ID": self.id, "Birth": self.birth})
            
class Course:
    def __init__(self, numberCourse = 0, id = " ", name = " ", credit = " "):
        self.numberCourse = numberCourse
        self.__id = id
        self.__name = name
        self.__credit = credit
        self.info = []

    def _get_numberCourse(self):
        return self.numberCourse
    def _get_id(self):
        return self.__id
    def _get_name(self):
        return self.__name
    def _get_credit(self):
        return self.__credit
        
    def input(self, stdscr):
        stdscr.clear()
        self.numberCourse = int(get_string(stdscr, "Enter the number of courses: ", 0, 0))
        self.info = []
        for i in range(1, self.numberCourse+1):
            base_row = i * 4 + 1
            self.id = str(get_string(stdscr, f"Enter the course ID #{i}: ", base_row, 0))
            self.name = str(get_string(stdscr, f"Enter the course's name ({i}): ", base_row+1, 0))
            self.credit = int(get_string(stdscr, f"Enter the credit for {self.name}: ", base_row+2, 0))
            self.info.append({"Name": self.name, "Credit": self.credit, "ID": self.id})

class main(Student, Course):
    def __init__(self):
        self.student_list = Student()
        self.course_list = Course()
        self.markInfo = {}

    def mark(self, stdscr):
        stdscr.clear()
        for i in range(len(self.course_list.info)):
            base_row = i * 6 + 1
            while True:
                finding = get_string(stdscr, f"Enter the course #{i+1}: ", base_row, 0)
                course_names = [c['Name'] for c in self.course_list.info]
                
                if finding in course_names:
                    if finding not in self.markInfo:
                        self.markInfo[finding] = {}
                    
                    j = 0
                    for student in self.student_list.info:
                        mark = math.floor(float(get_string(stdscr, f"{student['Name']}'s mark: ", base_row+1+j, 2))*10)/10
                        self.markInfo[finding][student['ID']] = mark
                        j += 1
                    break
                else:
                    stdscr.addstr(base_row+1, 0, "There are no course, course available: ")
                    k = 0
                    for c in self.course_list.info:
                        stdscr.addstr(base_row+2+k, 2, f"{c['ID']} - {c['Name']}")
                        k += 1
        stdscr.clear()
        row = 0
        
        stdscr.addstr(row, 0, "="*40 + "ALL MARKS" + "="*40)
        row += 2

        for course_name, students in self.markInfo.items():
            stdscr.addstr(row, 0, "-"*10 + f"MARK OF {course_name}" + "-"*10)
            row += 1

            for student_id, mark in students.items():
                for student in self.student_list.info:
                    if student['ID'] == student_id:
                        stdscr.addstr(row, 2, f"{student['Name']}'s mark: {mark}")
                        row += 1
                        break
            row += 1

        stdscr.addstr(row, 0, "="*40 + "GPA" + "="*40)
        row += 2
 
        num_courses = len(self.course_list.info)
        num_students = len(self.student_list.info)

        marks_array = np.zeros((num_courses, num_students))

        credits_array = np.zeros(num_courses)

        for i in range(num_courses):
            course = self.course_list.info[i]
            course_name = course['Name']
            credits_array[i] = course['Credit']
            
            if course_name in self.markInfo:
                for j in range(num_students):
                    student = self.student_list.info[j]
                    student_id = student['ID']
                    
                    if student_id in self.markInfo[course_name]:
                        marks_array[i, j] = self.markInfo[course_name][student_id]

        student_gpas = []
        
        for j in range(num_students):
            student = self.student_list.info[j]
            student_name = student['Name']

            student_marks = marks_array[:, j]

            weighted_sum = np.dot(student_marks, credits_array)
            total_credits = np.sum(credits_array)
            
            if total_credits > 0:
                gpa = weighted_sum / total_credits
            else:
                gpa = 0
            
            student_gpas.append((student_name, gpa))

        student_gpas.sort(key=lambda x: x[1], reverse=True)

        for name, gpa in student_gpas:
            stdscr.addstr(row, 2, f"{name}'s GPA: {gpa:.2f}")
            row += 1
        
        stdscr.addstr(row + 2, 0, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()

def main_program(stdscr):
    m = main()
    m.course_list.input(stdscr)
    m.student_list.input(stdscr)
    m.mark(stdscr)

if __name__ == "__main__":
    curses.wrapper(main_program)