# Week 2 - Day 3-5 - Assignments - Pool Table (Multi-Day Project)

# import datetime module
from datetime import datetime
#create a readable format for the time
now = datetime.now()
current_time = now.strftime("%H:%M")

# list for pool tables
pool_tables = []

# class to set properties for pool tables
class PoolTable:
    def __init__(self, name):
        self.table_name = name 
        self.availabile = True
        self.start_time = None
        self.end_time = None
# class function for checking out a pool table 
    def check_out_table(self):
        self.availabile = False
        self.start_time = current_time
# class function for checking in a pool table   
    def check_in_table(self):
        self.availabile = True 
        self.end_time = current_time
# class function for calculating how long a pool table was checked out
    def time_played(self):
        return self.start_time - self.end_time

# using range function to generate pool table names, then appending those names (along with class properties) to my pool table list
for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

# function to display pool tables
def display_tables():
    for table in range(0, len(pool_tables)):
        t = pool_tables[table]
        if t.availabile == True:
            t.availabile = "is available"
        else:
            t.availabile = "is NOT available"
        print(f"\nTable {t.table_name} {t.availabile} - Checkout time is {t.start_time}")


test = pool_tables[2]
test.check_out_table()


display_tables()

# x = PoolTable(pool_tables[2])
# print(x)
