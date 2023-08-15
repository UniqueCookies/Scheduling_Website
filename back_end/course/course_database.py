from scheduling_website.back_end.course.course import Course
import sqlite3
def connect_database():
    connection = sqlite3.connect("database/course_information.db")
    cursor = connection.cursor()
    return connection, cursor
def close_connection(cursor,connection):
    cursor.close()
    connection.close()
def add_course(course_info):
    connection,cursor = connect_database()

    # create the table if not already there
    query = '''
        CREATE TABLE IF NOT EXISTS course_information
        (
            course_name TEXT PRIMARY KEY NOT NULL,
            teacher_name TEXT, --this is the foreign key
            course_type INTEGER,
            grade_level INTEGER,
            FOREIGN KEY (teacher_name) REFERENCES teacher_information(teacher_name)
        )       
    '''
    cursor.execute(query)

    #add info into the database
    query = '''
        INSERT INTO course_information
        (course_name, teacher_name,course_type,grade_level)
        VALUES
        (?,?,?,?)
    '''

    try:
        cursor.execute(query,(course_info.course_name, course_info.teacher_name, course_info.class_type, course_info.grade_level))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occured: {e}")

    close_connection(cursor,connection)