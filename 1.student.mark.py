def enter_number_of_student():
    number_student = int(input("Enter number of students: "))
    if number_student <= 0:
        print("Invalid input, please enter a positive number")
        return enter_number_of_student()
    else:
        return number_student
def enter_student_infor():
    student_infor = {
        "StudentID": input("Enter student ID: "),
        "Student Name": input("Enter student name: "),
        "Date of birth": input("Enter student DOB: ")
    }
    return student_infor
def enter_number_of_course():
    number_course = int(input("Enter number of courses: "))
    if number_course <= 0:
        print("Invalid input, please enter a positive number")
        return enter_number_of_course()
    else:
        return number_course
def enter_course_infor():
    course_infor = {
        "CourseID": input("Enter course ID: "),
        "Course Name": input("Enter course name: ")
    }
    return course_infor
def select_course(courses):
    print("Select a course below:")
    for index, course in enumerate(courses):
        print(f"{index+1}. CourseID: {course['CourseID']} - Course Name: {course['Course Name']}")
    choice = int(input("Please enter the course number you want: "))
    if 1 <= choice <= len(courses):
        return courses[choice - 1]
    else:
        print("Invalid course")
def list_courses(courses):
    print("--------------------------------------------")
    print("List of courses:")
    if courses == []:
        print("There is no course information")
    for course in courses:
        print(f"Course ID: {course['CourseID']}, Name: {course['Course Name']}")
def list_student(students):
    print("--------------------------------------------")
    print("List of students:")
    if students == []:
        print("There is no student information")
    for student in students:
        print(f"Student ID: {student['StudentID']}, Name: {student['Student Name']}, Date of birth: {student['Date of birth']}")
def show_student_marks(students, course):
    course_id = course['CourseID']
    print(f"Showing marks for students in course {course_id}:\n")
    for student in students:
        marks = student.get(course_id)
        if marks:
            print(f"Student ID: {student['StudentID']}, Name: {student['Student Name']}, Marks: {marks}")
        else:
            print(f"Student ID: {student['StudentID']}, Name: {student['Student Name']}, Marks: No information")
def add_student_marks(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    marks = float(input("Enter marks: "))

    for student in students:
        if student['StudentID'] == student_id:
            for course in courses:
                if course['CourseID'] == course_id:
                    student[course_id] = marks
                    print("Update score successfully")
                    return

    print("Student or course not found.")
def main():
    students = []
    courses = []
    number_of_students = enter_number_of_student()
    for i in range(0, number_of_students):
        student_info = enter_student_infor()
        students.append(student_info)
    number_of_courses = enter_number_of_course()
    for j in range(0, number_of_courses):
        course_info = enter_course_infor()
        courses.append(course_info)
    while True:
        print("""
              1. List all the courses
              2. List all the students
              3. Show student marks for a course
              4. Add marks for a student in a course
              5. OUT
              """)
        option = int(input("Enter your option number: "))
        if option == 1:
            list_courses(courses)
        elif option == 2:
            list_student(students)
        elif option == 3:
            selected_course = select_course(courses)
            print("Selected course:", selected_course)
            show_student_marks(students, selected_course)
        elif option == 4:
            add_student_marks(students, courses)
        elif option == 5:
            print("Sucessfull get out")
            break
        else:
            print("Invalid option")
        print("---------------------------------------------------------------")
main()