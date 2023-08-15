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
            course_name TEXT UNIQUE,
            teacher_name TEXT,
            availability TEXT,
            preference TEXT
        )       
    '''
    cursor.execute(query)

    #change list to JSON strings
    availability_json = json.dumps(teacher_info.availability)
    preference_json = json.dumps(teacher_info.preference)

    #add info into the database
    query = '''
        INSERT INTO teacher_information
        (teacher_name, availability, preference)
        VALUES
        (?,?,?)
    '''

    try:
        cursor.execute(query,(teacher_info.name,availability_json,preference_json ))
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occured: {e}")

    close_connection(cursor,connection)