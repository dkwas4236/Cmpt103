# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  finalprojectpart3.py
# -------------------------------------------
# Purpose:  This program will move pieces on
#           the chess board.

from moves import *
from finalprojectpart2_updated import *

# purpose: calls other functions
# parameters: none
# return: none
def main():
    infoB = {
        "full"   : 700,
        "board"  : 600,
        "edge"   : 50 }
    colors = "kw"
    board, boardDict, infoBtn, imgTurn = setupBoard(infoB, colors)
    pieces = SetupPieceInfo()
    move = []
    while True:

        try:
            cp = board.getMouse()
        except:
            board.close()
            return
        (r, c) = getCell(cp, infoB, infoBtn)
        coord = r, c
        cell = cell2Name(coord)
        if coord == (701,701): # out of bounds
            continue
        else:
            if coord == (702,702): # restart button
                pieces = undrawPieces(pieces)
                print(pieces)
                pieces, player, imgTurn = initializeBoard(board, infoB, boardDict, pieces, imgTurn)
                print(pieces)
                move = []
            else:
                (r, c) = getCell(cp, infoB, infoBtn)
                coord = r, c
                cell = cell2Name(coord)
                move.append(cell)
                name = cell
                isOccupied = cellOccupied(name, pieces)
                
                (piece, iplayer) = getContents(move, pieces)
                if len(move) == 2:
                    if isOccupied == True:
                        if isValidMove(piece,move[0],move[1],iplayer):
                            (imgTurn, board) = updateTurnImage(imgTurn, board, iplayer)
                            updatePiece(board, iplayer, piece, move, pieces, boardDict)
                    if isOccupied == False:
                        continue
                elif len(move) > 2:
                    move = []
                    move.append(cell)

# purpose: undrawPieces() undraws the moved pieces on board
# parameters: pieces
# return: pieces
def undrawPieces(pieces):
    player1, player2 = pieces
    for key in player1:
        piece = player1[key]["gObj"]
        if player1[key]["gObj"] != (None):
            piece.undraw()
            player1[key]["gObj"] = (None)

    for key in player2:
        piece = player2[key]["gObj"]
        if player2[key]["gObj"] != (None):
            piece.undraw()
            player2[key]["gObj"] = (None)
    return pieces

# purpose: initializes the board upon restart button click
# parameters: board, infoB, boardDict, pieces, imgTurn
# return: pieces, turn, imgTurn
def initializeBoard(board, infoB, boardDict, pieces, imgTurn):
    player1, player2 = pieces
    turn = 0 
    for key in player1:
        pos = player1[key]["ipos"]
        name = player1[key]["imgName"]
        coord = boardDict[pos]['cp']
        piece = Image(coord,"img/"+name)
        player1[key]["gObj"] = piece
        piece.draw(board)
    for key in player2:
        pos = player2[key]["ipos"]
        name = player2[key]["imgName"]
        coord = boardDict[pos]['cp']
        piece = Image(coord,"img/"+name)
        player2[key]["gObj"] = piece
        piece.draw(board)
    print(pieces)    
    return pieces, turn, imgTurn

# purpose: updates the queen turn image colour
# parameters: imgTurn. board, iplayer
# return: imgTurn, board
def updateTurnImage(imgTurn, board, iplayer):
    x = 85
    y = 700
    if iplayer == 0:
        imgTurn = Image((Point(x,y)), "img/queen2.gif")
        imgTurn.draw(board)
    if iplayer == 1:
        imgTurn = Image((Point(x,y)), "img/queen1.gif")
        imgTurn.draw(board)
    return imgTurn, board

# purpose: gets the contents of a cell
# parameters: move, pieces
# return: piece, iplayer
def getContents(move, pieces):
    current_pos = move[0]
    player1, player2 = pieces
    iplayer = 1
    for key in player1:
        po_pos = player1[key]["cpos"]
        if current_pos == po_pos:
            piece = key
            iplayer = 0
            return (piece, iplayer)
    for key in player2:
        po_pos = player2[key]["cpos"]
        if current_pos == po_pos:
            piece = key
            iplayer = 1
            return (piece, iplayer)
    piece = "none"
    iplayer = "none"
    return (piece, iplayer)

# purpose: checks if a cell is occupied by a piece
# parameters: name, pieces
# return: true or false (bool)
def cellOccupied(name, pieces):
    # return true (not cp occupied) or false (cp occupied)
    player1, player2 = pieces
   
    for key in player1:
        po_pos = player1[key]["cpos"]
        if name == po_pos:
            return False
    for key in player2:
        po_pos = player2[key]["cpos"]
        if name == po_pos:
            return False
    
    return True

# purpose: updates piece once it moves
# parameters: board, iplayer, piece, move, pieces, boardDict
# return: board, pieces
def updatePiece(board, iplayer, piece, move, pieces, boardDict):
    player1, player2 = pieces
    current_pos = move[0]
    next_pos = move[1]

    if piece != "none":
        oldcp = (boardDict[current_pos]["cp"])
        newcp = (boardDict[next_pos]["cp"])
        pieces[iplayer][piece]["gObj"].undraw()
        image = Image(newcp,"img/"+pieces[iplayer][piece]["imgName"] )
        image.draw(board)
        pieces[iplayer][piece]["gObj"] = image
        pieces[iplayer][piece]["cpos"] = next_pos
    
    if piece == "none":
        print("Please Select A Piece")

    return board, pieces


if __name__ == "__main__":
    main()