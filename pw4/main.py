from domains import curses, math, np
from input import get_string, Student, Course

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