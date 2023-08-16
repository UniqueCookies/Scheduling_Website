from scheduling_website.back_end.schedule import *

#schedule test
# Creating a Schedule object with a 3x4 matrix
schedule = Schedule(3, 4)

# Displaying the matrix within the Schedule object
schedule.display()

#class_database portion test
'''''''''
teacher_name = 'Devin'
course = Course("Chemistry",teacher_name, 0, 10)
# Display course information
#add_course(course)
course_name = 'Chemistry'
teacher_name = 'Tommy'
#delete_course_info(course_name,teacher_name)
#display_all_course_information()
course = retrieve_course_info(course_name,teacher_name)
print(course)
'''''''''

'''''''''
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
'''''''''''

# Testing teacher_object functions
'''''''''''
teacher_name = "Tommy"
teacher_availability = [1, 1, 1, 1, 0, 0]  # Example availability for each day/time
teacher_preference = [0, 0, 0, 0, 0, 0]  # Example preference for each day/time
sally = Teacher(teacher_name,teacher_availability,teacher_preference)
print(sally)
add_teacher(sally)
display_all_teacher_information()
#delete_teacher_info('Devin')
teacher_info = retrieve_teacher_info('Sally')
if teacher_info is not None:
    print(teacher_info)
else:
    print("Teacher not found")
'''''''''''


