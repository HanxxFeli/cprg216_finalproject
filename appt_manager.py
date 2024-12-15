"""
Hair So Long Appointment Management System Final Project
================================

Description:
This program is a comprehensive appointment management system for a hair salon, 
"Hair So Long". It facilitates scheduling, managing, and tracking client appointments. 
The system offers functionalities to load and save appointments from/to files, 
calculate total fees, and modify or cancel bookings as needed. Users interact 
with an intuitive menu to handle appointment-related tasks.

Features:
- Create a weekly calendar with available appointment slots.
- Schedule new appointments with specific client details.
- Search for appointments by client name or day of the week.
- Modify or cancel existing appointments.
- Calculate total fees for a specific day or for an entire week.
- Load and save appointments from/to external files.

Modules Used:
- `appointment`: Custom module for handling Appointment class and related operations.
- `os`: For file system interaction to load/save appointments.

Constants:
- `OPTION`: Defines the menu options available in the program.
- `DAY_OF_WEEK`: List of days when the salon operates.
- `AVAIL_HOURS`: Defines the available hours for appointments.
- `DOUBLE_DASH`, `SINGLE_DASH`: Formatting constants for clean output display.

Functions:
- `create_weekly_calendar(appt_list)`: Initializes the weekly calendar with empty appointments.
- `schedule_an_appointment(appt_list)`: Adds a new appointment to the calendar.
- `find_appointment_by_time(appt_list, day, start_hour)`: Searches for an appointment by time.
- `cancel_an_appointment(appt_list)`: Cancels a booked appointment.
- `change_appointment_by_day_time(appt_list)`: Modifies an existing appointment.
- `calculate_fees_per_day(appt_list)`: Computes the total fees for a specified day.
- `calculate_weekly_fees(appt_list)`: Computes the total fees for the week.
- `save_scheduled_appointments(appt_list)`: Saves scheduled appointments to a file.
- `load_scheduled_appointments(appt_list)`: Loads appointments from a file.
- `print_menu()`: Displays the menu and handles user navigation.
- Additional helper functions for input validation and data manipulation.

How to Use:
1. Run the program.
2. Follow the on-screen menu to schedule, manage, or view appointments.
3. Save data before exiting to retain appointment records.

Author: Hans Feliciano, Enzo Torres, Minh Tam Nguyen, Cole Andrews
Date: December 14, 2024
"""


import appointment as ap
import os
OPTION = {'1':'Schedule an appointment',
          '2':'Find appointment by name', 
          '3':'Print calendar for a specific day',
          '4':'Cancel an appointment',
          '5':'Change an appointment',
          '6':'Calculate total fees for a day',
          '7':'Calculate total weekly fees',
          '0':'Exit the system'}
DAY_OF_WEEK = ['Monday','Tuesday', "Wednesday", "Thursday", "Friday", "Saturday"]
AVAIL_HOURS = [9, 10, 11, 12, 13, 14, 15, 16]
DOUBLE_DASH = '=' * 38
SINGLE_DASH = '-' * 85

def load_scheduled_appointments(appt_list):
    """
    Loads scheduled appointments from a file. Prompts the user to input a filename, validates its existence, and processes 
    each line to schedule appointments. Each appointment is updated with relevant details.

    Parameters:
        appt_list (list): List of appointment objects.

    Returns:
        int: Number of appointments scheduled.

    Note:
        The file should contain appointment details in the format:
        <client name>,<client phone>,<apppointment type>,<day of week>,<start hour>
        If the file does not exist, the user will be repeatedly prompted to provide a valid filename.
    """
    file_name = input('Enter appointment filename: ')
    while os.path.exists(file_name) == False:
        file_name = input('File not found. Re-enter appointment filename: ')
    file = open(file_name,'r')
    scheduled_appt_num = 0
    for line in file:
        line = line.rstrip()
        attributes = line.split(',')
        appt = find_appointment_by_time(appt_list, attributes[3], int(attributes[4]))
        appt.schedule(attributes[0],attributes[1], int(attributes[2]))
        scheduled_appt_num += 1
    return scheduled_appt_num
      
def schedule_an_appointment(appt_list):
    """
    Schedules an appointment for a client if the specified time slot is available. 
    Prompts the user to input a day of the week, start hour, client details, 
    and appointment type. If the selected time slot is free, the appointment 
    is scheduled and added to the appointment list.

    Parameters:
        appt_list (list): List of appointment objects.

    Returns:
        object: The newly scheduled appointment object if successful, or `None` 
                if the time slot is already booked.

    Note:
        - Uses helper functions like `input_day_of_week`, `input_start_hour`, 
          and `find_appointment_by_time` to handle input and search for the
          corresponding appointment.
        - Displays available appointment types with descriptions and prices.
        - Prints a message indicating success or failure based on slot availability.
    """
    day = input_day_of_week("\n** Schedule an appointment **\nEnter day of week: ")
    start_hour = input_start_hour('Enter start hour (24 hour clock): ')
    if start_hour != None:
        appt = find_appointment_by_time(appt_list, day, start_hour)
        if appt.get_client_name() == '':
            client_name = input('Client Name: ').title()
            client_phone = input('Client Phone: ')
            print('\nAppointment types')
            for index in range(1,5):
                print(f'{index:>4d}: {ap.Appointment.APPT_TYPE_DESC[index]} ${ap.Appointment.APPT_TYPE_PRICES[index]}')
            appt_type = int(input('Type of Appointment: '))
            new_apt = appt.schedule(client_name, client_phone, appt_type)

            print(f'\nAppointment for {client_name} has been scheduled for {day} at {start_hour:02d}:00')
            return new_apt
        else:
            print('\nSorry that time slot is booked already!')

def input_start_hour(promt):
    """
    Prompts the user to input a start hour for an appointment and validates it.

    The function checks if the entered hour is within the available hours (9:00 to 16:00). If valid, it returns the 
    formatted hour as a string. If invalid, it prints an error message and 
    returns `None`.

    Parameters:
        prompt (str): The message displayed to prompt the user for input.

    Returns:
        str: The valid start hour formatted as a two-digit string (e.g., "09", "10").
        None: If the entered hour is outside the valid range.
    """
    start_hour = input(promt)
    if int(start_hour) not in AVAIL_HOURS:     
        print('\nSorry that time slot is not in the weekly calendar!')
        return None
    else:
        return int(start_hour)
    
def create_weekly_calendar(appt_list=[]):
    """
    This function creates a weekly calendar, where each day is associated with 
    available hours (9AM to 3PM) and each hour is represented by an Appointment object.
    
    The appointments are stored in the provided appt_list.
    
    parameters: appt_list: List where created appointments will be stored (default: empty list)
    :return: The populated list of appointments
    """    
    appt_list.clear() #1                                     #1 --> clears list to [] to safeguard
    for day in DAY_OF_WEEK: #2                                  #2 --> iterates through WEEKDAY so hours objects for each weekday can be set
        for time_hour in AVAIL_HOURS: #3                    #3 --> sets range for available hours
            appt = ap.Appointment(day, time_hour) #5    #5 --> creates an instance of Appointment and assigns it to appt 
            appt_list.append(appt) #6                        #6 --> appends the appt vaiable to appt list which contains the day of week and hour
    return appt_list #7                        f              #7 --> returns appt_list

def find_appointment_by_time(appt_list, day, start_hour):
    """
    finds the appointment object based on the time and returns the object if the appointment exists

    Parameters:
        appointment list: appointment lis that contains the appointment objects
        day: day of the week 
        start hour: start hour of the appointment 

    Returns:
        appointment object  

    Notes:
        - both day and start hour should exist for the object to be returned
    """
    for appt in appt_list: 
        if appt.get_day_of_week() == day and appt.get_start_time_hour() == start_hour: 
            return appt
    return None

def print_menu():
    """
    This function prints the main menu of the system and prompts the user for a valid input.
    It keeps asking the user until they enter a valid menu selection.
    """

    print(f'\n{DOUBLE_DASH}' #(\n) --> to seperate for formating 
          )
    print(f'{'Hair So Long Appointment Manager':^38}') #(:^38) -->  centers in width of 38 charactors long
    print(DOUBLE_DASH)

    #iterating through the MENU_SELECTION dict:

    for key, value in OPTION.items(): #1              #1 --> iterates through each key and value 
        print(f' {key} {value}') #2                           #2 --> prints the following key and value in correct format
    selected_option = input('Enter your selection: ') #3      #3 --> user input to select an option 
    while selected_option not in OPTION: #4           #4 --> keeps user here until input is valid
        selected_option = input('\n' #5                       #5 --> print statment for invalid input
                                'Invalid option''\n' 
                                'Enter your selection: ')
        
    return selected_option # --> returns valid user selection

def input_day_of_week(prompt):
    """
    parameters:
    receives prompt string
    arguments:
    asks for day input as a string
    converts input to start with capital

    checks to see if input day is in the list of DAY_OF_WEEK
    if not valid/not in list 
    asks user to input again
    returns:
    day input 
    """
    day = str(input(prompt).title())
    while day not in DAY_OF_WEEK:
        day = str(input(f'Day must be one of: {', '.join(DAY_OF_WEEK)}\nEnter day of week: ').title())
    return day

def find_appointments_by_name():
    """
    Prompts the user to input a client's name and displays their appointments.

    Returns:
        str: The name of the client entered by the user.
    
    """
    client_name = input('\n** Find appointment by name **\nEnter Client Name: ')
    formated_display(client_name) 
    return client_name

def show_appointments_by_name(appt_list, client_name):
    """
    Displays the client names and the corresponding appointments for each client name 

    Parameters:
        appointment list: appointment list that contains the appointment objects
        client name: client name of the appointment object

    Returns:
        appointments for the name
        no appointments found when nothing is available

    Notes:
        - makes use of the __str__ method of the class to display the output
    """
    client_found = False 

    for appt in appt_list: 
        if client_name.lower() in appt.get_client_name().lower():
            client_found = True
            print(appt.__str__())
            
    if client_found == False:
        print('No appointments found.')

def change_appointment_by_day_time(appt_list):
    """
    Displays the client names and the corresponding appointments for each client name 

    Parameters:
        appointment list: appointment lis that contains the appointment objects

    Returns:
        appointments for the name
        no appointments found when nothing is available

    Notes:
        - needs the input_day_of_week() method to acquire original day
        - needs the (additional) input_start_hour() method to acquire original hours
    """
    original_day = input_day_of_week("\n** Change an appointment **\nEnter original day of week: ")
    original_start_hour = input_start_hour('Enter original start hour (24 hour clock): ')

    if original_start_hour != None:
        appt = find_appointment_by_time(appt_list, original_day, original_start_hour)
        if appt == None or appt.get_client_name() == '':
            print("\nThat time slot isn't booked and doesn't need to be changed")
        else:
            new_day = input_day_of_week('Enter new day of week: ')
            new_start_hour = input_start_hour('Enter new start hour (24 hour clock): ')
            if new_start_hour != None:
                new_appt = find_appointment_by_time(appt_list, new_day, new_start_hour)
                if new_appt.get_client_name() == '':
                    new_appt.schedule(appt.get_client_name(), appt.get_client_phone(), appt.get_appt_type())
                    print(f'\nAppointment for {appt.get_client_name()} has been changed to {new_appt.get_day_of_week()} at {int(new_appt.get_start_time_hour()):02d}:00')
                    appt.cancel()
                else:
                    print('\nThe new time slot is already booked')

def formated_display(name):
    """
    Displays a formatted header
    """
    print(f'\nAppointments for {name}\n\n{'Client Name':20}{'Phone':15}{'Day':10}{'Start':10}{'End':10}{'Type':15}')
    print(SINGLE_DASH)

def show_appointments_by_day(appt_list,day):
    """
    parameters: receives appointment list and day
    checks for the day in the object list

    prints: out the appointments with that day
    """
    for appt in appt_list:
        if appt.get_day_of_week().title() == day.title():
            print(appt.__str__())

def cancel_an_appointment(appt_list):
    """
    Cancels a scheduled appointment based on the user's input.

    Prompts the user to enter the day of the week and the start hour of the appointment 
    they want to cancel. If the appointment exists and is scheduled, it is canceled, 
    and a confirmation message is displayed. If no appointment exists at the specified 
    time, a message is displayed indicating that cancellation is unnecessary.

    Parameters:
        appt_list (list): A list of appointment objects to search through.

    Note:
        - Uses the `input_day_of_week()` and `input_start_hour()` helper functions 
          to gather user input for the day and time.
    """
    day = input_day_of_week('\n** Cancel an appointment **\nEnter day of week: ')
    start_hour = input_start_hour('Enter start hour (24 hour clock): ')
    if start_hour != None:
        appt = find_appointment_by_time(appt_list, day, start_hour)
        if appt.get_client_name() != '':      
            print(f'\nAppointment: {day} {start_hour:02d}:00 - {appt.get_end_time_hour()}:00 for {appt.get_client_name()} has been cancelled!')
            appt.cancel()
        else:
            print("\nThat time slot isn't booked and doesn't need to be cancelled")

def calculate_fees_per_day(appt_list):
    """
    Calculates and displays the total fees for all scheduled appointments on a specific day.

    Prompts the user to input a day of the week and sums up the fees for all appointments 
    scheduled on that day. The fees are determined based on the appointment type, using 
    the `APPT_TYPE_PRICES` dictionary.

    Parameters:
        appt_list (list): A list of appointment objects to calculate fees from.
    """
    day = input_day_of_week("\n** Calculate total fees for a day **\nEnter day of week: ")
    total_fee = 0
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            total_fee += ap.Appointment.APPT_TYPE_PRICES[appt.get_appt_type()]
    print(f'\nTotal fees for {day}: ${total_fee:,.2f}')

def calculate_weekly_fees(appt_list):
    """
    parameters: receives appointment list 

    arguments:
    sets weekly fee to 0
    sends appointment list into a for loop and adds up the cost of each appoinment
    prints: weekly fee

    """
    weekly_fee = 0
    for appt in appt_list:
        weekly_fee += ap.Appointment.APPT_TYPE_PRICES[appt.get_appt_type()]
    print(f'\n** Calculate total weekly fees **\nTotal weekly fees:  ${weekly_fee:,.2f}') 

def save_scheduled_appointments(appt_list):
    """
    Saves scheduled appointments to a file upon user confirmation.
    Prompts the user to decide whether to save all scheduled appointments 
    to a file before exiting the system. If the user agrees, they can provide 
    a filename. If the file already exists, the user is prompted to overwrite 
    it or provide a new filename. Only scheduled appointments are saved.

    Parameters:
        appt_list (list): List of appointment objects to be saved to a file.

    Note:
        - Each saved record is formatted using the `format_record()` method 
          of the appointment object.
        - Displays the number of appointments successfully saved.
    """
    user_choice = input('\n** Exit the system **\nWould you like to save all scheduled appointments to a file (Y/N)? ').upper()
    if user_choice == 'Y':
        overwrite = False
        file_name = input('Enter appointment filename: ')
        while os.path.exists(file_name) and overwrite == False:
            user_choice = input('File already exists. Do you want to overwrite it (Y/N)? ').upper()   
            if user_choice == 'N':
                file_name = input('Enter appointment filename: ')
            elif user_choice == 'Y':
                overwrite = True
            else:
                print('Please enter Y or N')
        scheduled_appts = 0
        file = open(file_name,'w')
        for appt in appt_list:
            if appt.get_appt_type() != 0:
                file.write(appt.format_record() + '\n')
                scheduled_appts += 1
        print(f'\n{scheduled_appts} scheduled appointments have been successfully saved')
    print('Good Bye!')

def main():
    appt_list = []
    create_weekly_calendar(appt_list)
    user_choice = input('Starting the Appointment Manager System\nWeekly calendar created\nWould you like to load previously scheduled appointments from a file (Y/N)? ').upper()
    if user_choice == 'Y':
        scheduled_appts = load_scheduled_appointments(appt_list)
        print(f'{scheduled_appts} previously scheduled appointments have been loaded')
    user_choice = print_menu()
    while user_choice != '0':
        match user_choice:
            case '1':
                schedule_an_appointment(appt_list)
            case '2':
                client_name = find_appointments_by_name()
                show_appointments_by_name(appt_list, client_name)
            case '3':
                day = input_day_of_week('\n** Print calendar for a specific day **\nEnter day of week: ')
                formated_display(day.title())
                show_appointments_by_day(appt_list,day)
            case '4':
                cancel_an_appointment(appt_list)
            case '5':
                change_appointment_by_day_time(appt_list)
            case '6':
                calculate_fees_per_day(appt_list)
            case '7':
                calculate_weekly_fees(appt_list)
        user_choice = print_menu()
    if user_choice == '0':
        save_scheduled_appointments(appt_list)

if __name__ == '__main__':
    main()
