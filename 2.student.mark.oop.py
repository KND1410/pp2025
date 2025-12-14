class Student:
    def __init__(self, numberStudent = 0, id = " ", name = " ", birth = " "):
        self.numberStudent = numberStudent
        self.__id = id
        self.__name = name
        self.__birth = birth
    def _get_numberStudent(self):
        return self.numberStudent
    def _get_ID(self):
        return self.__id
    def _get_name(self):
        return self.__name
    def _get_birth(self):
        return self.__birth
    def input(self):
        self.numberStudent = int(input("Enter the number of students: "))
        self.info = []
        for i in range(1, self.numberStudent+1):
            self.id = str(input(f"Enter the student #{i} id: "))
            self.name = str(input(f"Enter the name of the student ({self.id}): "))
            self.birth = int(input(f"Enter birthday of {self.name}: "))
            self.info.append({"Name": self.name, "ID": self.id, "Birth": self.birth})

class Course:
    def __init__(self, numberCourse = 0, id = " ", name = " "):
        self.numberCourse = numberCourse
        self.__id = id
        self.__name = name
    def _get_numberCourse(self):
        return self.numberCourse
    def _get_id(self):
        return self.__id
    def _get_name(self):
        return self.__name
    def input(self):
        self.numberCourse = int(input("Enter the number of courses: "))
        self.info = []
        for i in range(1, self.numberCourse+1):
            self.id = str(input(f"Enter the course ID #{i}: "))
            self.name = str(input(f"Enter the course's name ({i}): "))
            self.info.append({"Name": self.name, "ID": self.id})

class main(Student, Course):
    def __init__(self):
        self.student_list = Student()
        self.course_list = Course()
        self.markInfo = {}

    def mark(self):
        for i in range(len(self.course_list.info)):
            while True:
                finding = input(f"Enter the course #{i+1}: ")
                course_names = [c["Name"] for c in self.course_list.info]
                
                if finding in course_names:
                    if finding not in self.markInfo:
                        self.markInfo[finding] = {}
                    
                    for student in self.student_list.info:
                        mark = float(input(f"{student['Name']}'s mark: "))
                        self.markInfo[finding][student['ID']] = mark
                    break
                else:
                    print("There are no course, course available: ")
                    for c in self.course_list.info:
                        print(f"{c['ID']} - {c['Name']}")
    

        print("\n" + "="*40)
        print("ALL MARKS")
        print("="*40)
        for course_name, students in self.markInfo.items():
            print("-"*10 + f"MARK OF {course_name}" + "-"*10)
            for student_id, mark in students.items():
                for student in self.student_list.info:
                    if student['ID'] == student_id:
                        print(f"{student['Name']}'s mark: {mark}")
                        break
            print()

m = main()
m.course_list.input()
m.student_list.input()
m.mark()