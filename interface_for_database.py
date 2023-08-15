from scheduling_website.back_end.database import *
from scheduling_website.back_end.info import *


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
num_section = 2
population= create_matrix(num_period,num_section)
list = get_teacher_course_list()
print(random_list(list,population))


