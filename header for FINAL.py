"""
Hair So Long Appointment Manager
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

Author: [Your Name]
Date: [Insert Date]
"""
