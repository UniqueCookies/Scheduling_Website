from scheduling_website.back_end.database import *
from scheduling_website.back_end.info import *

#Connect
connection,cursor,answer = connect_database()
if(answer!=True):
    print('Error! Connection is not estabilished')
else:
    print('Connection is successful')

'''''''''
#database.py test
create_table(cursor)
info_list = [103,'Bob',0,0,0,0,0,1,'english1',None,None,None]
insert_data(connection,cursor,info_list)

identification = 101
#delete_row(connection,cursor,identification)
display_all(connection,cursor)
'''''''''''

#info.py test
print(create_tuples(connection, cursor))


#close connection
if(close_connection(cursor,connection)):
    print('Connection is closed succesffully')
else:
    print('Error! Connection is not closed')