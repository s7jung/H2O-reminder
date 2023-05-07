#Hydration Reminder Program

This is a python program that reminds you to drink water at regular intervals based on your personal hydration needs. The program calculates the recommended daily water intake based on your height, sex, age, and other factors, and sends a desktop notification to remind you to drink water.


####Requirements
To run this program, you'll need:

Python 3.6 or higher
The plyer package for sending desktop notifications (pip install plyer)


####Usage
Clone this repository or download the water.py and reminder.py files to your local machine.
Open the water.py file and input your personal information, such as your height, sex, age, etc., to calculate your recommended daily water intake. Save the changes.
Open the reminder.py file and run the script using python reminder.py. The program will start sending desktop notifications every hour to remind you to drink water.


####Customization
If you'd like to customize the program to your personal preferences, you can modify the following variables in the reminder.py file:

interval: The interval between reminders in seconds. By default, this is set to 3600 seconds (1 hour).
mL_a_day: The recommended daily water intake in milliliters. This value is calculated based on your personal information in the water.py file. If you'd like to manually set this value, you can modify it in the reminder.py file.
