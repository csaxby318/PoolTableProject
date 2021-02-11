# Week 2 - Day 3-5 - Assignments - Pool Table (Multi-Day Project)

# import json module for creation of log file. Create empty list to use in json file
import json
tables = []

# import datetime module to capture start, end and play time
from datetime import datetime
#create a readable format for the time
#time_now = datetime.now()
# formatted_time = time_now.strftime("%I:%M%p on %m-%d-%Y")
# create a readable formate for the date
date_now = datetime.now()
current_date = date_now.date()
formatted_date = current_date.strftime("%m-%d-%Y")

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
            is_available = "is available"
            print(f"\nTable {t.table_name} {is_available}")
        elif t.available == False:
            is_not_available = "is NOT available"
            print(f"\nTable {t.table_name} {is_not_available} - Checkout Time: {t.start_time} - Play Time: {t.time_played()}")


while True: 
    menu = input("""
    1. Display all tables
    2. Check-out a table 
    3. Check-in a table 
    q. Enter q to quit
    Enter your choice: """)
    
    # menu option 1 is to display the tables, along with their status
    if menu == "1":
        display_tables()
    
    # menu option 2 is to checkout a table    
    elif menu == "2":
        display_tables()
        which_table = int(input("Checkout table number: "))
        table = pool_tables[which_table-1]
        if table.available == False:
            print(f"\n /// Pool Table {table.table_name} is currently occupied ///")
        else:
            table.check_out_table()
            display_tables()
    
    # menu option 3 is to check-in a table and to create a log file 
    elif menu == "3":
        # display only the tables that are currently checked out
        for table in range(0, len(pool_tables)):
            t = pool_tables[table]
            if t.available == False:
                is_not_available = "is NOT available"
                print(f"\nTable {t.table_name} {is_not_available} - Checkout Time: {t.start_time} - Play Time: {t.time_played()}")
        # ask the admin which table they would like to check-in, then check-in that table
        which_table = int(input("Check-in table number: "))
        table = pool_tables[which_table-1]
        table.check_in_table()
        # format the start, end and play time for better view in the log file
        formatted_start_time = table.start_time.strftime("%I:%M%p on %m-%d-%Y")
        formatted_end_time = table.end_time.strftime("%I:%M%p on %m-%d-%Y")
        play_time = table.time_played()
        formatted_play_time = str(play_time)
        # create/write to file the required info as the table is checked in
        with open(f"{formatted_date}.json", "w") as file_object:
            table = {"table": table.table_name, "started": formatted_start_time, "ended": formatted_end_time, "playtime": formatted_play_time}
            tables.append(table)
            json.dump(tables, file_object)
    
    
    elif menu == "q":
        break

    else:
        print(f"{menu} is not a valid choice. Please try again")


# pool_tables[2].check_out_table()

# display_tables()