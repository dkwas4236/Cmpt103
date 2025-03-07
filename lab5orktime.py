# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  lab5orktime.py
# -------------------------------------------
# Purpose:  This program will determine time
#           and related info on planet Ork


# day is 72 h, h is 186 mins, min is 186 sec

# purpose: def orkTime() will convert total seconds into Ork time format
# parameter: totSeconds, fmt
# return: time

def orkTime (totSeconds, fmt = 36):
    h_count = 0
    m_count = 0
    sec_count = 0
# find max hours
    while totSeconds >= 34596:
        totSeconds = (totSeconds - 34596)
        h_count += 1
# find max mins
    while totSeconds >= 186:
        totSeconds = (totSeconds - 186)
        m_count += 1
# the remaining will be seconds
    sec_count = totSeconds
    
    hours = (str(h_count).zfill(2))
    minutes = (str(m_count).zfill(3))
    seconds = (str(sec_count).zfill(3))

    if fmt == 72:
        time = time = str(hours + ":" + minutes + ":" + seconds)
    else:
        if h_count <= 36:
            time = str(hours + ":" + minutes + ":" + seconds + " AM")
        else:
            time = str(hours + ":" + minutes + ":" + seconds + " PM")
    return time

# purpose: def getData72HrFormat() will convert time to 72h format
# parameter: time
# return: time72

def getData72HrFormat(time):
    time72 = ""
    if time[-2] == "P":
        time = time.split(":")
        time[0] = int(time[0]) + 36
        time[0] = str(time[0])
        time72 = ":".join(time[0:3])
        time72 = time72[0:-3]
    elif time [-2] == "A":
        time72 = time[0:-3]
    else:
        time72 = time
    
    return time72

# purpose: def convert2Seconds() will convert hr:mn:sec to seconds
# parameter: hour, minute, second
# return: totalSec

def convert2Seconds(hour, minute, second):
    
    secondsfromh = abs(int(hour) * 186 * 186)
    secondsfromm = abs(int(minute) * 186)
    totalSec = secondsfromh + secondsfromm + second
    return totalSec
    

# purpose: def timeElapsed will determine seconds elapsed between 2 times
# parameter: time1, time2
# return: secElapsed

def timeElapsed(time1, time2):
    time = ""
# convert to 72h
    if time1[-1] == "M":
        time = time1
        time1 = getData72HrFormat(time)
    if time2[-1] == "M":
        time = time2
        time2 = getData72HrFormat(time)

    time1 = time1.split(":")
    time2 = time2.split(":")
    hour1, minute1, second1 = (int(time1[0])), (int(time1[1])), (int(time1[2]))
    hour2, minute2, second2 = (int(time2[0])), (int(time2[1])), (int(time2[2]))
    
    sec1 = convert2Seconds(hour1, minute1, second1)
    sec2 = convert2Seconds(hour2, minute2, second2)
    secElapsed = abs(int(sec1- sec2))

    return secElapsed
    


# purpose: def durations() will determine the time between every 2 consequtive times
# parameter: time* (tuples)
# return: secElapsed

def durations(*time):
    secElapsed = []
    for pos in range(len(time) -1):
        time1 = time[pos]
        time2 = time[pos+1]
        timedif = timeElapsed(time1, time2)
        secElapsed.append(int(timedif))
    return secElapsed

