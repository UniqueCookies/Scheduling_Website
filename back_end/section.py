from back_end.course.course_database import *
from back_end.course.special_course import get_course_id_special, if_special
from back_end.teacher.special_course_teacher import multiple_course_info, get_availability_double
from back_end.teacher.teacher_database import *
import itertools
from tabulate import tabulate


def check_occupied(matrix, row, col):
    if matrix[row][col] is None:
        return True
    else:
        return False


def find_multiple(grade_level):
    multiple_course, teacher_name = get_course_id_special(grade_level, 1)
    availability = multiple_course_info(teacher_name)
    return [multiple_course, availability]


def find_double(grade_level):
    double_course, teacher_name = get_course_id_special(grade_level, 2)
    if not len(double_course) == 0 and not len(teacher_name) == 0:
        double_course, availability = get_availability_double(teacher_name, double_course)
        double_course_matrix = [t for t in double_course]
        availability_matrix = [list(t) for t in availability]
        return [double_course_matrix, availability_matrix]
    return False


# Use the key to get teacher and course name
def transform_element(key):
    teacher_name = retrieve_teacher_name(key)
    course_name,course_type = get_course_name(key)
    return course_name, teacher_name


# checking if the same class is being taught
# more than once for each section
def repeating_class(matrix, num_of_sections, num_of_period):
    count = 0
    for section in range(num_of_sections):
        for period1, period2 \
                in itertools.combinations(range(num_of_period), 2):
            key1 = matrix[section][period1]
            key2 = matrix[section][period2]
            # each section cannot get the same class twice
            if check_hcs_repeating_course(
                    key1, key2
            ):
                count = count + 1
    return count


# print(f"Repeating class hcs is:{class_repeat}")
# checking if the teacher is assigned to teach
# more than one class in the same period

def repeating_teacher(matrix, num_of_sections, num_of_period):
    count = 0
    for period in range(num_of_period):
        for section1, section2 in itertools.combinations(
                range(num_of_sections), 2
        ):
            key1 = matrix[section1][period]
            key2 = matrix[section2][period]
            if check_hcs_repeating_teacher(key1, key2):
                count += 1
    return count


# check if it violates the teacher's availability section
def violate_availability(matrix, num_of_sections, num_of_period):
    count = 0
    for section in range(num_of_sections):
        for period in range(num_of_period):
            key = matrix[section][period]
            # get teacher name
            teacher_name = retrieve_teacher_name(key)
            if check_availability(teacher_name, period) is not True:
                count += 1
    return count


# calculate violation of hard constraints
def hard_constraint(matrix):
    if matrix is None:
        return 0
    num_of_period = len(matrix[0])
    num_of_sections = len(matrix)

    class_repeat = repeating_class(matrix, num_of_sections, num_of_period)
    teacher_repeat = repeating_teacher(matrix, num_of_sections, num_of_period)
    violation = violate_availability(matrix, num_of_sections, num_of_period)
    final_count = class_repeat + teacher_repeat + violation
    return final_count


def display_as_table(matrix, grade_list):
    if matrix is None:
        return f"This section is empty"
    table = []
    for i, row in enumerate(matrix):
        new_row = [grade_list[i]] + [transform_element(key) for key in row]
        table.append(new_row)
    num_of_periods = len(matrix[0])
    head = ["Grades"] + [str(i) for i in range(1, num_of_periods + 1)]
    format_table = tabulate(table, headers=head, tablefmt="fancy_grid")
    return format_table


class Section:
    def __init__(self, num_of_sections, num_of_period,
                 grade_level, course_key):
        self.course_key = (
            course_key  # to access course_info database
        )
        self.grade_level = grade_level
        self.num_of_sections = num_of_sections
        self.num_of_period = num_of_period
        self.multiple = find_multiple(grade_level)
        self.double = find_double(grade_level)
        self.matrix = self.initialize_section(num_of_period, num_of_sections)
        self.hcs = self.update_hcs()  # hard constraints

    def __str__(self):
        print(f"The number of hard constraints is: {self.hcs}\n")
        # print(f"The number of double is: {self.double}\n")
        grade_list = [f"grade {self.grade_level}" for i in range(self.num_of_sections)]
        format_table = display_as_table(self.matrix, grade_list)
        return format_table

    # random generate section
    def initialize_section(self, num_of_period, num_of_sections):
        if not self.course_key:
            return None
        course_key = random_course_key_list(self.course_key)
        matrix = [[None for _ in range(num_of_period)]
                  for _ in range(num_of_sections)]
        course_key = self.fill_in_multiple(matrix, course_key)
        course_key = self.fill_in_double(matrix, course_key)
        if not course_key:
            return None
        count = 0

        for period in range(num_of_period):
            for section in range(num_of_sections):
                if matrix[section][period] is None:
                    matrix[section][period] = course_key[count]
                    count = count + 1
        return matrix

    def update_hcs(self):
        if self.matrix is None:
            return 0
        hcs = hard_constraint(self.matrix)
        self.hcs = hcs
        return hcs

    def fill_in_multiple(self, matrix, course_key):
        if self.multiple[1] is None:
            return False
        item = random.choice(self.multiple[1])
        course_list = self.multiple[0]
        for i in range(len(matrix)):
            matrix[i][item] = course_list[i]
        course_key = [item for item in course_key if item not in course_list]
        return course_key

    # Each course needs to be added in twice and back to back starting with even number period index
    # Should be added to different section
    def fill_in_double(self, matrix, course_key):
        if not self.double:
            return None
        course_list = self.double[0]
        availability = self.double[1]

        for i in range(len(availability)):
            available_period = availability[i]
            j = 0
            while j < len(available_period):
                period = available_period[j]
                section = 0
                while section < self.num_of_sections:
                    if all(check_occupied(matrix, section, p) for p in (period, period + 1)):
                        # fill in the cell
                        course_to_fill = course_list[i]
                        matrix[section][period] = course_to_fill
                        matrix[section][period + 1] = course_to_fill
                        course_key.remove(course_to_fill)
                        section = self.num_of_sections
                        j = len(available_period) + 1
                    else:
                        section += 1
                j = j + 2
        if any(course in course_key for course in course_list):
            return False

        # course_key = [item for item in course_key if item not in course_list]
        return course_key

    # get the course_key info from the matrix
    def get_info(self, row, col):
        return self.matrix[row][col]

    # single mutation step by swapping random two cells
    def swap_element(self, row1, col1, row2, col2):
        temp = self.matrix[row1][col1]
        self.matrix[row1][col1] = self.matrix[row2][col2]
        self.matrix[row2][col2] = temp

        # update hcs
        self.hcs = self.update_hcs()
        return True

    def swap_column(self, col1, col2):
        for row in self.matrix:
            row[col1], row[col2] = row[col2], row[col1]
        self.hcs = self.update_hcs()
        return True

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
    def check_if_special(self, row1, col1):
        key = self.matrix[row1][col1]
        return if_special(key)

    def check_if_swap_multiple(self, col1, col2):
        availability_list = self.multiple[1]
        if col1 in availability_list and col2 in availability_list:
            return True

    def check_if_swap_double(self,row1,col1,row2,col2):
        key1 = self.get_info(row1, col1)
        key2 = self.get_info(row2, col2)

        course_list = self.double[0]
        availability_list = self.double[1]

        position1 =100
        position2 = 100
        if key1 in course_list:
            position1 = course_list.index(key1)
        if key2 in course_list:
            position2 = course_list.index(key2)

        if not position1==100 and not position2==100:
                return None
        #if position one is double
        if not position1==100 and col2 in availability_list[position1]:
                return self.swap_double(row1,col1,row2,col2)
        if not position2==100 and col1 in availability_list[position2]:
                return self.swap_double(row1,col1,row2,col2)
        return None

    def swap_double(self,row1,col1,row2,col2):
        temp = self.matrix[row1][col1]
        self.matrix[row1][col1]=self.matrix[row2][col2]
        self.matrix[row1][col1+1]=self.matrix[row2][col2]
        self.matrix[row2][col2]=temp
        self.matrix[row2][col2+1] = temp
        return True

    def double_mutation(self):
        course_list = self.double[0]
        availability_list = self.double[1]

        for course in course_list:
            position = course_list.index(course)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    if self.matrix[i][j] == course:
                        row1 = i
                        col1 = j
            new_col = random.choice(availability_list[position])
            new_col = (new_col//2)*2
            col1 = (col1//2)*2
            self.swap_double(row1, col1, row1, new_col)

        return True
