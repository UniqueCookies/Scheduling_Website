from scheduling_website.back_end.database import *
from scheduling_website.back_end.info import *

#Connect
connection,cursor = connect_database()


#database.py test
#create_table()
#info_list = [104,'To_be_Deleted',0,0,1,1,1,1,'History','English','Math','Chemistry']
#insert_data(info_list)
#identification = 104
#delete_row(identification)
#display_all()
course_list,num_classes = get_unique_classes()


#info.py test
num_period = 4
create_matrix(num_period,num_classes)
print(get_teacher_course_list())



#close connection
if(close_connection(cursor,connection)):
    print('Connection is closed succesffully')
else:
    print('Error! Connection is not closed')