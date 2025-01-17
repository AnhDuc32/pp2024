import os
import zipfile
import pickle
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
            with open('students.txt', 'rb') as stu_data:
                stu = pickle.load(stu_data)
                for j in range (len(stu)):
                    student_num += 1
                    student.append(stu[j])
            with open('courses.txt', 'rb') as course_data:
                cour = pickle.load(course_data)
                for j in range (len(cour)):
                    course_num += 1
                    course.append(cour[j])
            with open('marks.txt', 'rb') as mark_data:
                mark = pickle.load(mark_data)
                for s in range (student_num):
                    data = mark[s::course_num]
                    for c in range (course_num):
                        student[s]._mark = np.append(student[s]._mark, data[c])
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