class Appointment:
    APPT_TYPE_DESC = {0:"Available",1:'Mens Cut', 2:'Ladies Cut', 3:'Mens Coluring', 4:'Ladies Colouring'}
    APPT_TYPE_PRICES = {0:0,1:40,2:60,3:40,4:80}
    def __init__(self,day_of_week, start_time_hour):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    # Client Name getter and setter
    def get_client_name(self):
        return self.__client_name
    
    def set_client_name(self, client_name):
        self.__client_name = client_name
    
    # Client Phone getter and setter
    def get_client_phone(self):
        return self.__client_phone
    
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone
    
    # Appointment Type getter and setter
    def get_appt_type(self):
        return self.__appt_type
    
    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type
    
    # Day of week getter
    def get_day_of_week(self):
        return self.__day_of_week
    
    # start time hour getter
    def get_start_time_hour(self):
        return self.__start_time_hour
    
    # end time hour getter
    def get_end_time_hour(self):
        end_time_hour = self.get_start_time_hour() + 1
        return end_time_hour
    
    # appointment type description getter
    def get_appt_type_desc(self):
        appt_type = self.get_appt_type()
        return self.APPT_TYPE_DESC[appt_type]  
    
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone) 
        self.set_appt_type(appt_type)

    def cancel(self):
        self.set_client_name('')
        self.set_client_phone('')
        self.set_appt_type(0)

    def format_record(self):
        format_str_rep = f"{self.get_client_name()},{self.get_client_phone()},{self.get_appt_type()},{self.get_day_of_week()},{self.get_start_time_hour()}"
        return format_str_rep
    
    def __str__(self):
        str_rep = f"{self.get_client_name():20}{self.get_client_phone():15}{self.get_day_of_week():10}{self.get_start_time_hour():02d}:00{'-':^5}{self.get_end_time_hour():02d}{':00':8}{self.get_appt_type_desc()}"
        return str_rep
    
    def get_appt_type_desc_and_price(appt_type):
        desc = Appointment.get_appt_type_desc(appt_type)
        price = Appointment.get_appt_type_price(appt_type)
        return f"{appt_type}: {desc} ${price}"
