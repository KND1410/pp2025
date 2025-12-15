from domains import curses

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