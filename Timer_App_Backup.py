import customtkinter
import csv
import time
from datetime import date

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.title('MOOC Timer Tests')
app.geometry('300x300')
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(2, weight=1)

#Set Global Variables
start_time = None
is_running = False
duration_seconds = 0
today = date.today()
formatted_date = today.strftime('%d-%m-%Y')

def submit():
    print(title.get())
    
def start():
    global start_time, is_running
    start_time = time.time()
    is_running = True
    formatted_start_time = time.strftime('%H:%M:%S', time.localtime(start_time))
    print(formatted_start_time)
    update_duration_label()
    return formatted_start_time

def stop():
    global is_running
    is_running = False
    duration_seconds = difference()
    return duration_seconds
    #formatted_stop_time = time.strftime('%H:%M:%S', time.localtime(stop_time))
    #print(formatted_stop_time)
    #return formatted_stop_time

def difference():
    global start_time
    if start_time is not None:
        return time.time() - start_time
    else:
        return 0
    
def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def update_duration_label():
    if is_running:
        duration_seconds = difference()
        formatted_duration = format_duration(duration_seconds)
        duration_label.configure(text=f'Duration: {formatted_duration}')
        app.after(1000, update_duration_label)
    
top_label = customtkinter.CTkLabel(app, text='MOOCFi Session Timer', font=('Helvetica', 18))
top_label.grid(pady=10, column=0, columnspan =3)

title = customtkinter.CTkEntry(app, placeholder_text='Enter MOOCFI session', font=('Helvetica', 12), justify='center')
title.grid(pady=10, row=1, column=0,)

submit_button = customtkinter.CTkButton(app, text='Submit', command=submit, fg_color='steelblue1', hover_color='steelblue4')      
submit_button.grid(pady=10, row=1, column=1, sticky='w')

start_button = customtkinter.CTkButton(app, text='Start', font=('Helvetica', 14), command=start, fg_color='lime green', hover_color='forest green')
start_button.grid(pady=10, row=2, column=0)

stop_button = customtkinter.CTkButton(app, text='Stop', font=('Helvetica', 14), command=stop, fg_color='firebrick1', hover_color='firebrick4')
stop_button.grid(pady=10, row=2, column=1)

duration_label = customtkinter.CTkLabel(app, text='Duration: 00:00:00', font=('Helvetica', 14))
duration_label.grid(pady=10, row=3, column=0, columnspan=2)

def log_press():
    log_label.configure(text='Data Saved')
    
log_label = customtkinter.CTkLabel(app, text="")
log_label.grid(pady=10, row=4, column=0, columnspan=2)



def log_to_csv():
    global duration_seconds
    formatted_duration = format_duration(stop())
    with open('MOOC Python Course Session Times.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([formatted_date, title.get(), formatted_duration])
        file.close
        print('Data Saved')

log_button = customtkinter.CTkButton(app, text='Log', command=lambda: [log_to_csv(), log_press()], fg_color='steelblue1', hover_color='steelblue4',)
log_button.grid(pady=10, row=6, column=0, columnspan=2)


app.mainloop()
