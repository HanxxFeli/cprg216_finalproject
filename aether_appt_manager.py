import appointment as ap
import os
OPTION = {'1':'Schedule an appointment',
          '2':'Find appointment by name', 
          '3':'Print calendar for a specific day',
          '4':'Cancel an appointment',
          '5':'Change an appointment',
          '6':'Calculate total fees for a day',
          '7':'Calculate total weekly fees',
          '0':' Exit the system'}
WEEKDAYS = ['Monday','Tuesday', "Wednesday", "Thursday", "Friday", "Saturday"]
AVAIL_HOURS = [9, 10, 11, 12, 13, 14, 15, 16]


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
        appt = find_appointment_by_time(appt_list, attributes[3], attributes[4])
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
                print(f'{index:>4d}: {ap.Appointment.APPT_TYPE_DESCS[index]} ${ap.Appointment.APPT_TYPE_PRICES[index]}')
            appt_type = int(input('Type of Appointment: '))
            new_apt = appt.schedule(client_name, client_phone, appt_type)

            print(f'\nAppointment for {client_name} has been scheduled for {day} at {start_hour}:00')
            return new_apt
        else:
            print('\nSorry that time slot is booked already!')

def input_start_hour(prompt):
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
    start_hour = input(prompt)
    if int(start_hour) not in AVAIL_HOURS:     
        print('\nSorry that time slot is not in the weekly calendar!')
        return None
    else:
        if start_hour == '9': start_hour = '09'
        return start_hour
    
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

def formated_display(name):
    """
    Displays a formatted header
    """
    print(f'\nAppointments for {name}\n\n{'Client Name':20}{'Phone':15}{'Day':10}{'Start':10}{'End':10}{'Type':15}')
    print(SINGLE_DASH)
          
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
            print(f'\nAppointment: {day} {start_hour}:00 - {appt.get_end_time_hour()}:00 for {appt.get_client_name()} has been cancelled!')
            appt.cancel()
        else:
            print("\nThat time slot isn't booked and doesn't need to be cancelled")
                  
def create_weekly_calendar(appt_list=[]):
    pass

def find_appointment_by_time(appt_list, day, start_hour):
    pass

def print_menu():
    pass

def input_day_of_week(promt):
    pass

def show_appointments_by_name(appt_list, client_name):
    pass

def show_appointments_by_day(appt_list, day):
    pass

def change_appointment_by_day_time(appt_list):
    pass

def calculate_fees_per_day(appt_list):
    pass

def calculate_weekly_fees(appt_list):
    pass

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
