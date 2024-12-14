import appointment as ap

DAY_OF_WEEK = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

#function for input of week asks to input a valid day of the week returns day if valid
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
    day = str(input('Enter day of week: ').title())
    while day not in DAY_OF_WEEK:
        day = str(input(f'Day must be one of: {', '.join(DAY_OF_WEEK)}\nEnter day of week: ').title())
    return day

#function to show what appoinment is listed according to input name returns to say if there is or isn't in the appoinment list
def show_appointments_by_name(appt_list,client_name):
    """
    parameters: receives appointment list and client 
    arguments:
    converts client name input to be all lower 
    set listed to False
    for loop to run over the appointment list to look for user
    if found sets listed to True

    if not in appointment list it print"No appointments found"
    """
    search_client_name = client_name.lower()
    listed = False
    for appointment in appt_list:
        if search_client_name in appt.get_client_name().lower():
            listed = True
            print(appt)
    if not listed:
        print('No appointments found')

#function to calculate weekly cost of appointments
def calculate_weekly_fees(appt_list):
    """
    parameters: receives appointment list 

    arguments:
    sets weekly fee to 0
    sends appointment list into a for loop and adds up the cost of each appoinment
    prints: weekly fee

    """
    weekly_fee = 0
    for appointment in appt_list:
        weekly_cost += ap.Appointment.APPT_TYPE_PRICES[appt.get_appt_type()]
    print(f'\n** Calculate total weekly fees **\nTotal weekly fees:  ${weekly_fee:.2d}\n')

#function to check if selected day is in the appt list
def show_appointments_by_day(appt_list,day):
    """
    parameters: receives appointment list and day
    checks for the day in the object list

    prints: out the appointments with that day
    """
    for appt in appt_list:
        if appt.get_day_of_week() == day:
            print(appt)