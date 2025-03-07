# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  finalproject.py
# -------------------------------------------
# Purpose:  This program will create the chess
#           board on a canvas.

from graphics import *

# purpose: to call all functions and closes window
# parameters: none
# return: none
def mainGame():
    infoB = {
        "full"   : 700,
        "board"  : 600,
        "edge"   : 125 }
    colors = "kw"
    board, boardDict, infoBtn, imgTurn = setupBoard(infoB, colors)
    board.getMouse()
    board.close() 
   
# purpose: to set up the full chess board
# parameters: infoB, colors
# return: board, boardDict, infoBtn, imgTurn
def setupBoard(infoB, colors):
# define board size   
    width = infoB["full"]
    height = infoB["full"]
    edge = infoB["edge"]
# create the window 
    board = GraphWin("", width, height)
# define the starting point
    sp = (50,50)
# call SetupBoardInfo to get boardDict
    boardDict = SetupBoardInfo(sp, width, height)
# draw the letters and numbers    
    board, boardDict = drawLetNum(board, boardDict)
# draw the text on board
    board = drawText(board)
# draw squares on the board
    board, boardDict = drawSquares(boardDict, board)
# draw image of whos turn it is
    imgTurn = drawImgTurn(board)
# draw the info button
    infoBtn = drawInfoButton(board)

    return board, boardDict, infoBtn, imgTurn

# purpose: draw the information button
# parameters: board
# return: infoBtn
def drawInfoButton(board):
# define points of the rectangle
    firstPoint = Point(510, 630)
    secondPoint = Point(640, 670)
# print the text inside the rectangle
    text = Text(Point(575,650), "Restart")
    text.setSize(22)
    text.draw(board)
# draw the rectangle border around text
    infoBtn = Rectangle(firstPoint, secondPoint)
    infoBtn.draw(board)

    return infoBtn

# purpose: draw the image of player's turn it is 
# parameters: board
# return: imgTurn
def drawImgTurn(board):
    x = 85
    y = 650
    imgTurn = Image((Point(x,y)), "img/queen2.gif")
    imgTurn.draw(board)
    
    return imgTurn

# purpose: draw the text on the board
# parameters: board, boardDict
# return: board, boardDict
def drawLetNum(board, boardDict):
    
    for key in boardDict:
        if (key == "A1" or key == "B2" or key == "C3"or key == "D4"
        or key == "E5"or key == "F6" or key == "G7" or key == "H8"):
            
            letnum = boardDict[key]["cp"] 
            x = letnum.getX()
            y = letnum.getY()
            key.split()
            let = Text(Point(x, 25),key[0])
            num = Text(Point(25, y),key[1])
            let.draw(board)
            num.draw(board)

    return board, boardDict

# purpose: draw the text on the board
# parameters: board
# return: board
def drawText(board):
    text = Text(Point(215, 650), "Player's Turn")
    text.setSize(22)
    text.draw(board)
    
    return board

# purpose: draw the squares on the board
# parameters: boardDict, board
# return: board, boardDict
def drawSquares(boardDict, board):
    
    for i in boardDict:
        squareDict = boardDict[i]
        for j in squareDict:
            squareup = squareDict["up"]
        for l in squareDict:
            squarelp = squareDict["lp"]
        
        rec = Rectangle(squareup, squarelp).draw(board)
        if squareDict["color"] == "k":
            rec.setFill("black")
    
    return board, boardDict

# purpose: setup the board dictionary
# parameters: sp, width, height
# return: boardDict
def SetupBoardInfo(sp,width,height):
    boardDict = {}
    x = sp[0]
    y = sp[1]
    changeinx = (width/9.5)
    changeiny = (height/10)
    for i in "12345678":
        for j in "ABCDEFGH":
            boardDict[j+i] = {"lp"    : Point(x+changeinx,y+changeiny),
                              "cp"    : Point(x+35,y+35),
                              "up"    : Point(x,y),
                              "color" : "w" if (ord(j) + int(i)) % 2 == 0 else "k"
                              }
            x += changeinx
        
        x = sp[0]
        y += changeiny
    return boardDict

# purpose: setup the pieces information
# parameters: none
# return: pieces
def SetupPieceInfo():
    
    # white player
    player1 = {
        "King"     : {"ipos" : "E8", "cpos" : "E8", "imgName": "king1.gif" , "gObj" : None},
        "Queen"    : {"ipos" : "D8", "cpos" : "D8", "imgName": "queen1.gif" , "gObj" : None},
        "BishopL"  : {"ipos" : "C8", "cpos" : "C8", "imgName": "bishop1.gif" , "gObj" : None},
        "BishopR"  : {"ipos" : "F8", "cpos" : "F8", "imgName": "bishop1.gif", "gObj" : None},
        "KnightL"  : {"ipos" : "B8", "cpos" : "B8", "imgName": "knight1.gif", "gObj" : None},
        "KnightR"  : {"ipos" : "G8", "cpos" : "G8", "imgName": "knight1.gif", "gObj" : None},
        "RookL"    : {"ipos" : "A8", "cpos" : "A8", "imgName": "rook1.gif", "gObj" : None},
        "RookR"    : {"ipos" : "H8", "cpos" : "H8", "imgName": "rook1.gif", "gObj" : None},
        "Pawn1"    : {"ipos" : "A7", "cpos" : "A7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn2"    : {"ipos" : "B7", "cpos" : "B7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn3"    : {"ipos" : "C7", "cpos" : "C7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn4"    : {"ipos" : "D7", "cpos" : "D7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn5"    : {"ipos" : "E7", "cpos" : "E7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn6"    : {"ipos" : "F7", "cpos" : "F7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn7"    : {"ipos" : "G7", "cpos" : "G7", "imgName": "pawn1.gif", "gObj" : None},
        "Pawn8"    : {"ipos" : "H7", "cpos" : "H7", "imgName": "pawn1.gif", "gObj" : None}}
    # black player
    player2 = {
        "King"     : {"ipos" : "E1", "cpos" : "E1", "imgName": "king2.gif", "gObj" : None},
        "Queen"    : {"ipos" : "D1", "cpos" : "D1", "imgName": "queen2.gif", "gObj" : None},
        "BishopL"  : {"ipos" : "C1", "cpos" : "C1", "imgName": "bishop2.gif", "gObj" : None},
        "BishopR"  : {"ipos" : "F1", "cpos" : "F1", "imgName": "bishop2.gif", "gObj" : None},
        "KnightL"  : {"ipos" : "B1", "cpos" : "B1", "imgName": "knight2.gif", "gObj" : None},
        "KnightR"  : {"ipos" : "G8", "cpos" : "G8", "imgName": "knight2.gif", "gObj" : None},
        "RookL"    : {"ipos" : "A1", "cpos" : "A1", "imgName": "rook2.gif", "gObj" : None},
        "RookR"    : {"ipos" : "H1", "cpos" : "H1", "imgName": "rook2.gif", "gObj" : None},
        "Pawn1"    : {"ipos" : "A2", "cpos" : "A2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn2"    : {"ipos" : "B2", "cpos" : "B2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn3"    : {"ipos" : "C2", "cpos" : "C2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn4"    : {"ipos" : "D2", "cpos" : "D2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn5"    : {"ipos" : "E2", "cpos" : "E2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn6"    : {"ipos" : "F2", "cpos" : "F2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn7"    : {"ipos" : "G2", "cpos" : "G2", "imgName": "pawn2.gif", "gObj" : None},
        "Pawn8"    : {"ipos" : "H2", "cpos" : "H2", "imgName": "pawn2.gif", "gObj" : None}}
    pieces = [player1, player2]
    return pieces

if __name__ == "__main__":
    mainGame()
    



