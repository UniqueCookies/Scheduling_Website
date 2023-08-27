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
section = Section(2, 6, 10, course_key)
print(section)


'''''''''''
grade_level_list = [(10, 2), (11, 2)]
population = create_population(10,6,grade_level_list)
parent = population[0]

print("Did it get this far?")

overall_iteration = 0
count=0
while parent.hcs > 0 and overall_iteration < 1:
    parent = tournament_selection(population, 5)
    print(parent)
    iteration = 0
    while parent.hcs > 0 and iteration < 1000:
        offspring = create_offspring(parent)
        mutation(offspring)
        parent = compare_fitness(parent, offspring)
        count +=1
        iteration +=1
    overall_iteration += 1
    print(offspring)

print(f"The number of iteration is: {count}")
'''''''''''