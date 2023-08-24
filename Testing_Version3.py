from back_end.course.multiple_course import *
from back_end.schedule import Schedule, repeating_teacher_schedule
from back_end.teacher.multiple_course_teacher import *
from back_end.course.course import Course
from back_end.section import *
from back_end.course.course_database import *
from back_end.teacher.teacher_database import *
from back_end.algorithm import *

grade_level_list = [(10, 2), (11, 2)]
population = create_population(5,6,grade_level_list)
parent = population[0]

overall_iteration = 0
while parent.hcs > 0 and overall_iteration < 1:
    parent = tournament_selection(population, 2)
    print(parent)
    iteration = 0
    while parent.hcs > 0 and iteration < 10:
        offspring = create_offspring(parent)
        print(mutation(offspring))
        parent = compare_fitness(parent, offspring)
        iteration += 1
    overall_iteration += 1

print(parent)
print(f"The number of iteration is: {iteration}")


'''''''''''''''''''''''
grade_level_list = [(10, 2), (11, 2)]
schedule = Schedule(6, grade_level_list)
print(schedule)
'''''''''''''''''''''''

'''''''''''''''''''''''
course_key = get_course_key_list(10)
section = Section(2, 6, 10, course_key)
print(section)
'''''''''''''''''''''
