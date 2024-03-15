import math
import numpy as np
import pandas as pd

class Student:
    def __init__(self, ID, name, dob):
        self.student_ID = ID
        self.student_name = name
        self.student_dob = dob
        self.student_mark = {}
        self.mark_array = []
        self.gpa = {}

    def get_mark(self, course_ID, mark):
        self.course_ID = course_ID
        self.student_mark[course_ID] = mark
        self.mark_array.append(mark)

class Course:
    def __init__(self, ID, name, credit):
        self.course_ID = ID
        self.course_name = name
        self.course_credit = credit

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
        course_credit = int(input("Enter the course_credit: "))
        return Course(course_ID, course_name, course_credit)

    def list_courses(self):
        print("List of all courses: \n")
        for index, c in enumerate(self.course_list):
            print(f"|No: {index+1}\t|Course_ID: {c.course_ID}\t|Course_name: {c.course_name}\t|Course_credit: {c.course_credit}")

    def list_students(self):
        print("List of all students: \n")
        for index, s in enumerate(self.student_list):
            print(f"|No: {index+1}\t|Student_ID: {s.student_ID}\t|Student_name: {s.student_name} \t|Student_dob: {s.student_dob}")

    def select_course(self):
        print("Select a course below:\n")
        self.list_courses()
        choice = int(input(f"Please enter the course ith(1-{len(self.course_list)}) you want: "))
        if 1 <= choice <= len(self.course_list):
            return self.course_list[choice - 1]
        else:
            print("Course not found")
    
    def select_student(self):
        print("Select a student below: \n")
        self.list_students()
        choice = int(input(f"Please enter the student ith(1-{len(self.student_list)}) you want: "))
        if 1 <= choice <= len(self.student_list):
            return self.student_list[choice - 1]
        else:
            print("Student not found")

    def show_student_marks(self, course):
        course_ID = course.course_ID
        print(f"Show marks for students in course {course_ID}:\n")
        for s in self.student_list:
            marks = s.student_mark.get(course_ID)
            if marks:
                print(f"Student ID: {s.student_ID}, Name: {s.student_name}, Marks: {marks}")
            else:
                print(f"Student ID: {s.student_ID}, Name: {s.student_name}, Marks: N/A")

    def input_mark(self):
        student_ID = input("Enter the student_ID: ")
        course_ID = input("Enter the course_ID: ")
        mark_input = float(input("Enter the mark: "))
        mark_input_rounded = math.floor(mark_input*10)/10
        for s in self.student_list:
            if s.student_ID == student_ID:
                s.get_mark(course_ID, mark_input_rounded)
                print("Mark is added successfully")
                break
        else:
            print("Not found student in the list")
        

    def calculate_gpa(self):  
        total_credits = np.sum(course.course_credit for course in self.course_list )
        selected_student = self.select_student()
        if selected_student:
            print(f"Selected student: {selected_student.student_ID} || {selected_student.student_name}") 
        for student in self.student_list:
            if student.student_ID == selected_student.student_ID:
                weighted_mark = np.array(student.mark_array) * np.array([course.course_credit for course in self.course_list])
                weighted_sum = np.sum(weighted_mark)
                gpa = float(weighted_sum / total_credits)
                student.gpa = gpa
        print(gpa)

    def sort_gpa(self):
        gpa_array = pd.DataFrame([student.__dict__ for student in self.student_list])
        gpa_array_sorted = gpa_array.sort_values(by='gpa', ascending=True)
        # for stud in gpa_array_sorted:
        #     print(f"Student ID: {stud.student_ID}\t||Student name: {stud.student_name}\t||Student dob: {stud.student_dob}")
        for index, stud in gpa_array_sorted.iterrows():
            print(f"Student ID: {stud['student_ID']}\t||Student name: {stud['student_name']}\t||Student dob: {stud['student_dob']}")

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
                  5. Show student average GPA
                  6. List all students order by GPA
                  7. Exit
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
                self.calculate_gpa()
            elif option == 6:
                self.sort_gpa()
            elif option == 7:
                print("Successful exit")
                break
            else:
                print("Invalid option")


manage_system = Manage_Student_Course()
manage_system.main()
