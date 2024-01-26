# first part
import pandas as pd
from datetime import datetime

excel_file_path = '/content/Assignment_Timecard.xlsx'  
df = pd.read_excel(excel_file_path)

consecutive_days_threshold = 7
current_date = None
consecutive_days_counter = 0
consecutive_days_employees = []

for index, row in df.iterrows():
    if pd.notna(row['Time']):
        try:
            date = row['Time'].date()  
        except AttributeError:
            print(f"Issue with date parsing at index {index}, skipping this entry.")
            continue

        day_difference = (date - current_date).days if current_date else 0
        if day_difference == 0:
            pass  
        elif day_difference == 1:
            consecutive_days_counter += 1
        else:
            consecutive_days_counter = 1 

        current_date = date  

        
        if consecutive_days_counter == consecutive_days_threshold:
            start_day_index = index - consecutive_days_threshold + 1
            start_date = df.loc[start_day_index, 'Pay Cycle Start Date']
           
            employee_name = row['Employee Name']
            Position_ID = row['Position ID']
            consecutive_days_employees.append((employee_name, Position_ID))

            
            consecutive_days_counter = 0
            current_date = None
for employee_info in consecutive_days_employees:
    print(f"Employee Name: {employee_info[0]}, Position ID: {employee_info[1]}")




#second part

import pandas as pd

# Read the Excel file
file_path = '/content/Assignment_Timecard.xlsx'  
df = pd.read_excel(file_path)

# Initialize variables
current_position_id = None
total_hours = 0
employees_outside_range = []

# Function to reset and print total hours
def reset_and_print():
    if total_hours < 1 or total_hours > 10:
        employees_outside_range.append((current_position_id, current_employee_name, total_hours))

# Iterate through the rows
for index, row in df.iterrows():
    position_id = row['Position ID']
    timecard_hours = row['Timecard Hours (as Time)']
    employee_name = row['Employee Name']

    # Check if Position ID has changed
    if position_id != current_position_id:
        # Reset and print total hours for the previous position ID
        reset_and_print()

        # Reset variables for the new Position ID
        current_position_id = position_id
        current_employee_name = employee_name
        total_hours = 0

    if pd.notna(timecard_hours):
        try:
            hours, minutes, seconds = map(int, timecard_hours.split(':'))
            total_hours += hours + minutes / 60 + seconds / 3600
        except (ValueError, TypeError):
            # Handle different time formats or empty values
            pass

# Check for the last row after the loop
            reset_and_print()

# Print employees outside the specified range
for position_id, employee_name, hours in employees_outside_range:
    print(f"Position ID: {position_id}, Employee Name: {employee_name}")
