import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
# Create a cursor object to interact with the database
def connect_database():
    connection = sqlite3.connect('teacher_availability.db')
    cursor = connection.cursor()
    return connection, cursor, True

def create_table(cursor):
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS teacher_availability
                  ( 
                    identification INTEGER PRIMARY KEY NOT NULL,
                    teacher_name TEXT NOT NULL, 
                    period_1 INTEGER,
                    period_2 INTEGER,
                    period_3 INTEGER,
                    period_4 INTEGER, 
                    period_5 INTEGER,
                    period_6 INTEGER,
                    course_1 TEXT NOT NULL,
                    course_2 TEXT,
                    course_3 TEXT,
                    course_4 TEXT
                  )
                  ''')

def insert_data(connection,cursor,info_list):
    # Insert data into the table
    identification, teacher_name, period_1, period_2, period_3, period_4, period_5, period_6, course_1, course_2, course_3, course_4 = info_list
    query = '''
                    INSERT INTO teacher_availability
                    (
                    identification,teacher_name,period_1,period_2,period_3,period_4, 
                    period_5,period_6,course_1,course_2,course_3,course_4
                    )
                    VALUES
                    (
                    ?,?,?,?,?,?,?,?,?,?,?,?
                    )
    
    '''
    values = (identification,teacher_name,period_1,period_2,period_3,period_4,
            period_5,period_6,course_1,course_2,course_3,course_4)

    try:
        cursor.execute(query,values)
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occured: {e}")



def function_tobedefined(conn, cursor):
    # Retrieve data from the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Display retrieved data
    for row in rows:
        print(row)

 # Close the cursor and connection
def close_connection(cursor,connection):
    cursor.close()
    connection.close()
    return True

