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
    possible_period = []
    for i in range(sublist_length):
        reference_value = availability_list[0][i]
        if all(sublist[i] == reference_value for sublist in availability_list[1:]):
            possible_period.append(i)

    return possible_period


def get_availability_double(teacher_name_list):
    # Get availability
    teacher_name_tuple = tuple(teacher_name_list)
    placeholders = ','.join(['?' for _ in teacher_name_list])
    connection, cursor = connect_database()
    query = '''
    SELECT availability FROM teacher_information WHERE teacher_name IN ({})
    '''.format(placeholders)
    cursor.execute(query, teacher_name_tuple)
    availability = cursor.fetchall()
    close_connection(cursor, connection)

    # convert from sting to list
    temp = []
    for i in range(len(availability)):
        to_add = json.loads(availability[i][0])
        to_add = check_availability_double(to_add)
        if to_add is not False:
            temp.append(to_add)
        else:
            return False
    return temp


def check_availability_double(availability):
    num_of_period = len(availability)
    available = []
    if not num_of_period%2 ==0:
        return False
    num_of_block = num_of_period//2
    for i in range (0,num_of_period-1, 2):
        if not availability[i]==0 and not availability[i+1]==0:
            available.append(i)
            available.append(i+1)
    return available
