import curses
import math
import numpy as np
from input import get_string

class mark_student:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.gpa = []
        self.marks = []
        self.markInfo = {}
    def markEnter(self, num_courses, student_names, course_names, course_ids, course_credits, num_students, student_ids, student_births):
        if num_courses == 0 or not course_ids or len(course_ids) == 0 or not course_names or len(course_names) == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please go to option \"Course\" and enter the all of the course\'s detail!")
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []
        
        elif num_students == 0 or not student_ids or len(student_ids) == 0 or not student_names or len(student_names) == 0 or not student_births or len(student_births) == 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please go to option \"Student\" and enter the all of the student\'s detail!")
            self.stdscr.addstr(1, 0, "Press any key to go back")
            self.stdscr.getch()
            return []

        self.stdscr.clear()
        line = 0

        student_marks = []
        for s in range(num_students):
            student_marks.append({})

        for c in range(num_courses):
            while True:
                finding = get_string(self.stdscr, f"Enter the course #{c+1}: ", line, 0)
                line +=1

                if finding in course_names:
                    self.stdscr.addstr(line, 0, f"=== ENTER {student_names[s]} MARK OF {finding} ===\n\n")
                    for s in range(num_students):
                        mark = math.floor(float(get_string(self.stdscr, f"{student_names[s]}'s mark of {finding}: ", line+1, 2))*10)/10
                        student_marks[s][finding] = mark

                        self.marks.append({"Student's name": student_names[s], "Course": finding, "Mark": mark})
                        line += 3
                    break
                else:
                    self.stdscr.addstr(line, 0, "There are no course, course available: ")
                    line+=1

                    for name in course_names:
                        self.stdscr.addstr(line, 2, f"- {name}")
                        line += 1

        for s in range(num_students):
            marks_array = []
            credits_array = []
            
            for course in student_marks[s]:
                for i in range(len(course_names)):
                    if course_names[i] == course:
                        marks_array.append(student_marks[s][course])
                        credits_array.append(float(course_credits[i]))
                        break
            
            if len(marks_array) > 0:
                marks_np = np.array(marks_array)
                credits_np = np.array(credits_array)
                
                total_mark = np.sum(marks_np * credits_np)
                total_credits = np.sum(credits_np)
                
                if total_credits > 0:
                    gpa = total_mark / total_credits
                else:
                    gpa = 0
            else:
                gpa = 0
            
            self.gpa.append(gpa)

        student_gpa_list = list(zip(student_names, self.gpa))
        sorted_student_gpa = sorted(student_gpa_list, key=lambda x: x[1], reverse=True)

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== GPA OF ALL STUDENTS (Sorted Descending) ===\n\n")
        for i in range(len(sorted_student_gpa)):
            name, gpa = sorted_student_gpa[i]
            self.stdscr.addstr(i+2, 0, f"{name}: {gpa:.2f}")
        
        self.stdscr.addstr(len(sorted_student_gpa) + 3, 0, "Press any key to go back...")
        self.stdscr.getch()
        return self.marks