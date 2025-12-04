def input_student_number():
    number = "no"
    while not number.isnumeric():
        number = input("Enter number of students: ")
    return int(number)

def input_student_info(student_list):
    number_student = input_student_number()
    for i in range(number_student):
        student_id = input("Enter student id: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student DoB: ")
        student_list.append({
            "id": student_id,
            "name": student_name,
            "dob": student_dob
        })

def list_student(student_list):
    for student in student_list:
        print(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['dob']}")

def input_course_number():
    number = "no"
    while not number.isnumeric():
        number = input("Enter number of courses: ")
    return int(number)

def input_course_info(course_list):
    number_course = input_course_number()
    for i in range(number_course):
        course_id = input("Enter course id: ")
        course_name = input("enter course name: ")
        course_list.append({
            "id": course_id,
            "name": course_name,
            "marks": {}
        })

def list_course(course_list):
    for course in course_list:
        print(f"ID: {course['id']} | Name: {course['name']}")

def input_student_mark(course_list, student_list):
    course_name = input("Enter course name to input marks: ")
    selected_course = None
    for course in course_list:
        if course['name'] == course_name:
            selected_course = course
            break
    
    if selected_course is None:
        print("Course not found.")
        return

    for student in student_list:
        mark = input(f"Enter mark for {student['name']}: ")
        if mark.isnumeric():
            selected_course['marks'][student['id']] = float(mark)

def show_marks(course_list):
    course_name = input("Enter course name to view marks: ")
    for course in course_list:
        if course['name'] == course_name:
            print(f"Marks for {course_name}:")
            for student_id, mark in course['marks'].items():
                print(f"Student ID {student_id}: {mark}")
            return
    print("Course not found.")

students = []
courses = []

input_student_info(students)
list_student(students)

input_course_info(courses)
list_course(courses)

input_student_mark(courses, students)
show_marks(courses)