from scheduling_website.back_end.course.course_database import *
from scheduling_website.back_end.teacher.teacher_database import *
import itertools
from tabulate import tabulate
class Schedule:
    def __init__(self, num_of_sections, num_of_period,grade_level_list,course_key):
        self.course_key = course_key            #course key will be used to access course_info database
        self.matrix = self.initialize_schedule(num_of_period,num_of_sections)
        self.hcs = self.hard_constraint()  # hard constraints
    #Use the key to get teacher and course name
    def transform_element(self,key):
        teacher_name = retrieve_teacher_name(key)
        course_name = get_course_name(key)
        return (course_name,teacher_name)
    def __str__(self):
        print(f"The number of hard constraints is: {self.hcs}\n")
        table =[]
        for row in self.matrix:
            new_row =[self.transform_element(key) for key in row]
            table.append(new_row)
        num_of_periods = len(self.matrix[0])
        head = [i for i in range(1,num_of_periods+1)]
        format_table = tabulate(table,headers = head,tablefmt="fancy_grid")
        return format_table

    #random generate schedule
    def initialize_schedule(self,num_of_period,num_of_sections):
        course_key = random_course_key_list(self.course_key)
        matrix = [[None for _ in range(num_of_period)] for _ in range(num_of_sections)]

        count = 0
        for period in range(num_of_period):
            for section in range(num_of_sections):
                matrix[section][period]=course_key[count]
                count=count+1
        self.course_key=course_key
        return matrix
    #calculate violation of hard constraints
    def hard_constraint(self):
        count = 0
        num_of_period = len(self.matrix[0])
        num_of_sections = len(self.matrix)
        # checking if the same class is being taught more than once for each section
        def repeating_class():
            count =0
            for section in range(num_of_sections):
                for period1, period2 in itertools.combinations(range(num_of_period), 2):
                    key1 =self.matrix[section][period1]
                    key2 = self.matrix[section][period2]
                    if check_hcs_repeating_course(key1, key2):  #same course name means the section gets the same class twice
                        count = count+1

            return count
        class_repeat = repeating_class()
        #print(f"Repeating class hcs is:{class_repeat}")

        # checking if the teacher is assigned to teach more than one class in the same period
        def repeating_teacher():
            count =0
            for period in range(num_of_period):
                for section1,section2 in itertools.combinations(range(num_of_sections),2):
                    key1 = self.matrix[section1][period]
                    key2 = self.matrix[section2][period]
                    if check_hcs_repeating_teacher(key1,key2):
                            count +=1
            return count
        teacher_repeat = repeating_teacher()
        #print(f"Repeating teacher hcs is:{teacher_repeat}")

        #check if it violates the teacher's availability schedule
        def violate_availability():
            count = 0
            for section in range(num_of_sections):
                for period in range(num_of_period):
                    key = self.matrix[section][period]
                    teacher_name = retrieve_teacher_name(key)       #get teacher name
                    if check_availability(teacher_name, period) is not True:
                        count +=1
            return count

        violation = violate_availability()
        #print(f"Teacher availability violation hcs is:{violation}")

        final_count = class_repeat+teacher_repeat+violation
        self.hcs = final_count
        return final_count

    #get matrix info
    def get_info(self, row, col):
        return self.matrix[row][col]

    #single mutation step
    def swap_element(self, row1, col1, row2, col2):
        temp = self.matrix[row1][col1]
        self.matrix[row1][col1]=self.matrix[row2][col2]
        self.matrix[row2][col2]=temp

        #update hcs
        self.hcs=self.hard_constraint()



