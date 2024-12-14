import appointment as ap

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
        else: 
            return None

def show_appointments_by_name(appt_list, client_name) :
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
        if appt.get_client_name().lower() == client_name.lower():
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
                    new_appt.schedule(appt.set_client_name(appt.get_client_name()), appt.set_client_phone(appt.get_client_phone()), appt.set_appt_type(appt.get_appt_type()))
                    print(f'\nAppointment for {appt.get_client_name()} has been changed to {new_appt.get_day_of_week()} at {new_appt.get_start_time_hour():02d}')
                    appt.cancel()
                else:
                    print('\nThe new time slot is already booked')
        
# Additional function for getting the start hour. Functions similar to input_day_of_week()
def input_start_hour(promt):
    start_hour = input(promt)
    if int(start_hour) not in AVAIL_HOURS:            
        print('\nSorry that time slot is not in the weekly calendar!')
        return None
    else:
        if start_hour == '9': 
            start_hour = '09'
        return start_hour


