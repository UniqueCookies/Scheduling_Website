import random
import sqlite3

from back_end.course.course import Course


def connect_database():
    connection = sqlite3.connect("database/course_information.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


def add_course(course_info):
    connection, cursor = connect_database()

    # create the table if not already there
    query = """
        CREATE TABLE IF NOT EXISTS course_information
        (
            id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            teacher_name TEXT, --this is the foreign key
            course_type INTEGER,
            grade_level INTEGER,
            FOREIGN KEY (teacher_name)
                REFERENCES teacher_information(teacher_name)
        )
    """
    cursor.execute(query)

    # add info into the database
    query = """
        INSERT INTO course_information
        (course_name, teacher_name,course_type,grade_level)
        VALUES
        (?,?,?,?)
    """

    try:
        cursor.execute(
            query,
            (
                course_info.course_name,
                course_info.teacher_name,
                course_info.class_type,
                course_info.grade_level,
            ),
        )
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occured: {e}")

    close_connection(cursor, connection)


# display all the course information from the database
def display_all_course_information():
    connection, cursor = connect_database()
    # Retrieve data from the table
    cursor.execute("SELECT * FROM course_information")
    rows = cursor.fetchall()

    # Display retrieved data
    if len(rows) > 0:
        for row in rows:
            print(row)
    else:
        print("Error: The table is empty")
    close_connection(cursor, connection)


# delete a certain course(s) taught by a particular teacher
def delete_course_info(course_name, teacher_name):
    connection, cursor = connect_database()
    query = """
         DELETE FROM course_information
         WHERE course_name = ? AND teacher_name =?
    """

    cursor.execute(query, (course_name, teacher_name))

    if cursor.rowcount > 0:
        connection.commit()
        print("delete is successful")
    else:
        connection.rollback()
        print(f"Error: {course_name} with {teacher_name} does not exist")
    close_connection(cursor, connection)


# Get the course object information by matching the course and teacher name.
# If the teacher teaches more than one of the same class
# will only return one of the course
def retrieve_course_info(course_name, teacher_name):
    connection, cursor = connect_database()
    query = """
        select * from course_information
            where course_name =? AND teacher_name =?
        """
    try:
        cursor.execute(query, (course_name, teacher_name))
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    course_data = cursor.fetchone()
    close_connection(cursor, connection)

    if course_data:
        id, course_name, teacher_name, \
            course_type, grade_level = course_data[0]
        course = Course(course_name, teacher_name, course_type, grade_level)
    else:
        return None

    return course


# retrieve teacher's name according to the key
def retrieve_teacher_name(key):
    # get teacher name from the course_database
    connection, cursor = connect_database()
    cursor.execute("select teacher_name from course_information "
                   "where id=?", (key,))
    teacher_name = cursor.fetchone()
    if teacher_name:
        teacher_name = teacher_name[0]
    close_connection(cursor, connection)
    return teacher_name


# Get the list of course_key
def get_course_key_list(grade):
    connection, cursor = connect_database()
    query = """
    SELECT id from course_information where grade_level = ? and course_type <>?
    """
    cursor.execute(query,(grade,2,))
    course_key_list = [row[0] for row in cursor.fetchall()]
    query = """
    SELECT id from course_information where grade_level = ? and course_type =?
    """
    cursor.execute(query,(grade,2,))
    double_course_key_list=[row[0] for row in cursor.fetchall()]
    course_key_list = course_key_list + double_course_key_list
    close_connection(cursor, connection)
    return course_key_list


def random_course_key_list(course_key_list):
    new_list = random.sample(course_key_list, len(course_key_list))
    return new_list


# get course name from the key
def get_course_name(key):
    connection, cursor = connect_database()
    cursor.execute("select course_name, course_type from course_information "
                   "where id=?", (key,))
    info = cursor.fetchall()
    close_connection(cursor, connection)

    info = info[0]
    name = info[0]
    course_type = info[1]
    return name, course_type


# check if the keys refer to the same class
def check_hcs_repeating_course(key1, key2):
    # fetch course_name
    name1,course_type1= get_course_name(key1)
    name2,course_type2 = get_course_name(key2)

    if course_type1 ==2 and course_type2 == 2:
        return False
    # compare
    return name1 == name2


# Check the keys refer to the same teacher
def check_hcs_repeating_teacher(key1, key2):
    # get teacher_name from the table
    connection, cursor = connect_database()
    cursor.execute("select teacher_name from course_information "
                   "where id=?", (key1,))
    name1 = cursor.fetchone()
    name1 = name1[0]
    cursor.execute("select teacher_name from course_information "
                   "where id=?", (key2,))
    name2 = cursor.fetchone()
    name2 = name2[0]
    close_connection(cursor, connection)

    # check if the teacher is overbooked
    if name1 is not None and name2 is not None:
        return name1 == name2
    else:
        return None


def get_unique_section():
    connection, cursor = connect_database()
    cursor.execute("select DISTINCT grade_level from course_information")
    grade_list = cursor.fetchall()
    close_connection(cursor, connection)

    grade_list =[row[0] for row in grade_list]
    return grade_list
