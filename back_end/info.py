import sqlite3

#create matrix according to the num of periods and num of classes
def create_matrix(num_period, num_classes):
    schedule = [[0 for _ in range(num_classes)] for _ in range(num_period)]
    quer
    return schedule

#create teacher-course tuples
def create_tuples(cursor):

    cursor.execute("SELECT teacher_name, course_1 FROM teacher_availability where course_1 IS NOT NULL ")
    info = cursor.fetchall()
    temp = [(teacher_name, course_1) for teacher_name, course_1 in info]
    teacher_course_tuples = temp

    cursor.execute("SELECT teacher_name, course_2 FROM teacher_availability where course_2 IS NOT NULL ")
    info = cursor.fetchall()
    temp = [(teacher_name, course_2) for teacher_name, course_2 in info]
    teacher_course_tuples.extend(temp)

    cursor.execute("SELECT teacher_name, course_3 FROM teacher_availability where course_3 IS NOT NULL ")
    info = cursor.fetchall()
    temp = [(teacher_name, course_3) for teacher_name, course_3 in info]
    teacher_course_tuples.extend(temp)

    cursor.execute("SELECT teacher_name, course_4 FROM teacher_availability where course_4 IS NOT NULL ")
    info = cursor.fetchall()
    temp = [(teacher_name, course_4) for teacher_name, course_4 in info]
    teacher_course_tuples.extend(temp)

    return teacher_course_tuples

#sort the into three list
