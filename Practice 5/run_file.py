import os
import input_file as i
import output_file as o

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
            student_num = i.student_number()
            clear()
        elif option == 2:
            os.system("cls")
            student = i.student_information(student_num)
            clear()
        elif option == 3:
            os.system("cls")
            course_num = i.course_number()
            clear()
        elif option == 4:
            os.system("cls")
            course = i.course_information(course_num)
            clear()
        elif option == 5:
            os.system("cls")
            o.student_list(student, student_num)
            o.course_list(course, course_num)
            i.student_mark(course_num, student, student_num)
            clear()
        elif option == 6:
            os.system("cls")
            o.course_list(course, course_num)
            clear()
        elif option == 7:
            os.system("cls")
            o.student_list(student, student_num)
            clear()
        elif option == 8:
            os.system("cls")
            o.course_list(course, course_num)
            o.show_student_mark(course, course_num, student, student_num)
            clear()
        elif option == 9:
            os.system("cls")
            o.cal_gpa(student, student_num, course, course_num)
            clear()

if __name__ == "__main__":
    main()