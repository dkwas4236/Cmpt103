#-------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own. 
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
#-------------------------------------------
# Name:     Darion Kwasnitza
# Program:  X05Ldk.py
#-------------------------------------------
# Purpose:  This program will determine info
# based on a given date
    
# purpose: def calcCentury will calculate the century and return it
# parameter: year (int)
# return: c (int) (the century of the year)
def calcCentury(year):
    year = str(year)
    c = year[0:2] 
    c = int(c) + 1
    return c

# purpose: def calcMonth will calculate the month and return it, 
#          (1 = march ... 12 = february)
# parameter: month (str)
# return: m (int) (month in numeric form)
def calcMonth(month):
    month = month.lower()
    
    months = ["march","april", "may", "june", "july", "august", "september", "october", "november", "december", "january", "february"]
    for i in range (len(months)):
        if months[i] == month:
            
            return i + 1
    
        
# purpose: def fixYear will return the last two digits of the year 
#          and fix it if it is january or february (set back to previous year)
# parameter: year (int), m (int)
# return: y (int) (last two digits of the year, fixed if Jan or Feb)

def fixYear(year, m):
    if m == 11 or m == 12:
        year = str(year)
        y = year[2:4]
        y = int(y) -1
        
    else:
        year = str(year)
        y = year[2:4]
        
    return int(y)

# purpose: def calcWeekday will return the weekday of the date
# parameter: day (int), month (str), year (int)
# return: weekday (str) (the weekday)

def calcWeekday(day, month, year):
    import math
    c = calcCentury(year)
    m = calcMonth(month)
    y = fixYear(year, m)
    
    w = (day + math.floor(2.6*m - 0.2) - 2*(c-1) + (y) + math.floor(y/4) + math.floor((c-1)/4))%7
    
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday"]
    
    weekday = weekdays[w]
    
    return weekday

# purpose: def isLeapYear will return true if it is a leap year 
#          and false if it is not a leap year
# parameter: year (int)
# return: isLeap (bool)

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
        else:
            isLeap = True
    else:
        isLeap = False
    
    return isLeap

# purpose: def calcDaysInMonth will determine the number of days in a month 
# parameter: month (str), year (int)
# return: days (int) (the number of given days in a month

def calcDaysInMonth(month, year):
    m = calcMonth(month)
    isLeap = isLeapYear(year)
    
    if month.lower() in ("september", "april", "june", "november"):
        days = 30
    elif month.lower() in ("january", "march", "may", "july", "august", "october", "december"):
        days = 31
    else:
        if isLeap == True:
            days = 29
        else:
            days = 28
    return days
 
# purpose: def printInformation will print the date information 
# parameter: day (int), month (str), year(int)
# return: (prints the date information)

def printInformation(day, month, year):
    c = calcCentury(year)
    isLeap = isLeapYear(year)
    days = calcDaysInMonth(month, year)
    weekday = calcWeekday(day, month, year)
    
    print("Date           :",day, month, year)
    print("Century        :",c)
    print("Is a Leap Year :",isLeap)
    print("Days in Month  :",days)
    print("Weekday        :",weekday)
