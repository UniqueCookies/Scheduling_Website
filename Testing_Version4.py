from back_end.algorithm import single_mutation_section
from back_end.course.special_course import *
from back_end.schedule import Schedule, repeating_teacher_schedule
from back_end.teacher.special_course_teacher import *
from back_end.course.course import Course
from back_end.section import *
from back_end.course.course_database import *
from back_end.teacher.teacher_database import *
from back_end.algorithm import *


course_key = get_course_key_list(9)
section = Section(3, 7, 9, course_key)
print(section)

'''''''''''
grade_level_list = [(9,3)]
population = create_population(10, 7, grade_level_list)
parent = population[0]

overall_iteration = 0
count = 0
while parent.hcs > 0 and overall_iteration < 1:
    parent = tournament_selection(population, 5)
    print(parent)
    iteration = 0
    while parent.hcs > 0 and iteration < 4000:
        offspring = create_offspring(parent)
        mutation(offspring)
        parent = compare_fitness(parent, offspring)
        count += 1
        iteration += 1
    overall_iteration += 1
    print(offspring)

print(f"The number of iteration is: {count}")
'''''''''''