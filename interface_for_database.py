from scheduling_website.back_end.database import *

#Connect
connection,cursor,answer = connect_database()
if(answer!=True):
    print('Error! Connection is not estabilished')
else:
    print('Connection is successful')

create_table(cursor)
info_list = [102,'Sue',0,1,0,0,0,1,'math','math','science','science']
insert_data(connection,cursor,info_list)



identification = 101
#delete_row(connection,cursor,identification)
display_all(connection,cursor)

#close connection
if(close_connection(cursor,connection)):
    print('Connection is closed succesffully')
else:
    print('Error! Connection is not closed')