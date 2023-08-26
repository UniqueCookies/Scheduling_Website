from back_end.course.special_course import *
from back_end.schedule import Schedule, repeating_teacher_schedule
from back_end.teacher.special_course_teacher import *
from back_end.course.course import Course
from back_end.section import *
from back_end.course.course_database import *
from back_end.teacher.teacher_database import *
from back_end.algorithm import *

course_key = get_course_key_list(10)
section = Section(2, 6, 10, course_key)
print(section)
