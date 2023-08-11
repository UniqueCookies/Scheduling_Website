from scheduling_website.back_end.database import *

#Connect
connection,cursor,answer = connect_database()
if(answer!=True):
    print('Error! Connection is not estabilished')
else:
    print('Connection is successful')


#close connection
if(close_connection(cursor,connection)):
    print('Connection is closed succesffully')
else:
    print('Error! Connection is not closed')