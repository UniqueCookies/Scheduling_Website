from section import Section

class Schedule:
    def __init__(self, num_of_sections, num_of_period,grade_level_list):
        self.matrix = self.initialize_schedule(num_of_sections, num_of_period,
                    grade_level_list)

    def initialize_schedule(num_of_sections, num_of_period,
                        grade_level_list):
        num_of_grade = len(grade_level_list)


        matrix = 0
        return matrix