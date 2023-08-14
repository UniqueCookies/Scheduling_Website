import sqlite3

#create matrix according to the num of periods and num of classes
def create_matrix(num_period, num_classes):
    schedule = [[0 for _ in range(num_classes)] for _ in range(num_period)]
    return schedule


#sort the into three list
