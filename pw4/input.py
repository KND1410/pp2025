import curses
import math

def get_string(stdscr, prompt, row, col):
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()

    curses.echo()
    input_string = stdscr.getstr(row, col + len(prompt), 20)
    curses.noecho()

    return input_string.decode('utf-8')

def input_marks(self, stdscr):
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
                    mark_str = get_string(stdscr, f"{student['Name']}'s mark: ", base_row+1+j, 2)
                    try:
                        mark = math.floor(float(mark_str) * 10) / 10
                    except ValueError:
                        mark = 0.0
                    self.markInfo[finding][student['ID']] = mark
                    j += 1
                break
            else:
                stdscr.addstr(base_row+1, 0, "There are no course, course available: ")
                k = 0
                for c in self.course_list.info:
                    stdscr.addstr(base_row+2+k, 2, f"{c['ID']} - {c['Name']}")
                    k += 1