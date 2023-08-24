from back_end.course.special_course import *
from back_end.teacher.special_course_teacher import *
from back_end.course.course import Course
from back_end.section import *
from back_end.course.course_database import *
from back_end.teacher.teacher_database import *
from back_end.algorithm import *

# test algorithm.py
population = create_population(100, 2, 6, 10)
parent = tournament_selection(population, 5)
overall_iteration = 0
while parent.hcs > 0 and overall_iteration < 3:
    parent = tournament_selection(population, 5)
    iteration = 0
    while parent.hcs > 0 and iteration < 1000:
        offspring = create_offspring(parent)
        mutation(offspring)
        parent = compare_fitness(parent, offspring)
        iteration += 1
    overall_iteration += 1
print(parent)
print(f"The number of iteration is: {iteration}")