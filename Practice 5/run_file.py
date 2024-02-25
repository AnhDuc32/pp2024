import os
import zipfile
import numpy as np
import input_file as i
import output_file as o

def compress_file():
    file_name = ['students.txt', 'courses.txt', 'marks.txt']
    compress_file_name = zipfile.ZipFile('students.dat', 'w')
    for f in file_name:
        compress_file_name.write(f, compress_type=zipfile.ZIP_DEFLATED)
    compress_file_name.close()

def decompress_file(student, course, student_num, course_num):
    file_name = 'students.dat'
    if os.path.exists(file_name):
        print('"Students.dat" is already exists!\nLoading data successfully!')
        with zipfile.ZipFile(file_name, 'r') as zip_file:
            zip_file.extractall()
            with open('students.txt', 'r') as stu_data:
                line = stu_data.readlines()
                for l in line:
                    id, name, dob = l.split(' - ')
                    id = id.replace('ID: ', '')
                    name = name.replace('Name: ', '')
                    dob = dob.replace('DoB: ', '')
                    stu = i.Student(id, name, dob)
                    student.append(stu)
                    student_num += 1
            with open('courses.txt', 'r') as course_data:
                line = course_data.readlines()
                for l in line:
                    id, name, credit = l.split(' - ')
                    id = id.replace('ID: ', '')
                    name = name.replace('Name: ', '')
                    credit = credit.replace('Credit: ', '')
                    cour = i.Course(id, name, credit)
                    course.append(cour)
                    course_num += 1
            with open('marks.txt', 'r') as mark_data:
                line = mark_data.readlines()
                for l in line:
                    if not l.startswith('Course'):
                        id, name, dob, mark = l.split(' - ')
                        id = id.replace('ID: ', '')
                        mark = mark.replace('Mark: ', '')
                        for s in range (student_num):
                            if id == student[s]._id:
                                student[s]._mark = np.append(student[s]._mark, float(mark))
    else:
        print('"Students.dat" is not exists!')
    return student, course, student_num, course_num

def clear():
    print("")
    os.system("pause")
    os.system("cls")

def main():
    student = []
    course = []
    student_num = 0
    course_num = 0
    
    student, course, student_num, course_num = decompress_file(student, course, student_num, course_num)
    
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
            compress_file()
            os.system("cls")
            print("""
You have exited the program. All the files have been compressed into "students.dat".
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
            o.student_list(student, student_num)
            o.show_student_mark(course, course_num, student, student_num)
            clear()
        elif option == 9:
            os.system("cls")
            o.cal_gpa(student, student_num, course, course_num)
            clear()

if __name__ == "__main__":
    main()