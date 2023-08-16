class Schedule:
    def __init__(self, num_of_sections, num_of_period,grade_level_list):
        self.num_of_sections = num_of_sections
        self.num_of_period = num_of_period
        self.grade_level_list=grade_level_list
        self.matrix = [[None for _ in range(num_of_period)] for _ in range(num_of_sections)]
    def __str__(self):
        for row in self.matrix:
            print(row)
        return f"The column name is: {self.grade_level_list}"

    #random generate schedule
    def initialize_schedule(self):
        for _ in range(self.num_of_period):
            for __ in range(self.num_of_sections):
                self.matrix[__][_]=1
        return self
