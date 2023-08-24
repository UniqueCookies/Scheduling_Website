import itertools

from tabulate import tabulate

from back_end.course.course_database import get_course_key_list, check_hcs_repeating_teacher
from back_end.section import Section, transform_element, display_as_table, hard_constraint, repeating_teacher
import numpy as np


def initialize_schedule(num_of_period, grade_level_list):
    num_of_grades = len(grade_level_list)
    temp = []
    for i in range (num_of_grades):
        grade = grade_level_list[i][0]
        course_key = get_course_key_list(grade)
        num_of_sections = grade_level_list[i][1]

        section = Section(num_of_sections, num_of_period, grade, course_key)
        temp.append([section])
    return temp


def repeating_teacher_schedule(schedule, num_of_period,grade_level_list):
    num_of_grades = len(schedule)
    temp = []
    for i in range (num_of_grades):
        num_of_sections = grade_level_list[i][1]
        for j in range (num_of_sections):
            temp.append(schedule[i][0].matrix[j])
    num_of_sections = num_of_grades * num_of_sections
    count = repeating_teacher(temp, num_of_sections, num_of_period)
    return count


class Schedule:
    def __init__(self, num_of_period, grade_level_list):
        self.grade_level_list = grade_level_list
        self.num_of_period = num_of_period
        self.matrix = initialize_schedule(num_of_period,
                                          grade_level_list)
        self.hcs = self.update_hcs()

    def __str__(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i][0])
        return f"Schedule's teacher conflict is: {self.hcs}\n"

    def update_hcs(self):
        hcs = repeating_teacher_schedule(self.matrix,self.num_of_period,self.grade_level_list)
        num_of_grades=len(self.matrix)
        for i in range (num_of_grades):
            hcs += self.matrix[i][0].hcs
        self.hcs = hcs
        return hcs
