import pickle
import os
import gzip

class infoManager:
    def __init__(self, stdscr):
        self.stdscr = stdscr

        self.num_students = 0
        self.student_ids = []
        self.student_names = []
        self.student_births = []
        
        self.num_courses = 0
        self.course_ids = []
        self.course_names = []
        self.course_credits = []
        
        self.marks = []
    
    def load_infomation(self):
            with open("students.dat", "rb") as f:
                data = pickle.load(f)
            
            self.num_students = data["num_students"]
            self.student_ids = data["student_ids"]
            self.student_names = data["student_names"]
            self.student_births = data["student_births"]
            self.num_courses = data["num_courses"]
            self.course_ids = data["course_ids"]
            self.course_names = data["course_names"]
            self.course_credits = data["course_credits"]
            self.marks = data["marks"]
            
            self.stdscr.addstr(3, 0, f"Loaded {data['num_students']} students")
            self.stdscr.addstr(4, 0, f"Loaded {data['num_courses']} courses")
            self.stdscr.addstr(5, 0, f"Loaded {len(data['marks'])} marks")
            self.stdscr.addstr(6, 0, "="*60)
            self.stdscr.addstr(8, 0, "Press any key to continue...")
            self.stdscr.refresh()
            self.stdscr.getch()

    def show_data(self):

        self.stdscr.clear()
        line = 0
        
        try:
            if os.path.exists("students.dat.gz"):
                self.stdscr.addstr(line, 0, "No data available. Please enter student/course/mark data first.")
                line += 2
                self.stdscr.addstr(line, 0, "Press any key...")
                self.stdscr.getch()
                return
            else:
                self.stdscr.addstr(line, 0, "=== ALL MARKS WITH STUDENT INFO ===")
                line += 1
                
                for mark in self.marks:
                    student_name = mark.get("Student's name", "N/A")
                    course_name = mark.get("Course", "N/A")
                    score = mark.get("Mark", "N/A")
                    
                    student_id = "N/A"
                    for i, name in enumerate(self.student_names):
                        if name == student_name:
                            student_id = self.student_ids[i]
                            break

                    self.stdscr.addstr(line, 0, f"Student: {student_name} - ID: {student_id} - Course: {course_name} - Mark: {score}")
                    line += 1
                
                line += 1
                self.stdscr.addstr(line, 0, "Press any key...")
                self.stdscr.getch()
        except FileNotFoundError:
            print("File not found")