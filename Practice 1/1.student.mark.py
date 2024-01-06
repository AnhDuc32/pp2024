import os

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
        student_data = {}
        student_data["ID"] = input("Enter ID: ")
        student_data["Name"] = input("Enter name: ")
        student_data["DoB"] = input("Enter DoB: ")
        print("")
        student_info.append(student_data)
    return student_info

def student_list(student, student_num):
    if not student:
        print("There are currently no students\n")
        return None
    else: 
        for i in range (student_num):
            print(f'Student {i+1}:\nID: {student[i]["ID"]} - Name: {student[i]["Name"]} - DoB: {student[i]["DoB"]}\n')

def student_mark(course, course_num, student, student_num):
    if course_num == 0 or student_num == 0:
        return None
    else:
        a = input(f"Enter course's ID: ")
        for i in range (course_num):
            if a == course[i]["ID"]:
                for j in range (student_num):
                    b = input(f'\nEnter mark for student {j+1}: ')
                    student[j]["Mark"] = b
    return a
                    
def show_student_mark(course, course_num, student, student_num, course_mark_id):
    if not course:
        return None
    else:
        a = input(f"Enter course's ID: ")
        for i in range (course_num):
            if a == course_mark_id and course[i]["ID"] == course_mark_id:
                print(f"\nCourse's ID: {course[i]['ID']}")
                for j in range (student_num):
                    print(f"Student {j+1}'s mark: {student[j]['Mark']}")
                break
            elif a != course_mark_id:
                print("\nThere are currently no marks in this course")
                break
                
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
        course_data = {}
        print(f'Course {i+1}: ')
        course_data["ID"] = input("Enter ID: ")
        course_data["Name"] = input("Enter name: ")
        print("")
        course_info.append(course_data)
    return course_info

def course_list(course, course_num):
    if not course:
        print("There are currently no courses\n")
        return None
    else:
        for i in range (course_num):
            print(f'Course {i+1}:\nID: {course[i]["ID"]} - Name: {course[i]["Name"]}\n')

def clear():
    print("")
    os.system("pause")
    os.system("cls")

def main():
    student = []
    course = []
    student_num = 0
    course_num = 0
    course_mark_id = 0
    
    while (True):
        print("""
===========================================================
1. Input number of students in a class
2. Input student information: id, name, DoB
3. Input number of courses
4. Input course information: id, name
5. Select a course, input marks for student in this course
6. List courses
7. List students
8. Show student marks for a given course
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
            student_num = student_number()
            clear()
        elif option == 2:
            os.system("cls")
            student = student_information(student_num)
            clear()
        elif option == 3:
            os.system("cls")
            course_num = course_number()
            clear()
        elif option == 4:
            os.system("cls")
            course = course_information(course_num)
            clear()
        elif option == 5:
            os.system("cls")
            student_list(student, student_num)
            course_list(course, course_num)
            course_mark_id = student_mark(course, course_num, student, student_num)
            clear()
        elif option == 6:
            os.system("cls")
            course_list(course, course_num)
            clear()
        elif option == 7:
            os.system("cls")
            student_list(student, student_num)
            clear()
        elif option == 8:
            os.system("cls")
            course_list(course, course_num)
            show_student_mark(course, course_num, student, student_num, course_mark_id)
            clear()

if __name__ == "__main__":
    main()