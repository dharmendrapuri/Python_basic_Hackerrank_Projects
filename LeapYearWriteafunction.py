"""
Write a Function
-----------------

We add a Leap Day on February 29, almost every four years. The leap day is an extra or
intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar, three criteria must be taken into account to identify
leap years
    -The year can be evenly divided by 4, is a leap year, unless;
        The year can be evenly divided by 100, it is NOT  a leap year, unless
            The year is also evenly divisible by 400, then it is a leap year.
This means that in the Gregorian calendar, the year 2000, and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years

Task
------
You are given the year, and you have to write a function to check if the year
is leap or not
Note that you have to complete the function and remaining code is given as template

Input Format
---------
Read y, the year that needs to be checked.

Constraitns
1900<=y<=10to the power of five

Output format
Output is taken care of by the template, Your function must return a boolean value

"""

def is_leapYear(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

is_leapYear(1900)

