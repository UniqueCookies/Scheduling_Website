from tabulate import tabulate

from back_end.course.course_database import get_course_key_list
from back_end.section import Section, transform_element, display_as_table
import numpy as np


def initialize_schedule(num_of_sections, num_of_period,
                        grade_level_list):
    num_of_grades = len(grade_level_list)
    temp = []
    for grade in grade_level_list:
        course_key = get_course_key_list(grade)
        section = Section(num_of_sections, num_of_period, grade, course_key)
        temp.append(section.matrix)
    merge_matrix =[]
    for matrix_pair in temp:
        for row in matrix_pair:
            merge_matrix.append(row)
    return merge_matrix


def calculate_hcs(matrix):

    return 0


class Schedule:
    def __init__(self, num_of_sections, num_of_period, grade_level_list):
        self.matrix = initialize_schedule(num_of_sections, num_of_period,
                                          grade_level_list)
        self.grade_level_list = grade_level_list
        self.num_of_sections = num_of_sections
        self.hcs = calculate_hcs(self.matrix)

    def __str__(self):
        temp_list = [x for x in self.grade_level_list for _ in range(self.num_of_sections)]
        grade_list = [f"grade {temp_list[i]}" for i in range(len(temp_list))]
        format_table = display_as_table(self.matrix,grade_list)
        return format_table
