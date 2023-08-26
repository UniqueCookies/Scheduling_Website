from back_end.course.course import Course
from back_end.course.course_database import *
import sqlite3


# get all the multiple course and its teacher's name
def get_course_id_special(grade,course_type):
    connection, cursor = connect_database()
    query = '''
    select id,teacher_name from course_information where course_type =? 
                                                and grade_level = ?
    '''

    cursor.execute(query,(course_type,grade))
    rows = cursor.fetchall()
    special_course_list = [row[0] for row in rows]
    teacher_name_list = [row[1] for row in rows]
    close_connection(cursor, connection)
    if special_course_list is None or teacher_name_list is None:
        return None, None
    return special_course_list, teacher_name_list


# check if the schedule is infeasible
def check_conflict_teacher(teacher_name_list):
    seen_name = set()

    for name in teacher_name_list:
        if name in seen_name:
            return False
        seen_name.add(name)
    return True


# check if the course is multiple or not
def if_multiple(key):
    connection, cursor = connect_database()
    cursor.execute(
        "select course_type from course_information where id = ?", (key,)
    )
    check = cursor.fetchone()
    check = check[0]
    if check == 1:
        return True
    else:
        return False
