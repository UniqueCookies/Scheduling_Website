from scheduling_website.back_end.schedule import *
import random


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

    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda schedule: schedule.hcs)
        selected_parents.append(winner)

    return selected_parents