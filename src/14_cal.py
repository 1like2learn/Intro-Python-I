"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

def calFunction():
  now = datetime.now()
  # print("\n now.month", now.month, type(now.month))
  # print("\n now.year", now.year, type(now.year))
  # print("\n length of system arguments", len(sys.argv))
  # print("\ntype of arguments", type( int(sys.argv[1])))
  if len(sys.argv) == 1:
    # print("\ncurrent month and year used")
    month = now.month
    year = now.year

  elif len(sys.argv) == 2:
    arg1 = sys.argv[1]
    # print("\ninput month and current year used")
    year = now.year
    if not arg1.isdigit() or 1 < int(arg1) or int(arg1) < 12:
      return "\nPlease input a number between 1 and 12.\n"
    else:
      # print("\ninput value set for month")
      month = int(arg1)

  elif len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # print("too low?", 1 > int(arg1), arg1)
    # print("too high?", int(arg1) > 12, arg1)
    # print("\ninput month and year used")
    if not arg1.isdigit() or 1 > int(arg1) or int(arg1) > 12:
      return "\nPlease input a number between 1 and 12 for your first argument.\n"
    else:
      # print("\ninput value set for month")
      month = int(arg1)

    if not arg2.isdigit():
      return "\nPlease input a number for year.\n"
    else:
      # print("\ninput value set for year")
      year = int(arg2)

  # print("\nmonth", month, type(month))
  # print("\nyear", year, type(year), "\n")
  return calendar.month(year, month)
  # return month

print(calFunction())

# initializing the yearn and month number
# year = 2000
# month = 1
# # getting the calendar of the month
# print(calendar.month(year, month))

# now = datetime.now()
# print(now.month)
# print(now.year)