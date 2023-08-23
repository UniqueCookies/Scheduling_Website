from back_end.course.course_database import *
from back_end.course.multiple_course import get_multiple_course_id, if_multiple
from back_end.teacher.multiple_course_teacher import multiple_course_info
from back_end.teacher.teacher_database import *
import itertools
from tabulate import tabulate


def find_multiple(grade_level):
    multiple_course, teacher_name = get_multiple_course_id(grade_level)
    availability = multiple_course_info(teacher_name)
    return [multiple_course, availability]


# Use the key to get teacher and course name
def transform_element(key):
    teacher_name = retrieve_teacher_name(key)
    course_name = get_course_name(key)
    return (course_name, teacher_name)


def display_as_table(matrix,grade_list):
    table = []
    for i, row in enumerate(matrix):
        new_row = [grade_list[i]]+[transform_element(key) for key in row]
        table.append(new_row)
    num_of_periods = len(matrix[0])
    head = ["Grades"]+[str(i) for i in range(1, num_of_periods + 1)]
    format_table = tabulate(table, headers=head, tablefmt="fancy_grid")
    return format_table


class Section:
    def __init__(self, num_of_sections, num_of_period,
                 grade_level, course_key):
        self.course_key = (
            course_key  # to access course_info database
        )
        self.multiple = find_multiple(grade_level)
        self.matrix = self.initialize_section(num_of_period, num_of_sections)
        self.hcs = self.hard_constraint()  # hard constraints
        self.grade_level = grade_level
        self.num_of_sections = num_of_sections

    def __str__(self):
        print(f"The number of hard constraints is: {self.hcs}\n")
        grade_list = [f"grade {self.grade_level}" for i in range (self.num_of_sections)]
        format_table = display_as_table(self.matrix,grade_list)
        return format_table

    # random generate section
    def initialize_section(self, num_of_period, num_of_sections):
        course_key = random_course_key_list(self.course_key)
        matrix = [[None for _ in range(num_of_period)]
                  for _ in range(num_of_sections)]
        course_key = self.fill_in_multiple(matrix, course_key)
        count = 0

        for period in range(num_of_period):
            for section in range(num_of_sections):
                if matrix[section][period] is not None:
                    break
                matrix[section][period] = course_key[count]
                count = count + 1
        self.course_key = course_key
        return matrix

    def fill_in_multiple(self, matrix, course_key):
        item = random.choice(self.multiple[1])
        course_list = self.multiple[0]
        for i in range(len(matrix)):
            matrix[i][item] = course_list[i]
        course_key = [item for item in course_key if item not in course_list]
        return course_key

    # calculate violation of hard constraints
    def hard_constraint(self):
        count = 0
        num_of_period = len(self.matrix[0])
        num_of_sections = len(self.matrix)

        # checking if the same class is being taught
        # more than once for each section
        def repeating_class():
            count = 0
            for section in range(num_of_sections):
                for period1, period2 \
                        in itertools.combinations(range(num_of_period), 2):
                    key1 = self.matrix[section][period1]
                    key2 = self.matrix[section][period2]
                    # each section cannot get the same class twice
                    if check_hcs_repeating_course(
                            key1, key2
                    ):
                        count = count + 1

            return count

        class_repeat = repeating_class()

        # print(f"Repeating class hcs is:{class_repeat}")
        # checking if the teacher is assigned to teach
        # more than one class in the same period

        def repeating_teacher():
            count = 0
            for period in range(num_of_period):
                for section1, section2 in itertools.combinations(
                        range(num_of_sections), 2
                ):
                    key1 = self.matrix[section1][period]
                    key2 = self.matrix[section2][period]
                    if check_hcs_repeating_teacher(key1, key2):
                        count += 1
            return count

        teacher_repeat = repeating_teacher()

        # print(f"Repeating teacher hcs is:{teacher_repeat}")

        # check if it violates the teacher's availability section
        def violate_availability():
            count = 0
            for section in range(num_of_sections):
                for period in range(num_of_period):
                    key = self.matrix[section][period]
                    # get teacher name
                    teacher_name = retrieve_teacher_name(key)
                    if check_availability(teacher_name, period) is not True:
                        count += 1
            return count

        violation = violate_availability()
        # print(f"Teacher availability violation hcs is:{violation}")

        final_count = class_repeat + teacher_repeat + violation
        self.hcs = final_count
        return final_count

    # get the course_key info from the matrix
    def get_info(self, row, col):
        return self.matrix[row][col]

    # single mutation step by swapping random two cells
    def swap_element(self, row1, col1, row2, col2):
        temp = self.matrix[row1][col1]
        self.matrix[row1][col1] = self.matrix[row2][col2]
        self.matrix[row2][col2] = temp

        # update hcs
        self.hcs = self.hard_constraint()

    def swap_column(self, col1, col2):
        for row in self.matrix:
            row[col1], row[col2] = row[col2], row[col1]
        self.hcs = self.hard_constraint()

    # check if this teacher is teaching more than one class in the same period
    def check_if_clash(self, row1, col1):
        value = self.matrix[row1][col1]
        for row in range(len(self.matrix)):
            if row == row1:
                continue
            if check_hcs_repeating_teacher(self.matrix[row][col1], value):
                return True
        return False

    # return True if it is multiple
    def check_if_double(self, row1, col1):
        key = self.matrix[row1][col1]
        return if_multiple(key)

    def check_if_swap_double(self, col1, col2):
        availability_list = self.multiple[1]
        if col1 in availability_list and col2 in availability_list:
            return True
