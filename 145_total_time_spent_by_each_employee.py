# Create a new column with time difference (out - in). Group by the event_date and employee ID to get the 
# total time spent and return DF.

import pandas as pd
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    return employees.rename(columns = {'event_day': 'day'})