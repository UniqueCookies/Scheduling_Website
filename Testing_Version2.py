from back_end.course.multiple_course import *
from back_end.course.course import Course
from back_end.schedule import *
from back_end.course.course_database import *
from back_end.teacher.teacher_database import *
from back_end.algorithm import *

multiple_course,teacher_name = get_multiple_course_id()
print(multiple_course)
print(teacher_name)

print(if_multiple(5))