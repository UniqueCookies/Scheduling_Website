from scheduling_website.back_end.schedule import *
import random

#create the size of population input by the user
def create_population(num_of_population, num_of_section, num_of_period, grade_level):
    # initailize the schedule
    course_key = get_course_key_list()
    # create a number of schedules
    population = []
    for _ in range(num_of_population):
        schedule = Schedule(num_of_section, num_of_period, grade_level, course_key)  # 2 sections, 6 periods  --> input by the user
        population.append(schedule)
    return population

#tournament selection
def tournament_selection(population,tournament_size):
    selected_parents = []

    tournament = random.sample(population, tournament_size)
    winner = max(tournament, key=lambda schedule: schedule.hcs)

    return winner

#Mutation Operator Section

#randomly generate numbers for row and col
def random_generate(num_rows,num_cols):
    row = random.randint(0, num_rows - 1)
    col = random.randint(0, num_cols - 1)
    return row,col

#Single Mutation
def single_mutation(schedule):
    num_rows = len(schedule.matrix)
    num_cols = len(schedule.matrix[0])

    # Generate random row and column indices for the two elements to swap
    row1,col1 = random_generate(num_rows,num_cols)
    row2, col2 = random_generate(num_rows, num_cols)
    # Ensure the two sets of indices are distinct
    while row1 == row2 and col1 == col2:
        row2, col2 = random_generate(num_rows, num_cols)

    #swap the element
    schedule.swap_element(row1,col1,row2,col2)

    return schedule

#Hill climber for singler course
def hill_climber(schedule):
    num_rows = len(schedule.matrix)
    num_cols = len(schedule.matrix[0])
    iteration =0
    maximum_iteration=100

    # Generate random row and column indices for the two elements to swap
    row1,col1 = random_generate(num_rows,num_cols)
    row2, col2 = random_generate(num_rows, num_cols)

    #make sure this one is a clash, after certain iteration, assume no clash
    while not schedule.check_if_clash(row1,col1) and iteration<maximum_iteration:
        row1, col1 = random_generate(num_rows, num_cols)
        iteration +=1
    if not schedule.check_if_clash(row1,col1):
        return None

    iteration = 0
    #make sure 2nd swap is a clash is a clash
    while (not schedule.check_if_clash(row2,col2) or col1==col2) and iteration < maximum_iteration :
        row2, col2 = random_generate(num_rows, num_cols)
        iteration += 1

    schedule.swap_element(row1, col1, row2, col2)

    print(iteration)
    key = schedule.get_info(row2, col2)
    print(schedule.transform_element(key))
    key = schedule.get_info(row1, col1)
    print(schedule.transform_element(key))


    if schedule.check_if_clash(row2,col2) or col1==col2: #only one teacher has a schedule conflict
        print(col1,col2,schedule.check_if_clash(row2,col2))
        return False #mutation with one clash and may not be meaningful swap
                    #when col1==col2, that does not solve the schedule conflict

    return True
