from scheduling_website.back_end.course.course_database import *
class Schedule:
    def __init__(self, num_of_sections, num_of_period,grade_level_list,course_key,hcs):
        self.num_of_sections = num_of_sections  #rows/what are course sections
        self.num_of_period = num_of_period      #column/num of period used in school, generally 6
        self.grade_level_list=grade_level_list  #which grade level is invovled, will update this later
        self.course_key = course_key            #course key will be used to access course_info database
        self.hcs = hcs                          #hard constraints
        self.matrix = [[None for _ in range(num_of_period)] for _ in range(num_of_sections)]
    def __str__(self):
        for row in self.matrix:
            print(row)
        return f"The column name is: {self.grade_level_list}\nThe course_key is: {self.course_key}\nThe number of hard constraints is: {self.hcs}"

    #random generate schedule
    def initialize_schedule(self):
        course_key = random_course_key_list(self.course_key)
        count = 0

        for period in range(self.num_of_period):
            for section in range(self.num_of_sections):
                self.matrix[section][period]=course_key[count]
                count=count+1
        self.course_key=course_key
        return self

    #calculate violation of hard constraints
    def hard_constraint(self):
        count = 0
        def repeating_class():

            count =0
        return count
