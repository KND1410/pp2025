import curses
from input import get_string

class Student:
    def __init__(self, numberStudent=0, id=" ", name=" ", birth=" "):
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
            student_id = str(get_string(stdscr, f"Enter the student #{i} id: ", base_row, 0))
            name = str(get_string(stdscr, f"Enter the name of the student ({student_id}): ", base_row+1, 0))
            birth = int(get_string(stdscr, f"Enter birthday of {name}: ", base_row+2, 0))
            self.info.append({"Name": name, "ID": student_id, "Birth": birth})