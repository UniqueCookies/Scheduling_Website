from scheduling_website.back_end.database import *
from scheduling_website.back_end.info import *

#Connect
connection,cursor = connect_database()


#database.py test
#create_table()
#info_list = [103,'Devin',0,0,1,1,1,1,'History','English','Math','Chemistry']
#insert_data(connection,cursor,info_list)
#delete_row(connection,cursor,identification)
#display_all(connection,cursor)
course_list,num_classes = get_unique_classes(connection,cursor)
print(course_list)
print(num_classes)

#info.py test
#print(create_tuples(cursor))



#close connection
if(close_connection(cursor,connection)):
    print('Connection is closed succesffully')
else:
    print('Error! Connection is not closed')