import sqlite3
import json
from scheduling_website.back_end.teacher import Teacher
#teacher database connections
def connect_database():
    connection = sqlite3.connect("database/teacher_information.db")
    cursor = connection.cursor()
    return connection, cursor
def close_connection(cursor,connection):
    cursor.close()
    connection.close()
#add teacher info to the database
def add_teacher(teacher_info):
    connection,cursor = connect_database()

    # create the table if not already there
    query = '''
        CREATE TABLE IF NOT EXISTS teacher_information
        (
            id INTEGER PRIMARY KEY,
            teacher_name TEXT UNIQUE,
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
#display all teachers
def display_all_teacher_information():
    connection, cursor = connect_database()
    # Retrieve data from the table
    cursor.execute('SELECT * FROM teacher_information')
    rows = cursor.fetchall()

    # Display retrieved data
    if len(rows)>0:
        for row in rows:
            print(row)
    else:
        print("Error: The table is empty")
    close_connection(cursor, connection)
def delete_teacher_info(name):
    connection, cursor = connect_database()
    query = f"DELETE FROM teacher_information WHERE teacher_name = ?"
    cursor.execute(query, (name,))

    if cursor.rowcount>0:
        connection.commit()
        print("delete is successful")
    else:
        connection.rollback()
        print(f"Error: {name} does not exist")
    close_connection(cursor, connection)
#Retrieve teacher info from the database into the object
def retrieve_teacher_info(name):

    #fetch data
    connection, cursor = connect_database()
    query = '''
    select * from teacher_information where teacher_name =?
    '''
    try:
        cursor.execute(query,(name,))
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    teacher_data = cursor.fetchone()
    close_connection(cursor,connection)

    #turn it back to the
    if teacher_data:
        id, teacher_name, availability_json, preference_json = teacher_data
        availability = json.loads(availability_json)
        preference = json.loads(preference_json)
        teacher = Teacher(teacher_name, availability, preference)
        return teacher
    else:
        return None