import os
import math
import numpy

class Init():
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def __str__(self):
        return f'ID: {self._id} - Name: {self._name}'

class Student(Init):
    def __init__(self, id, name, dob): 
        super().__init__(id, name)
        self._dob = dob
        self._mark = numpy.array([])
        self._gpa = None
    def __str__(self):
        return f'{super().__str__()} - DoB: {self._dob}'
    def student_number():
        while (True):
            student_num = int(input("Enter number of students: "))
            if student_num > 0:
                print(f'\nThe number of students is {student_num}')
                break
            else:
                print("Invalid input! Try again\n")
        return student_num
    def student_information(student_num):
        if student_num == 0:
            print("There are currently no students\n")
            return None
        student_info = []
        for i in range(student_num):
            print(f'Student {i+1}: ')
            id = input("Enter ID: ")
            name = input("Enter name: ")
            dob = input("Enter DoB: ")
            print("")
            student = Student(id, name, dob) 
            student_info.append(student)
        return student_info
    def student_list(student, student_num):
        if not student:
            print("There are currently no students")
            return None
        else:
            print("Student list:")
            for i in range (student_num):
                print(f'{i+1}. {student[i]}')
    def student_mark(course_num, student, student_num):
        if course_num == 0 or student_num == 0:
            return None
        else:
            for i in range (course_num):
                print(f'\nCourse {i+1}:')
                for j in range (student_num):
                    student[j]._mark = numpy.append(student[j]._mark, float(input(f'Enter mark for student {j+1}: ')))
    def show_student_mark(course, course_num, student, student_num):
        if not course:
            return None
        else:
            for i in range (course_num):
                print(f'\nCourse {i+1}:')
                for j in range (student_num):
                    print(f"Student {j+1}'s mark: {math.floor(student[j]._mark[i])}")
    def cal_gpa(student, student_num, course, course_num):
        if not student:
            print("There are currently no students")
            return None
        else:
            print("List students by GPA:")
            for i in range (student_num):
                sum = 0
                sum_credit = 0
                for j in range (course_num):
                    sum += student[i]._mark[j] * course[j]._credit
                    sum_credit += course[j]._credit
                student[i]._gpa = sum / sum_credit
                print(f'{i+1}. {student[i]} - GPA: {round(student[i]._gpa, 2)}')   

class Course(Init):
    def __init__(self, id, name, credit):
        super().__init__(id, name)
        self._credit = credit
    def __str__(self):
        return f'{super().__str__()} - Credit: {self._credit}'
    def course_number():
        while (True):
            course_num = int(input("Enter number of courses: "))
            if course_num > 0:
                print(f'\nThe number of courses is {course_num}')
                break
            else:
                print("Invalid input! Try again\n")
        return course_num
    def course_information(course_num):
        if course_num == 0:
            print("There are currently no courses\n")
        course_info = []
        for i in range(course_num):
            print(f'Course {i+1}: ')
            id = input("Enter ID: ")
            name = input("Enter name: ")
            credit = int(input("Enter credit: "))
            print("")
            course = Course(id, name, credit) 
            course_info.append(course)
        return course_info
    def course_list(course, course_num):
        if not course:
            print("\nThere are currently no courses\n")
            return None
        else:
            print("Course list:")
            for i in range (course_num):
                print(f'{i+1}. {course[i]}')

def clear():
    print("")
    os.system("pause")
    os.system("cls")

def main():
    student = []
    course = []
    student_num = 0
    course_num = 0
    
    while (True):
        print("""
===========================================================
1. Input number of students in a class
2. Input student information: id, name, DoB
3. Input number of courses
4. Input course information: id, name, credit
5. Select a course, input marks for student in this course
6. List courses
7. List students
8. Show student marks for a given course
9. List students by GPA in descending order
0. Exit the program 
===========================================================""")

        option = int(input("Choose an option: "))
        if option == 0:
            os.system("cls")
            print("""
You have exited the program
GOODBYE!""")
            exit(0)
        elif option == 1:
            os.system("cls")
            student_num = Student.student_number()
            clear()
        elif option == 2:
            os.system("cls")
            student = Student.student_information(student_num)
            clear()
        elif option == 3:
            os.system("cls")
            course_num = Course.course_number()
            clear()
        elif option == 4:
            os.system("cls")
            course = Course.course_information(course_num)
            clear()
        elif option == 5:
            os.system("cls")
            Student.student_list(student, student_num)
            Course.course_list(course, course_num)
            Student.student_mark(course_num, student, student_num)
            clear()
        elif option == 6:
            os.system("cls")
            Course.course_list(course, course_num)
            clear()
        elif option == 7:
            os.system("cls")
            Student.student_list(student, student_num)
            clear()
        elif option == 8:
            os.system("cls")
            Course.course_list(course, course_num)
            Student.show_student_mark(course, course_num, student, student_num)
            clear()
        elif option == 9:
            os.system("cls")
            Student.cal_gpa(student, student_num, course, course_num)
            clear()
if __name__ == "__main__":
    main()