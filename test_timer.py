import time
from datetime import date
import csv

#Set Global Variables
start_time = None
today = date.today()
formatted_date = today.strftime('%d-%m-%Y')

#Creating functions to return time when timer is started
def start():
    global start_time
    start_time = time.time()
    formatted_start_time = time.strftime('%H:%M:%S', time.localtime(start_time))  
    return formatted_start_time

#Creating functions to return time when timer is stopped
def stop():
    stop_time = time.time()
    formatted_stop_time = time.strftime('%H:%M:%S', time.localtime(stop_time))
    return formatted_stop_time

#Function to give the difference in time between the start and stop
def difference():
    global start_time
    if start_time is not None:
        return time.time() - start_time
    else:
        return 0

#Function to break down the seconds into H:M:S format
def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

#User inputs
# title = input('Please enter title for this timer: ') 

# begin = input('Press "s" to start the timer: ')
# if begin.lower() == 's':
#     print("Start Time:", start())
    
# pause = input('Press "p" to pause...')

# if pause =='p':
#     print('Pause Time', stop())
    
duration_seconds = difference()
formatted_duration = format_duration(duration_seconds)

print(f'Date: {formatted_date} Session: {title} Duration: {formatted_duration}')



#CSV PRINTING
# csv_date = formatted_date
# csv_title = title
# csv_duration = formatted_duration

# csv_ls = [csv_title, csv_date, csv_duration]

# with open('MOOC Python Course Times_TEST3.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(csv_ls)
# file.close
# print('Data Saved')