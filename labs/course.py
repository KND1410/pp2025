import curses
from input import get_string


class number_course:
    def __init__(self, stdscr):
        self.num_courses = 0
        self.stdscr = stdscr

    def numberCourse(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== ENTER NUMBER OF COURSES ===\n\n")

        s = get_string(self.stdscr, "Enter number of courses: ", 2, 0)
        try:
            self.num_courses = int(s)
        except ValueError:
            self.stdscr.addstr(4, 0, "Invalid number. Press any key...")
            self.stdscr.getch()
            return 0

        self.stdscr.addstr(4, 0, f"Number of courses: {self.num_courses}")
        self.stdscr.addstr(6, 0, "Press any key to continue...")
        self.stdscr.getch()
        return self.num_courses

class course_iD:
    def __init__(self, stdscr):
        self.course_ids = []
        self.stdscr = stdscr

    def courseID(self, num_courses):
        if num_courses <= 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter number of courses first.")
            self.stdscr.getch()
            return []

        self.course_ids = []

        for i in range(num_courses):
            self.stdscr.clear()
            self.stdscr.addstr(
                0, 0,
                f"=== ENTER COURSE ID ({i+1}/{num_courses}) ===\n\n"
            )
            cid = get_string(self.stdscr, f"Course ID {i+1}: ", 2, 0)
            self.course_ids.append(cid)

        return self.course_ids

class course_name:
    def __init__(self, stdscr):
        self.course_names = []
        self.stdscr = stdscr

    def courseName(self, num_courses, course_ids):
        if num_courses <= 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter number of courses first.")
            self.stdscr.getch()
            return []

        if not course_ids:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter course IDs first.")
            self.stdscr.getch()
            return []

        self.course_names = []

        for i in range(num_courses):
            self.stdscr.clear()
            self.stdscr.addstr(
                0, 0,
                f"=== ENTER COURSE NAME ({i+1}/{num_courses}) ===\n\n"
            )
            cname = get_string(self.stdscr, f"Course name {i+1}: ", 2, 0)
            self.course_names.append(cname)

        return self.course_names
    
class course_credit:
    def __init__(self, stdscr):
        self.course_credit = []
        self.stdscr = stdscr

    def courseCredit(self, num_courses, course_ids, course_names):
        if num_courses <= 0:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter number of courses first.")
            self.stdscr.getch()
            return []

        if not course_ids:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter course IDs first.")
            self.stdscr.getch()
            return []
        
        if not course_names:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Please enter courses name first.")
            self.stdscr.getch()
            return []

        self.course_credit = []

        for i in range(num_courses):
            self.stdscr.clear()
            self.stdscr.addstr(
                0, 0,
                f"=== ENTER COURSE CREDITS ({course_names[i]}) ===\n\n"
            )
            ccredit = float(get_string(self.stdscr, f"Course credit of {course_names[i]}: ", 2, 0))
            self.course_credit.append(ccredit)

        return self.course_credit

class list_course:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def courseList(self, num_courses, course_ids, course_names, course_credits):
        if num_courses <= 0 or not course_ids or not course_names or not course_credits:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, "Course data incomplete.")
            self.stdscr.getch()
            return []

        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "=== LIST OF COURSES ===\n\n")

        for i in range(num_courses):
            self.stdscr.addstr(
                i + 2, 0,
                f"{i+1}. ID: {course_ids[i]} | Name: {course_names[i]} | Credits: {course_credits[i]}"
            )

        self.stdscr.addstr(num_courses + 4, 0, "Press any key to go back...")
        self.stdscr.getch()
        return []