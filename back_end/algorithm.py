import copy

from back_end.course.course_database import get_course_key_list
from back_end.schedule import Schedule
from back_end.section import *
import random


# create the size of population input by the user
def create_population(num_of_population, num_of_section,
                      num_of_period):
    # initialize the schedule
    grade_level_list = get_unique_section()
    # create a number of schedules
    population = []
    for _ in range(num_of_population):
        schedule = Schedule(
            num_of_section, num_of_period, grade_level_list
        )  # Assuming 2 sections, 6 periods right now  --> input by the user
        population.append(schedule)
    return population


# tournament selection
def tournament_selection(population, tournament_size):

    tournament = random.sample(population, tournament_size)
    winner = max(tournament, key=lambda schedule: schedule.hcs)

    return winner


# Mutation Operator Section


# create offspring
def create_offspring(parent):
    offspring = copy.deepcopy(parent)
    return offspring


# randomly generate numbers for row and col
def random_generate_row(num_rows):
    row = random.randint(0, num_rows - 1)
    return row
def random_generate_col(num_cols):
    col = random.randint(0, num_cols - 1)
    return col
def random_generate(num_rows,num_cols):
    row =random_generate_row(num_rows)
    col =random_generate_col(num_cols)
    return row,col


# Single Mutation
def single_mutation(section):
    num_rows = len(section.matrix)
    num_cols = len(section.matrix[0])

    # Generate random row and column indices for the two elements to swap
    row1, col1 = random_generate(num_rows, num_cols)
    row2, col2 = random_generate(num_rows, num_cols)
    # Ensure the two sets of indices are distinct
    while row1 == row2 and col1 == col2:
        row2, col2 = random_generate(num_rows, num_cols)

    if section.check_if_double(row1, col1) or section.check_if_double(row2, col2):
        # If one of them is a double course
        # Swap the entire columns
        if section.check_if_swap_double(col1, col2):
            section.swap_column(col1, col2)
    else:
        section.swap_element(row1, col1, row2, col2)

    return True


# Hill climber for singler course
def hill_climber(section):
    num_rows = len(section.matrix)
    num_cols = len(section.matrix[0])
    iteration = 0
    maximum_iteration = 100

    # Generate random row and column indices for the two elements to swap
    row1, col1 = random_generate(num_rows, num_cols)
    row2, col2 = random_generate(num_rows, num_cols)
    while section.check_if_double(row1, col1):
        row1, col1 = random_generate(num_rows, num_cols)
    while section.check_if_double(row2, col2):
        row2, col2 = random_generate(num_rows, num_cols)

    # make sure this one is a clash,
    # after certain iteration, assume no clash
    while not section.check_if_clash(row1, col1) \
            and iteration < maximum_iteration:
        while section.check_if_double(row1, col1):
            row1, col1 = random_generate(num_rows, num_cols)
        iteration += 1
    if not section.check_if_clash(row1, col1):
        return None

    iteration = 0
    # make sure 2nd swap is a clash, assume no clash after certain iteration
    while (
            not section.check_if_clash(row2, col2) or col1 == col2
    ) and iteration < maximum_iteration and section.check_if_double(row2, col2):
        row2, col2 = random_generate(num_rows, num_cols)
        iteration += 1

    # swap happens
    section.swap_element(row1, col1, row2, col2)

    # Error Analysis
    if (
            section.check_if_clash(row2, col2) or col1 == col2
    ):  # only one teacher has a section conflict
        return False  # mutation with one clash and may not be meaningful swap
        # when col1==col2, that does not solve the section conflict

    return True


# Mutation step: randomly choose which function to perform
def mutation(section):
    function_list = [single_mutation, hill_climber]
    random_function = random.choice(function_list)
    result = random_function(section)
    if result:
        return f"{random_function} performed"
    elif result is None:
        return f"{random_function} not performed"
    else:
        return f"{random_function}: not fully performed"


def compare_fitness(parent, offspring):
    if parent.hcs >= offspring.hcs:
        return offspring
    else:
        return parent
