import json
import sqlite3

from back_end.teacher.teacher import Teacher
from back_end.teacher.teacher_database import *


def multiple_course_info(teacher_name_list):
    # get availability information from teacher in the multiple course type
    connection, cursor = connect_database()
    availability_list = []
    for teacher_name in teacher_name_list:
        cursor.execute("select availability from teacher_information where teacher_name =?", (teacher_name,))
        availability = cursor.fetchone()
        availability = json.loads(availability[0])
        availability_list.append(availability)
    close_connection(cursor, connection)

    sublist_length = len(availability_list[0])
    possible_period=[]
    for i in range (sublist_length):
        reference_value = availability_list[0][i]
        if all(sublist[i] == reference_value for sublist in availability_list[1:]):
            possible_period.append(i)

    return possible_period




