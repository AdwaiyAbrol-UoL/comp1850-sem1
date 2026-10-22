# Week 4, Session 2: Task 1

import calendar

# calendar is a module in the Python standard library. To use this module,
# we need to import it using the import keyword as shown above. One of the
# functions in calendar is the month function. This function returns a
# month's calendar in a multi-line string.

# For example, the following code prints the calendar month for October 2025.
# Run the program and observe the output.

print(calendar.month(2025, 10))

# Your task is to go to https://docs.python.org/3/library/calendar.html,
# and have a look at other optional arguments for the month function,
# namely the w and l parameters. Write code to made two more function calls
# to the month function with different values of w and l and observe the
# output.
print(calendar.month(2025, 10, w=3, l=1))
print(calendar.month(2025, 10, w=5, l=2))


# While at https://docs.python.org/3/library/calendar.html, explore
# the calendar function(calendar.calendar, yes the function is called
# calendar). The calendar function returns a 3-column calendar for an entire
# year as a multi-line string. For example print(calendar.calendar(2025))
# will print the calendar for 2025.

# Your task is to write code to make 3 functions calls to the calendar
# function with different values to the optional arguments (w, l, c, and m).
# Display the output to observe the differences.
print(calendar.calendar(2025, w=7, l=1, c=3, m=5))
print(calendar.calendar(2025, w=1, l=2, c=8, m=4))
print(calendar.calendar(2025, w=6, l=1, c=10, m=7))
