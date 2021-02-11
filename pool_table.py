# Week 2 - Day 3-5 - Assignments - Pool Table (Multi-Day Project)

# import datetime module
from datetime import datetime
#create a readable format for the time
now = datetime.now()
current_time = now.strftime("%I:%M%p on %m-%d-%Y")

# list for pool tables
pool_tables = []

# class to set properties for pool tables
class PoolTable:
    def __init__(self, name):
        self.table_name = name 
        self.available = True
        self.start_time = None
        self.end_time = None
# class function for checking out a pool table 
    def check_out_table(self):
        self.available = False
        self.start_time = datetime.now()
# class function for checking in a pool table   
    def check_in_table(self):
        self.available = True 
        self.end_time = datetime.now()
# class function for calculating how long a pool table was checked out
    def time_played(self):
        if self.start_time == None:
            return datetime.now() - datetime.now()
        elif self.end_time == None:
            return datetime.now() - self.start_time
        else:
            return self.end_time - self.start_time

# using range function to generate pool table names, then appending those names (along with class properties) to my pool table list
for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

# function to display pool tables
def display_tables():
    for table in range(0, len(pool_tables)):
        t = pool_tables[table]
        if t.available == True:
            t.available = "is available"
            print(f"\nTable {t.table_name} {t.available}")
        elif t.available == False:
            t.available = "is NOT available"
            print(f"\nTable {t.table_name} {t.available} - Checkout Time: {t.start_time} - Play Time: {t.time_played()}")
        else:
            print(f"{t.table_name} {t.available}")


while True: 
    menu = input("""
    1. Display all tables
    2. Check-out a table 
    3. Check-in a table 
    q. Enter q to quit
    Enter your choice: """)
 
    if menu == "1":
        display_tables()
    elif menu == "2":
        display_tables()
        which_table = int(input("Enter the table number: "))
        table = pool_tables[which_table-1]
        if table.available == False:
            print(f"Pool Table {table.table_name} is currently occupied")
        else:
            table.check_out_table()
        display_tables()
    elif menu == "q":
        break



# pool_tables[2].check_out_table()

# display_tables()