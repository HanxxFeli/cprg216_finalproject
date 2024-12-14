
import appointment as ap

#list needed for weekly fees
appt_list = []

#dict to slim down on code size in print menu funtion:
MENU_SELECTION = {'1' : 'Schedule an appointment',
                  '2' : 'Find appointment by name',
                  '3' : 'Print calendar for a specific day',
                  '4' : 'Cancel an appointment',
                  '5' : 'Change an appointment',
                  '6' : 'Calculate total fees for a day',
                  '7' : 'Calculate total weekly fees',
                  '0' : 'Exit the system'}

#list for weekdays for stuff
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#print menu function:
def print_menu():

#top of menu:

    print('\n' #(\n) --> to seperate for formating 
          '=======================================')
    print(f'{'Hair So Long Appointment Manager':^38}') #(:^38) -->  centers in width of 38 charactors long
    print('=======================================')

#iterating through the MENU_SELECTION dict:

    for key, value in MENU_SELECTION.items(): #1              #1 --> iterates through each key and value 
        print(f'{key}) {value}') #2                           #2 --> prints the following key and value in correct format
    selected_option = input('Enter your selection: ') #3      #3 --> user input to select an option 
    while selected_option not in MENU_SELECTION: #4           #4 --> keeps user here until input is valid
        selected_option = input('\n' #5                       #5 --> print statment for invalid input
                                'Invalid option''\n' 
                                'Enter your selection: ')
        
    return selected_option # --> returns valid user selection 

#weekly fee calculator:
def calculate_weekly_fees(appt_list):
    total_fee = 0 #1                                                          #1 --> sets the fee count to 0 to safeguard 
    for i in appt_list: #2                                                    #2 --> iterates through appt list to add all fees to total
        total_fee += ap.Appointment.APPT_TYPE_PRICES[i.get_appt_type()] #3    #3 --> calls Appointment class to get dict of prices  
    print(f'\n'                                                               #     -and matches selection to the correct price  
          'Total weekly fees: ${total_fee:,.2f}') #4                          #4 --> prints the weekly fees 
    
#creating weekly calender
def create_weekly_calendar(appt_list = []):            
    appt_list = []                                     
    appt_list.clear() #1                                     #1 --> clears list to [] to safeguard
    for day in WEEKDAYS: #2                                  #2 --> iterates through WEEKDAY so hours objects for each weekday can be set
        for time_hour in range(9, 16): #3                    #3 --> sets range for available hours
            if time_hour == 9: #4                            #4 --> turns 9 into 09 to safegaurd so all hour strings can be 2 figures
                time_hour = '09' #4
            appt = ap.Appointment(day, str(time_hour)) #5    #5 --> creates an instance of Appointment and assigns it to appt 
            appt_list.append(appt) #6                        #6 --> appends the appt vaiable to appt list which contains the day of week and hour
    return appt_list #7                                      #7 --> returns appt_list
