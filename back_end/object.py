import sqlite3
import json
class Teacher:
    def __init__(self, name, availability, preference):
        self.name = name
        self.availability = availability
        self.preference = preference
    def __str__(self):
        return f"Teacher: {self.name}\nAvailability: {self.availability}\nPreference: {self.preference}"

#teacher database
def connect_database():
    connection = sqlite3.connect("database/teacher_information.db")
    cursor = connection.cursor()
    return connection, cursor
#add teacher info to the database
def add_teacher(teacher_info):
    connection,cursor = connect_database()

    # create the table if not already there
    query = '''
        CREATE TABLE IF NOT EXISTS teacher_information
        (
            id INTEGER PRIMARY KEY,
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

    cursor.close()
    connection.close()
