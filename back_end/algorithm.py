from scheduling_website.back_end.schedule import *
#create population with the number of populations
def create_population(num_of_population,num_of_section,num_of_period,grade_level):
    #initailize the schedule
    course_key = get_course_key_list()
    #create a number of schedules
    population = []
    for _ in range(num_of_population):
        schedule = Schedule(num_of_section, num_of_period, grade_level, course_key, 0)  # 2 sections, 6 periods  --> input by the user
        schedule = schedule.create_schedule()
        print(schedule)
        population.append(schedule)
    return population


