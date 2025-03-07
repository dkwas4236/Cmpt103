# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  finalproject2_updated.py
# -------------------------------------------
# Purpose:  This program will create the pieces
#           on the board

from graphics import *
from finalproject import *

# purpose: calls other functions
# parameters: none
# return: none
def mainGameM2():
    infoB = {
        "full"   : 700,
        "board"  : 600,
        "edge"   : 50 }
    colors = "kw"
    board, boardDict, infoBtn, imgTurn = setupBoard(infoB, colors)
    pieces = SetupPieceInfo()
    cp = board.getMouse()
    (r, c) = getCell(cp, infoB, infoBtn)
    coord = r, c
    cell = cell2Name(coord)
    if coord != (702, 702):
        board.close() 
    else:    
        initializeBoardM2(board, infoB, boardDict, pieces, imgTurn)
        board.getMouse()
    
    board.close() 

# purpose: changed what cell was clicked to its square name
# parameters: coord
# return: string representation of the cell

def cell2Name(coord):
    # hard coding allowed here
    if coord == (701, 701):
        print("No Cell Selected")
        return 0
    if coord == (702, 702):
        print("Restart Game Selected")
        return 0
    if coord[0] == 1.0:
        cell = "A" + str(int(coord[1]))
        return cell
    elif coord[0] == 2.0:
        cell = "B" + str(int(coord[1]))
        return cell
    elif coord[0] == 3.0:
        cell = "C" + str(int(coord[1]))
        return cell
    elif coord[0] == 4.0:
        cell = "D" + str(int(coord[1]))
        return cell
    elif coord[0] == 5.0:
        cell = "E" + str(int(coord[1]))
        return cell
    elif coord[0] == 6.0:
        cell = "F" + str(int(coord[1]))
        return cell
    elif coord[0] == 7.0:
        cell = "G" + str(int(coord[1]))
        return cell
    elif coord[0] == 8.0:
        cell = "H" + str(int(coord[1]))
        return cell
        
# purpose: find out what cell was clicked
# parameters: cp, infoB, infoBtn
# return: coordinates (r,c) of cell on window
#         or
#         coordinates (dummyr, dummyc) signifying click on button
#         or
#         something to signify click was outside board and button
def getCell(cp, infoB, infoBtn):
    #cp = pixel coordinate on screen
    x = cp.getX()
    y = cp.getY()
    x = x-50
    y = y-50
    inc = infoB['board'] // 8
    xcoord = x // inc
    ycoord = y // inc
    button = 702
    nothing = 701
    if (x+50) >= 520 and (x+50) <= 680:
        if (y+50) >= 680 and (y+50) <= 720:
            return (button, button)
    if xcoord >= 0 and xcoord <= 7:
        if ycoord >= 0 and ycoord <= 7:
            return (xcoord+1, ycoord+1)
        else:
            return(nothing, nothing)
    else:
        return (nothing, nothing) # return twice for dummy coords
    

# purpose: draws the pieces on the board
# parameters: board, infoB, boardDict, pieces, imgTurn
# return: pieces (list), turn (int), imgTurn # won't be used
def initializeBoardM2(board, infoB, boardDict, pieces, imgTurn):
    player1, player2 = pieces
    turn = 0 
    for key in player1:
        pos = player1[key]["ipos"]
        name = player1[key]["imgName"]
        coord = boardDict[pos]['cp']
        piece = Image(coord,"img/"+name)
        piece.draw(board)
    for key in player2:
        pos = player2[key]["ipos"]
        name = player2[key]["imgName"]
        coord = boardDict[pos]['cp']
        piece = Image(coord,"img/"+name)
        piece.draw(board)

    return pieces, turn, imgTurn


if __name__ == "__main__":
    mainGameM2()