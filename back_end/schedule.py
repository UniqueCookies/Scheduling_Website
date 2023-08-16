from scheduling_website.back_end.course.course_database import *
class Schedule:
    def __init__(self, num_of_sections, num_of_period,grade_level_list,course_key):
        self.num_of_sections = num_of_sections
        self.num_of_period = num_of_period
        self.grade_level_list=grade_level_list
        self.course_key = course_key
        self.matrix = [[None for _ in range(num_of_period)] for _ in range(num_of_sections)]
    def __str__(self):
        for row in self.matrix:
            print(row)
        return f"The column name is: {self.grade_level_list}\nThe course_key is: {self.course_key}"

    #random generate schedule
    def initialize_schedule(self):
        course_key = random_course_key_list(self.course_key)
        count = 0

        for _ in range(self.num_of_period):
            for __ in range(self.num_of_sections):
                self.matrix[__][_]=course_key[count]
                count=count+1
        self.course_key=course_key
        return self
