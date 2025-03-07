# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  Lab4colourbands.py
# -------------------------------------------
# Purpose:  This program will give the resistance
#           of a band based upon 4 colours of the band



# dictionary of colours and information:

colourinfo = {
    "K" : [0, 0, 1E0, 0],
    "Br" :[1, 1, 1E1, 1],
    "R" : [2, 2, 1E2, 2],
    "O" : [3, 3, 1E3, 0],
    "Y" : [4, 4, 1E4, 0],
    "G" : [5, 5, 1E5, 0.5],
    "B" : [6, 6, 1E6, 0.25],
    "V" : [7, 7, 1E7, 0.10],
    "Gr" : [8, 8, 1E8, 0.05],
    "W" : [9, 9, 1E9, 0],
    "Au" : [0, 0, 1E-1, 5],
    "Ag" : [0, 0, 1E-2, 10],
}

# purpose: def main() will ask the user for input and call supporting functions
# parameter: none
# return: none

def main():
    colourBands = input("Please enter a string: ")
    (value, tolerance) = colour2Value(colourBands)
    dataString = formatString(value, tolerance)
    print(dataString)
 
# purpose: def colour2Value() will call functions in order to get value and tolerance out of colourBands
# parameter: colourBands
# return: value, tolerance

def colour2Value(colourBands): #4
    colourList = splitColourString(colourBands)
    valueList = determineValues(colourList)
    (value, tolerance) = value2Float(valueList)
    return (value, tolerance)

# purpose: def splitColourString() will break colourBands into 4 different colours and put them in a list
# parameter: colourBands
# return: colourList

def splitColourString(colourBands): #1
    colourList = []
    pos = 0
    while pos < (len(colourBands)):
        if colourBands[pos] == "B":
            colourList.append(colourBands[pos] + "r")
            pos += 1
        elif colourBands[pos] == "G":
            if pos < (len(colourBands) - 1) and colourBands[pos + 1] == "r":
                colourList.append("Gr")
                pos += 2
            else:
                colourList.append("G")
                pos += 1
        elif colourBands[pos] == "A":
            if pos < (len(colourBands) - 1) and colourBands[pos + 1] == "u":
                colourList.append("Au")
                pos += 2
            else:
                colourList.append("Ag")
                pos += 2
        else:
            colourList.append(colourBands[pos])
            pos += 1

    return colourList

# purpose: def determineValues() will convert the colours from colourList into values in a new list
# parameter: colourList
# return: valueList

def determineValues(colourList): #2
    valueList = []
    pos = 0
    while pos < len(colourList):
        if colourList[pos] in colourinfo:
            valueList.append(colourinfo[colourList[pos]])
        pos += 1
    return valueList

# purpose: def main() will ask the user for input and call supporting functions
# parameter: none
# return: none

def value2Float(valueList): #3
    ogvalue = (str(valueList[0][0])) + (str(valueList[1][1]))
    multi = (valueList[2][2])
    value = int(ogvalue) * float(multi)
    tolerance = str(valueList[3][3])
    value = float(value)
    tolerance = float(tolerance)

    return (value, tolerance)

# purpose: def formatString() convert the value and tolerance into a formatted string
# parameter: value, tolerance
# return: dataString

def formatString(value, tolerance): #5
    if tolerance < 1:
        if value >= 1000000:
            value = (value / 1000000)
            dataString = f"The resistor has a value of: {value}0 MΩ ± {tolerance}%"
        elif value >= 1000:
            value = (value/1000)
            dataString = f"The resistor has a value of: {value}0 kΩ ± {tolerance}%"
        elif value < 1:
            dataString = f"The resistor has a value of: {value} Ω ± {tolerance}%"
        else:
            dataString = f"The resistor has a value of: {value}0 Ω ± {tolerance}%"
    elif tolerance >= 1:
        if value >= 1000000:
            value = (value/1000000)
            dataString = f"The resistor has a value of: {value}0 MΩ ± {int(tolerance)}%"
        elif value >= 1000:
            value = (value/1000)
            dataString = f"The resistor has a value of: {value}0 kΩ ± {int(tolerance)}%"
        elif value < 1:
            dataString = f"The resistor has a value of: {value} Ω ± {int(tolerance)}%"
        else:
            dataString = f"The resistor has a value of: {value}0 Ω ± {int(tolerance)}%"
    return dataString


