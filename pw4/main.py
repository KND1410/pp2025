import curses
from domains import Student, Course
import input
import output


class Main:
    def __init__(self):
        self.student_list = Student()
        self.course_list = Course()
        self.markInfo = {}


def main(stdscr):
    m = Main()
    m.course_list.input(stdscr)
    m.student_list.input(stdscr)
    input.input_marks(m, stdscr)
    output.output(stdscr, m.course_list, m.student_list, m.markInfo)


if __name__ == "__main__":
    curses.wrapper(main)