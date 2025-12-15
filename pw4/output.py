from domains import curses
from main import main

def main_program(stdscr):
    m = main()
    m.course_list.input(stdscr)
    m.student_list.input(stdscr)
    m.mark(stdscr)

if __name__ == "__main__":
    curses.wrapper(main_program)