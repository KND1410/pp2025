import curses
from domains import Student, Course, math, np
from input import get_string
from output import output

class Main:
    def __init__(self):
        self.student_list = Student()
        self.course_list = Course()
        self.markInfo = {}
    
    def input_marks(self, stdscr):
        """Nhập điểm cho sinh viên"""
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
    
    def calculate_gpa(self):
        """Tính GPA cho sinh viên"""
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
        return student_gpas

def main_program(stdscr):
    """Main script for coordination"""
    m = Main()
    m.course_list.input(stdscr)
    m.student_list.input(stdscr)
    m.input_marks(stdscr)
    student_gpas = m.calculate_gpa()
    output(stdscr, m.course_list, m.student_list, m.markInfo, student_gpas)

if __name__ == "__main__":
    curses.wrapper(main_program)