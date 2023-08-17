from scheduling_website.back_end.schedule import *
import random
class Individual:
    def __init__(self, num_of_section,num_of_period,grade_level):
        self.genes,self.fitness = self.generate_schedule(num_of_section,num_of_period,grade_level)
    def generate_schedule(num_of_section,num_of_period,grade_level):
        course_key = get_course_key_list()
        schedule = Schedule(num_of_section, num_of_period, grade_level, course_key, 0)
        genes = schedule.course_key
        fitness = schedule.hcs
        return genes,fitness

#individual = Individual(2,6,[10,10])




#tournament selection
def tournament_selection(population,tournament_size):
    selected_parents = []

    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda schedule: schedule.hcs)
        selected_parents.append(winner)

    return selected_parents