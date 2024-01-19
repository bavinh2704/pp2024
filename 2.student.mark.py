class Student:
    def __init__(self, ID, name, dob):
        self.student_ID = ID
        self.student_name = name
        self.student_dob = dob
        self.mark = {}

    def get_mark(self, course_ID, mark):
        self.course_ID = course_ID
        self.mark[course_ID] = mark


class Course:
    def __init__(self, ID, name):
        self.course_ID = ID
        self.course_name = name


def enter_number_of_student():
    number_student = int(input("Enter number of students: "))
    if number_student <= 0:
        print("Invalid input, please enter a positive number")
        return enter_number_of_student()
    else:
        return number_student


def enter_number_of_course():
    number_course = int(input("Enter number of courses: "))
    if number_course <= 0:
        print("Invalid input, please enter a positive number")
        return enter_number_of_course()
    else:
        return number_course


class Manage_Student_Course:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def input_student_infor(self):
        student_ID = input("Enter the student_ID: ")
        student_name = input("Enter the student_name: ")
        student_dob = input("Enter the student_dob: ")
        return Student(student_ID, student_name, student_dob)

    def input_course_infor(self):
        course_ID = input("Enter the course_ID: ")
        course_name = input("Enter the course_name: ")
        return Course(course_ID, course_name)

    def list_courses(self):
        print("List of all courses: \n")
        for c in self.course_list:
            print(f"|Course_ID: {c.course_ID}|Course_name: {c.course_name}")

    def list_students(self):
        print("List of all students: \n")
        for s in self.student_list:
            print(f"|Student_ID: {s.student_ID}|Student_name: {s.student_name}|Student_dob: {s.student_dob}")

    def select_course(self):
        print("Select a course below:\n")
        self.list_courses()
        choice = int(input("Please enter the course number you want: "))
        if 1 <= choice <= len(self.course_list):
            return self.course_list[choice - 1]
        else:
            print("Course not found")

    def show_student_marks(self, course):
        course_ID = course.course_ID
        print(f"Show marks for students in course {course_ID}:\n")
        for s in self.student_list:
            marks = s.mark.get(course_ID)
            if marks:
                print(f"Student ID: {s.student_ID}, Name: {s.student_name}, Marks: {marks}")
            else:
                print(f"Student ID: {s.student_ID}, Name: {s.student_name}, Marks: N/A")

    def input_mark(self):
        student_ID = input("Enter the student_ID: ")
        course_ID = input("Enter the course_ID: ")
        mark_input = float(input("Enter the mark: "))

        for s in self.student_list:
            if s.student_ID == student_ID:
                s.get_mark(course_ID, mark_input)
                print("Mark is added successfully")
                break
        else:
            print("Not found student in the list")

    def main(self):
        number_student = enter_number_of_student()
        number_course = enter_number_of_course()

        for i in range(number_student):
            student_infor = self.input_student_infor()
            self.student_list.append(student_infor)

        for j in range(number_course):
            course_infor = self.input_course_infor()
            self.course_list.append(course_infor)

        while True:
            print("""
                  1. List all the courses
                  2. List all the students
                  3. Show student marks for a course
                  4. Add marks for a student in a course
                  5. Exit
                  """)
            option = int(input("Enter your option number: "))

            if option == 1:
                self.list_courses()
            elif option == 2:
                self.list_students()
            elif option == 3:
                selected_course = self.select_course()
                if selected_course:
                    print(f"Selected course: {selected_course.course_ID} || {selected_course.course_name}")
                    self.show_student_marks(selected_course)
            elif option == 4:
                self.input_mark()
            elif option == 5:
                print("Successful exit")
                break
            else:
                print("Invalid option")


manage_system = Manage_Student_Course()
manage_system.main()
