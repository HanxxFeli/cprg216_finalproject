import appointment as ap

DAY_OF_WEEK = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def input_day_of_week():
    day = str(input('Enter day of week: ').title())
    while day not in DAY_OF_WEEK:
        day = str(input(f'Day must be one of: {', '.join(DAY_OF_WEEK)}\nEnter day of week: ').title())
    return day

def show_appointments_by_name(appt_list,client_name):
    search_client_name = client_name.lower()
    listed = False
    for appointment in appt_list:
        if search_client_name in appt.get_client_name().lower():
            listed = True
            print(appt)
    if not listed:
        print('No appointments found')

def calculate_weekly_fees(appt_list):
    weekly_fee = 0
    for appointment in appt_list:
        weekly_cost += ap.Appointment.__APPT_TYPE_PRICES[appt.get_appt_type()]
    print(f'\n** Calculate total weekly fees **\nTotal weekly fees:  ${weekly_fee:.2d}\n')

