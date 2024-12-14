
#Do not fear, for I am with you; Do not be afraid, for I am your God

class Appointment:
    def __init__(self, day_of_week, start_time_hour):

        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0

        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

# getters
    def get_client_name(self):
        return self.__client_name
    
    def get_client_phone(self):
        return self.__client_phone
    
    def get_appt_type(self):
        return self.__appt_type
    
    def get_day_of_week(self):
        return self.__day_of_week
    
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_appt_type_desc(self):
        match self.__appt_type:
            case 0:
                self.__appt_type = 'Available'
            case 1:
                self.__appt_type = 'Mens Cut'
            case 2:
                self.__appt_type = 'Ladies Cut'
            case 3:
                self.__appt_type = 'Mens Colouring'
            case 4:
                self.__appt_type = 'Ladies Colouring'
        return self.__appt_type

    def get_end_time_hour(self):
        return str(int(self.__start_time_hour) + 1)
# end of getters

# setters
    def set_client_name(self, client_name):
        self.__client_name = client_name 
    
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone
    
    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        client_name = self.__client_name
        client_phone = self.__client_phone
        appt_type = self.__appt_type
# end of setters

    def cancel(self):
        client_name = ''
        client_phone = ''
        appt_type = 0

    def format_record(self):
        return (f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}')
    
    def __str__(self):
        return f'{self.__client_name:<20}{self.__client_phone:<15}{self.get_day_of_week():<10s}{str(self.__start_time_hour)+':00':<7}{'-':3}{self.get_end_time_hour()+':00':<10}{Appointment.APPT_TYPE_DESCS[self.__appt_type]:15}'

#selection for description and price (str)
    APPT_TYPE_DESCS = {0:"Available",1:'Mens Cut', 2:'Ladies Cut', 3:'Mens Coluring', 4:'Ladies Colouring'}
    APPT_TYPE_PRICES = {0:0,1:40,2:60,3:40,4:80}
#end of selection

#this sucks
    def get_appt_type_desc_and_price(appt_type):
        description = Appointment.APPT_TYPE_DESCS[appt_type]
        price = Appointment.APPT_TYPE_PRICES[appt_type]
        return f"{appt_type}: {description} ${price}"
    
    
