import random
import sqlite3

#create matrix according to the num of periods and num of classes
def create_matrix(num_period, num_sections):
    schedule = [[0 for _ in range(num_sections)] for _ in range(num_period)]
    return schedule

#sort the into three list
def random_list(list,population):
    rows = len(population)
    cols = len(population[0])
    random.shuffle(list)
    tuple_index = 0
    for row in range(rows):
        for col in range(cols):
            population[row][col] = list[tuple_index]
            tuple_index += 1
    return population