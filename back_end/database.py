import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
# Create a cursor object to interact with the database
def connect_database():
    connection = sqlite3.connect("database/teacher_availability.db")
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    connection,cursor=connect_database()
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
    close_connection(cursor,connection)
def insert_data(info_list):
    # Insert data into the table
    connection, cursor = connect_database()
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
    close_connection(cursor, connection)
#display all data
def display_all():
    connection, cursor = connect_database()
    # Retrieve data from the table
    cursor.execute('SELECT * FROM teacher_availability')
    rows = cursor.fetchall()

    # Display retrieved data
    if len(rows)>0:
        for row in rows:
            print(row)
    else:
        print("Error: The table is empty")
    close_connection(cursor, connection)
def delete_row(identification):
    connection, cursor = connect_database()
    query = f"DELETE FROM teacher_availability WHERE identification = ?"
    cursor.execute(query, (identification,))


    if cursor.rowcount>0:
        connection.commit()
        print("delete is successful")
    else:
        connection.rollback()
        print(f"Error: {identification} does not exist")
    close_connection(cursor, connection)

#get unique classes from the databse -> will use it to create the num_of_col for the matrix
def get_unique_classes():
    connection, cursor = connect_database()
    query = '''
        SELECT DISTINCT course_1 from teacher_availability'
        UNION 
        SELECT DISTINCT course_2 from teacher_availability'
        UNION
        SELECT DISTINCT course_3 from teacher_availability'
        UNION
        SELECT DISTINCT course_4 from teacher_availability' ; 
     '''

    cursor.execute(query)
    info = cursor.fetchall()

    course_list = [row[0] for row in info]

    num_classes = len(course_list)
    close_connection(cursor, connection)
    return course_list,num_classes

#get the teacher/class pairs from the database and return the list
def get_teacher_course_list():
    connection, cursor = connect_database()
    query = '''
    SELECT teacher_name, course_1 FROM teacher_availability where course_1 IS NOT NULL
    UNION 
    SELECT teacher_name, course_2 FROM teacher_availability where course_2 IS NOT NULL
    UNION 
    SELECT teacher_name, course_3 FROM teacher_availability where course_3 IS NOT NULL
    UNION
    SELECT teacher_name, course_4 FROM teacher_availability where course_4 IS NOT NULL
    '''

    cursor.execute(query)
    info = cursor.fetchall()
    teacher_course_tuple = [row for row in info]
    close_connection(cursor, connection)

    return teacher_course_tuple
 # Close the cursor and connection
def close_connection(cursor,connection):
    cursor.close()
    connection.close()
    return True

