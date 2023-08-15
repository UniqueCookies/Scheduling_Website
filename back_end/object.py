import sqlite3
class Teacher:
    def __init__(self, name, availability, preference):
        self.name = name
        self.availability = availability
        self.preference = preference
    def __str__(self):
        return f"Teacher: {self.name}\nAvailability: {self.availability}\nPreference: {self.preference}"

# Example usage
teacher_name = "John Smith"
teacher_availability = [1, 0, 1, 1, 0, 1]  # Example availability for each day/time
teacher_preference = [5, 4, 3, 2, 1, 0]  # Example preference for each day/time


#add teacher info to the database
def add_teacher(info):
    connection = sqlite3.connect("database/teacher.db")
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS teacher
        (
            id INTEGER PRIMARY KEY,
            name TEXT,
            availability TEXT
        )       
    '''

