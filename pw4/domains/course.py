import curses
from input import get_string

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