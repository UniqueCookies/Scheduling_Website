import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
# Create a cursor object to interact with the database
def connect_database():
    connection = sqlite3.connect('teacher_availability.db')
    cursor = connection.cursor()
    return connection, cursor, True

def create_table(cursor):
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS teacher_avaialbility
                  ( 
                    id int PRIMARY KEY,
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

def function_tobedefined(conn,cursor):
    # Insert data into the table
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 30))
    conn.commit()

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

