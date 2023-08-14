import sqlite3

#create matrix according to the num of periods and num of classes
def create_matrix(num_period, num_classes):
    schedule = [[0 for _ in range(num_classes)] for _ in range(num_period)]
    return schedule

#create teacher-course tuples
def create_tuples(cursor):

    query = '''
    SELECT teacher_name, course_1 FROM teacher_availability where course_1 IS NOT NULL
    UNION 
    SELECT teacher_name, course_2 FROM teacher_availability where course_2 IS NOT NULL
    '''

    info = cursor.execute(query)

    teacher_course_tuples = 0

    return teacher_course_tuples

#sort the into three list
