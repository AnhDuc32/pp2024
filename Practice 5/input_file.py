from Domains.student import Student
from Domains.course import Course
import numpy

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
    f = open('students.txt', 'w')
    student_info = []
    for i in range(student_num):
        print(f'Student {i+1}: ')
        id = input("Enter ID: ")
        name = input("Enter name: ")
        dob = input("Enter DoB: ")
        print("")
        student = Student(id, name, dob) 
        student_info.append(student)
        f.write(f'{(student)}\n')
    f.close()
    return student_info
def student_mark(course_num, student, student_num):
    if course_num == 0 or student_num == 0:
        return None
    else:
        f = open('marks.txt', 'w')
        for i in range (student_num):
            student[i]._mark = numpy.array([])
        for c in range (course_num):
            f.write(f'Course {c+1}:\n')
            print(f'\nCourse {c+1}:')
            for j in range (student_num):
                student[j]._mark = numpy.append(student[j]._mark, float(input(f'Enter mark for student {j+1}: ')))
                f.write(f'{(student[j])} - Mark: {(student[j]._mark[c])}\n')
        f.close()

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
    f = open('courses.txt', 'w')
    course_info = []
    for i in range(course_num):
        print(f'Course {i+1}: ')
        id = input("Enter ID: ")
        name = input("Enter name: ")
        credit = int(input("Enter credit: "))
        print("")
        course = Course(id, name, credit) 
        course_info.append(course)
        f.write(f'{(course)}\n')
    f.close()
    return course_info