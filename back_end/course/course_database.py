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
            id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            teacher_name TEXT, --this is the foreign key
            course_type INTEGER,
            grade_level INTEGER,
            FOREIGN KEY (teacher_name) REFERENCES teacher_information(teacher_name)
            UNIQUE (course_name,teacher_name)
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
def display_all_course_information():
    connection, cursor = connect_database()
    # Retrieve data from the table
    cursor.execute('SELECT * FROM course_information')
    rows = cursor.fetchall()

    # Display retrieved data
    if len(rows)>0:
        for row in rows:
            print(row)
    else:
        print("Error: The table is empty")
    close_connection(cursor, connection)
def delete_course_info(course_name,teacher_name):
    connection, cursor = connect_database()
    query = '''
         DELETE FROM course_information 
         WHERE course_name = ? AND teacher_name =?
    '''

    cursor.execute(query, (course_name,teacher_name))

    if cursor.rowcount>0:
        connection.commit()
        print("delete is successful")
    else:
        connection.rollback()
        print(f"Error: {course_name} with {teacher_name} does not exist")
    close_connection(cursor, connection)