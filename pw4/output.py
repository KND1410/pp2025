import curses

def output(stdscr, course_list, student_list, mark_info):
    """Module for curses output - chỉ hiển thị kết quả"""
    stdscr.clear()
    stdscr.getch()
    stdscr.refresh()
    stdscr.clear()
    
    row = 0
    
    stdscr.addstr(row, 0, "="*40 + "ALL MARKS" + "="*40)
    row += 2
    
    for course_name, students in mark_info.items():
        stdscr.addstr(row, 0, "-"*10 + f"MARK OF {course_name}" + "-"*10)
        row += 1
        for student_id, mark in students.items():
            for student in student_list.info:
                if student['ID'] == student_id:
                    stdscr.addstr(row, 2, f"{student['Name']}'s mark: {mark}")
                    row += 1
                    break
        row += 1

    stdscr.addstr(row, 0, "="*40 + "GPA" + "="*40)
    row += 2
    
    stdscr.addstr(row + 2, 0, "Press any key to exit...")
    stdscr.refresh()
    
    curses.echo()
    curses.noecho()