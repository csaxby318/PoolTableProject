# Week 2 - Day 3-5 - Assignments - Pool Table (Multi-Day Project)

# import json module for creation of log file. Create empty list to use in json file
import json
tables = []

# import datetime module to capture start, end and play time
from datetime import datetime
# create a readable formate for the date only, later used to generate json log file name
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
            formatted_start_time = t.start_time.strftime("%I:%M%p on %m-%d-%Y")
            print(f"\nTable {t.table_name} {is_not_available} - Checkout Time: {formatted_start_time} - Play Time: {t.time_played()}")


while True: 
    # what the admin sees
    print(f"\n  Frankie's Billiards Club")
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
        # display all of the tables
        display_tables()
        # ask the admin which table they would like to check
        which_table = int(input(f"\nCheckout table number: "))
        table = pool_tables[which_table-1]
        # if the table is already checked out, display message
        if table.available == False:
            print(f"\n ******** PLEASE BE ADVISED ********")
            print(f"/// Pool Table {table.table_name} is currently occupied ///")
        # if table is not checked out, check it out
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
                formatted_start_time = t.start_time.strftime("%I:%M%p on %m-%d-%Y")
                print(f"\nTable {t.table_name} {is_not_available} - Checkout Time: {formatted_start_time} - Play Time: {t.time_played()}")
        # ask the admin which table they would like to check-in
        which_table = int(input(f"\nCheck-in table number: "))
        table = pool_tables[which_table-1]
        # if the table is already checked in, display message
        if table.available == True:
            print(f"\n ******** PLEASE BE ADVISED ********")
        # if table is not checked in, check it in
        else:
            table.check_in_table()
        # format the start, end and play time for better view in the log file
        try:
            formatted_start_time = table.start_time.strftime("%I:%M%p on %m-%d-%Y")
            formatted_end_time = table.end_time.strftime("%I:%M%p on %m-%d-%Y")
            play_time = table.time_played()
            formatted_play_time = str(play_time)
        # create/write to json log file the required info as the table is checked in
            with open(f"{formatted_date}.json", "w") as file_object:
                table = {"table": table.table_name, "started": formatted_start_time, "ended": formatted_end_time, "playtime": formatted_play_time}
                tables.append(table)
                json.dump(tables, file_object)
        # if the table is already checked in, display message
        except AttributeError:
            print(f"/// Pool Table {table.table_name} is already checked in ///")
        # display all of the tables after check-in is completed     
        display_tables()
    # menu option to quit the app
    elif menu == "q" or menu == "Q":
        break
    # if an invalid choice is made at the menu, the below message will display
    else:
        print(f"{menu} is not a valid choice. Please try again")