import customtkinter
import time

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.title('MOOC Timer Tests')
app.geometry('300x300')
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(2, weight=1)

# Set Global Variables
start_time = None
is_running = False

def start():
    global start_time, is_running
    start_time = time.time()
    is_running = True
    update_duration_label()

def stop():
    global is_running
    is_running = False

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
        duration_label.configure(text=f"Duration: {formatted_duration}")
        app.after(1000, update_duration_label)  # Schedule the function to run again after 1000 milliseconds (1 second)

top_label = customtkinter.CTkLabel(app, text='MOOCFi Session Timer', font=('Helvetica', 18))
top_label.grid(pady=10, column=0)

title = customtkinter.CTkEntry(app, placeholder_text='Enter MOOCFI session', font=('Helvetica', 12), justify='center')
title.grid(pady=10, row=1, column=0)

submit_button = customtkinter.CTkButton(app, text='Submit')      
submit_button.grid(pady=10, row=1, column=1)

start_button = customtkinter.CTkButton(app, text='Start', font=('Helvetica', 14), command=start)
start_button.grid(pady=10, row=2, column=0)

stop_button = customtkinter.CTkButton(app, text='Stop', font=('Helvetica', 14), command=stop)
stop_button.grid(pady=10, row=2, column=1)

duration_label = customtkinter.CTkLabel(app, text="Duration: 00:00:00", font=('Helvetica', 14))
duration_label.grid(pady=10, row=3, column=0, columnspan=2)

app.mainloop()


