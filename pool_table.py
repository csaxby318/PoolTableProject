# Week 2 - Day 3-5 - Assignments - Pool Table (Multi-Day Project)

# import datetime module
from datetime import datetime

# create list of 12 pool tables
pool_tables = ["Table_1", "Table_2", "Table_3", "Table_4", "Table_5", "Table_6", "Table_7", "Table_8", "Table_9", "Table_10", "Table_11", "Table_12"]

class PoolTable:
    def __init__(self, name):
        self.table_name = name 
        self.availabile = True
        self.start_time = None
        self.end_time = None

    def check_out_table(self):
        self.availabile = False
        self.start_time = current_time
    
    def check_in_table(self):
        self.availabile = True 
        self.end_time = current_time

    def time_played(self):
        return self.start_time - self.end_time

# create a readable format for the time
now = datetime.now()
current_time = now.strftime("%H:%M")


# display pool tables
def display_tables():
    counter = 0
    for table in pool_tables:
        t = PoolTable(table)
        if t.availabile == True:
            t.availabile = "is available"
        else:
            t.availabile = "is not available"
        print(f"{counter+1}. {t.table_name} {t.availabile}")
        counter += 1

display_tables()

# x = PoolTable(pool_tables[2])
# print(x)
