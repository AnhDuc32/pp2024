import math

def student_list(student, student_num):
    if not student:
        print("There are currently no students")
        return None
    else:
        print("Student list:")
        for i in range (student_num):
            print(f'{i+1}. {student[i]}')
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
        sort_gpa = sorted(student, key = lambda x: x._gpa, reverse = True)
        for stu in sort_gpa:
            print(f'{stu} - GPA: {round(stu._gpa, 2)}')

def course_list(course, course_num):
    if not course:
        print("\nThere are currently no courses\n")
        return None
    else:
        print("Course list:")
        for i in range (course_num):
            print(f'{i+1}. {course[i]}')