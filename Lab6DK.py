# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  Lab6DK.py
# -------------------------------------------
# Purpose:  This program will draw and display
#           info about various functions used in
#           files/programs. 


from graphics import *


# purpose: def getFunctions() will get the function info, such as 
#          the name, parameters, and return value
# parameter: data (list, str)
# return: fName, fParam, ffReturn

def getFunctions(data):
    fName = []
    fParam = []
    ffReturn = []
    print (data)
    for item in data:
        if item[0:3] == "def":
            start, finish = item.index('('), item.index(')')
            fName.append(item[4:start])
            fParam.append(item[start:finish+1])
        elif "return" in item and item[0] != "#":
            item.strip()
            ffReturn.append(item[11:])
    return fName, fParam, ffReturn


# purpose: def loadData() will load the python file
# parameter: filename
# return: data (list, str)

def loadData(filename):
    file = open(filename, "r")
    data = []
    line = file.readline()

    while(line):
        data.append(line.rstrip())
        line = file.readline()
    
    file.close()
    return data


# purpose: def setupScreen() will draw the canvas
# parameter: title, width, height, lines
# return: win

def setupScreen(title = "", width = 650, height = 800, lines = False):
    win = GraphWin("", width, height)
    win = drawDraftLines(win, height, lines)
    return win
    

# purpose: def drawDraftLines() will draw draftlines on the canvas
# parameter: win, height, lines
# return: win

def drawDraftLines(win, height, lines):
    side_margin = height / 11
    vertical_margin = side_margin / 2
    width = win.getWidth()
    
    topline = Line(Point(side_margin, vertical_margin) , 
                Point(width - side_margin, vertical_margin))
    bottomline = Line(Point(side_margin, height - vertical_margin) , 
                Point(width - side_margin, height - vertical_margin))
    leftline = Line(Point(side_margin, vertical_margin) , 
                Point(side_margin, height - vertical_margin))
    rightline = Line(Point(width - side_margin, vertical_margin) , 
                Point(width - side_margin, height - vertical_margin))
    titleline = Line(Point(side_margin, (height / 11) *1.5) , 
                Point(width - side_margin, height / 11*1.5))
    titleline.draw(win)
    topline.draw(win)
    bottomline.draw(win)
    leftline.draw(win)
    rightline.draw(win)

    return win

# purpose: def drawTitle() will draw the title on the canvas
# parameter: win, height
# return: win

def drawTitle(win, height):
    width = win.getWidth()
    side_margin = height / 11

    title_text = "Cmpt 103 - Intro. to Computing II".ljust(int(36))
    title_text_2 = "\n Lab 06 - Graphics".ljust(int(39))
    title = Text(Point(width / 2, height / 11), title_text + title_text_2)
# change text size    
    title.setSize(18)
# make title bold
    title.setStyle("bold")
# change font
    title.setFace("courier")
# draw title
    title.draw(win)
    
    return win

# purpose: def drawFunctionInfo() will draw the function info
#          on the canvas
# parameter: fName, fParam, fReturn, win, height
# return: win

def drawFunctionInfo(fName, fParam, ffReturn, win, height):
    width = win.getWidth()
    initial_height = (height/11) * 1.75
    spacing = 80
    side_margin = height / 11

    for pos in range (len(fName)):
# left justify the strings        
        Name_str = str("Name  : " + fName[pos]).ljust(int(0.70 * side_margin))
        Param_str = str("Param : " + fParam[pos]).ljust(int(0.70 * side_margin))
        Retur_n_str = str("Return: " + ffReturn[pos]).ljust(int(0.70 * side_margin))
# create the function info        
        name = Text(Point(width/2, initial_height + (spacing * pos)), Name_str)
        param = Text(Point(width/2, initial_height + (spacing * pos) + 20), Param_str)
        retur_n = Text(Point(width/2, initial_height + (spacing * pos) + 40), Retur_n_str)
        pos += 1
# change the text size  (MUST CHANGE IF PARAMETERS are TOO LONG IN SOME CASES!)  
        name.setSize(12)
        param.setSize(12)
        retur_n.setSize(12)
# change the font
        name.setFace("courier")
        param.setFace("courier")
        retur_n.setFace("courier")
# draw the information
        name.draw(win)
        param.draw(win)
        retur_n.draw(win)
        
    return win

# purpose: def main() will call all other functions
# parameter: none
# return: none

def main():
    win = setupScreen()
    data = loadData("lab5orktime.py")
    fName, fParam, ffReturn = getFunctions(data)
    height = win.getHeight()
    drawTitle(win, height)
    win = drawFunctionInfo(fName, fParam, ffReturn, win, height)

    while win.getKey() != "q":
        pass
    win.close()


