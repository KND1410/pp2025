import numpy as np


def output(stdscr, course_list, student_list, mark_info):
    stdscr.clear()
    row = 0

    stdscr.addstr(row, 0, "=" * 40 + "ALL MARKS" + "=" * 40)
    row += 2

    for course_name, students in mark_info.items():
        stdscr.addstr(row, 0, "-" * 10 + f"MARK OF {course_name}" + "-" * 10)
        row += 1
        for student_id, mark in students.items():
            for student in student_list.info:
                if student['ID'] == student_id:
                    stdscr.addstr(row, 2, f"{student['Name']}'s mark: {mark}")
                    row += 1
                    break
        row += 1

    row += 1
    stdscr.addstr(row, 0, "=" * 40 + "GPA" + "=" * 40)
    row += 2

    num_courses = len(course_list.info)
    num_students = len(student_list.info)

    marks_array = np.zeros((num_courses, num_students))
    credits_array = np.zeros(num_courses)

    for i in range(num_courses):
        course = course_list.info[i]
        course_name = course['Name']
        credits_array[i] = course.get('Credit', 0)

        if course_name in mark_info:
            for j in range(num_students):
                student = student_list.info[j]
                student_id = student['ID']
                if student_id in mark_info[course_name]:
                    marks_array[i, j] = mark_info[course_name][student_id]

    student_gpas = []
    for j in range(num_students):
        student = student_list.info[j]
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

    for name, gpa in student_gpas:
        stdscr.addstr(row, 2, f"{name}: {gpa:.2f}")
        row += 1

    stdscr.addstr(row + 1, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

    return student_gpas
