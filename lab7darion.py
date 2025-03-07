# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  lab7darion.py
# -------------------------------------------
# Purpose:  This program will plot points of a map
from graphics import *

def loadData(filename):
    file = open(filename, "r", errors = "ignore")
    data = []
    line = file.readline()
    while line != '':
        data.append(line.rstrip)
        line = file.readline()

    file.close()
    return data

# purpose: def loadRawData() will load the data in a file
# parameter: filename
# return: header(str), rawData(str, list)

def loadRawData(filename):
    file = open(filename, "r", errors = "ignore")
    rawData = []
    line = file.readline()
    while line != '':
        rawData.append(line.rstrip())
        line = file.readline()
    
    header = rawData[0]
    del rawData[0]
    
    file.close()
    return header, rawData

# purpose: def formatRawData() will format data into dictionary
# parameter: header, rawData
# return: dData (dict)

def formatRawData(header, rawData):
    dData = {}
    header_list = header.split('","')
    header_list[0] = header_list[0].replace('"', '')
    header_list[-1] = header_list[-1].replace('"', '')
    
    for item in range(len(header_list)):
        dData[header_list[item]] = []
    
    for pos in range(len(rawData)):
        rawData_string = rawData[pos]
        rawData_string = rawData_string.split('","')
        
        for i in range(len(header_list)):
            rawData_string[i] = (rawData_string[i]).replace('"', "")
            dData[header_list[i]].append(rawData_string[i])

    return dData

# purpose: def visualizeData() will show points on map of AB
# parameter: dData
# return: none

def visualizeData(dData):
    win =  GraphWin("", 475, 850) 
    map_image = Image(Point(235,400), "alberta_openMap.gif")
    map_image.draw(win)
    longitude = dData['Longitude']
    latitude = dData['Latitude']
    
    xpoint, ypoint = coord2Pixel(longitude, latitude)
    pointlist = list(zip(xpoint, ypoint))
    
    
    for tupl in pointlist:
        x, y = tupl
        points2draw = (Point(x,y))
        cirpoint = Circle(points2draw, 2)
        cirpoint.draw(win)

    while True:
        win.getMouse()    
        win.close()

# purpose: def coord2Pixel() will convert long and lat to pixel x and y
# parameter: longitude, latitude
# return: xpoint, ypoint
def coord2Pixel(longitude, latitude):
    xpoint = [ ]
    ypoint = [ ]
    longlow, longhigh, xhigh, xlow = -120, -110, 475, 0
    longitude = str(longitude).replace("'", "")
    longitude = longitude.replace("[", "")
    longitude = longitude.replace("]", "")
    longitude = longitude.strip()
    longitude = longitude.split(",")
    pos = 0
    for item in longitude:
        x = (((int((float(longitude[0]) - longlow))/(longhigh - longlow)*(xhigh - xlow) + xlow)))
        xpoint.append(x)
        pos += 1
        longitude[0] = longitude[pos-1]
    latlow, lathigh, yhigh, ylow = 49, 60, 850, 0
    pos = 0
    for item in latitude:
        y = (((int((float(latitude[0]) - latlow))/(lathigh - latlow)*(yhigh - ylow) + ylow)))
        ypoint.append(y)
        pos +=1
        latitude[0] = latitude[pos-1]
    return xpoint, ypoint
    
def main():
    header, rawData = loadRawData("pipeline-incidents-comprehensive-data (1).csv")
    dData = formatRawData(header, rawData)
    visualizeData(dData)
    