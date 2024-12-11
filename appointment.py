

class Appointment:
    __APPT_TYPE_DESC = {0:'Available', 1:'Mens Cut', 2:'Ladies Cut', 3:'Mens Colouring', 4:'Ladies Colouring'} 
    __APPT_TYPE_PRICES = {0:0, 1:40, 2:60, 3:40, 4:80}
    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

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
        return Appointment.__APPT_TYPE_DESC[self.__appt_type]
    
    def get_appt_type_price(self):
        return Appointment.__APPT_TYPE_PRICES[self.__appt_type]
    
    def get_end_time_hour(self):
        return self.__start_time_hour +1 
    
    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def cancel(self):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0

    def format_record(self):
        result = (f'{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour:02d}')
        return result
    
    def __str__(self):
        slot = {f'{self.__client_name:20}{self.__client_phone:15}{self.__day_of_week:10}{self.__start_time_hour:02d}:00{'-':^5}{self.get_end_time_hour():02d}{':00':8}{self.get_appt_type_desc()}'}
        return str(*slot)

    def get_appt_type_desc_and_price(appt_type):
        option = (f'{appt_type}: {Appointment.get_appt_type_desc(appt_type)} ${Appointment.get_appt_type_price(appt_type)}')
        return str(option)