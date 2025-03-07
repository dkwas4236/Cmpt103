# -------------------------------------------
# Integrity Pledge:
#   The work that I am submitting is my own.
#   It was completed in accordance with
#   MacEwan's Academic Integrity Policy - DK
# -------------------------------------------
# Name:     Darion Kwasnitza
# Program:  chessmovesDK.py
# -------------------------------------------
# Purpose:  This program will check if moves
#           on a chess board are valid for 
#           various pieces
import math

# purpose: def checkMoved() will check if the piece was actually moved
# parameter: currentPos, nextPos
# return: True or False

def checkMoved(currentPos, nextPos):
    if currentPos != nextPos:
        return True
    else: 
        return False

# purpose: def checkBounds() will check if the next move is in bounds of the chess board
# parameter: nextPos
# return: True or False

def checkBounds(nextPos):
    if len(nextPos) > 2:
        return False
    else:
        column = nextPos[0]
        row = nextPos[1]
        row = int(row)
    if column.upper() >= "A" and column.upper() < "I":
        if row > 0 and row < 9:
            return True
        else:
            return False
    else:
        return False

# purpose: def checkRookMove() will check if a move is possible for a rook game piece to make
# parameter: currentPos, nextPos
# return: True or False

def checkRookMove(currentPos, nextPos):
    if checkMoved(currentPos, nextPos):
        if checkBounds(nextPos):
            newColumn = nextPos[0]
            newRow = nextPos[1]
            newRow = int(newRow)
            column = currentPos[0]
            row = currentPos[1]
            row = int(row)
    
# if rook stays in same column then row must be changed:
            if column.upper() == newColumn.upper():
                if row != newRow:
                    return True
                else:
                    return False
 # if rook stay in same row then column must be changed:     
            if column.upper() != newColumn.upper():
                if row == newRow:
                    return True
                else:
                    return False
            else:
                return False
        else: 
            return False        
    else:
        return False

# purpose: def checkBishopMove() will check if a move is possible for a bishop game piece to make
# parameter: currentPos, nextPos
# return: True or False

def checkBishopMove(currentPos, nextPos):
    if checkMoved(currentPos, nextPos):
        if checkBounds(nextPos):
            newColumn = nextPos[0]
            newRow = nextPos[1]
            newRow = int(newRow)
            column = currentPos[0]
            row = currentPos[1]
            row = int(row)
            netRow = row - newRow
            netColumn = ord(column) - ord(newColumn)
            if abs(netRow) == abs(netColumn):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# purpose: def checkKingMove() will check if a move is possible for a king game piece to make
# parameter: currentPos, nextPos
# return: True or False

def checkKingMove(currentPos, nextPos):
    if checkMoved(currentPos, nextPos):
        if checkBounds(nextPos):
            newColumn = nextPos[0]
            newRow = nextPos[1]
            newRow = int(newRow)
            column = currentPos[0]
            row = currentPos[1]
            row = int(row)
# if king moves vertical:
            if (row + 1 == newRow or row - 1 == newRow) and column == newColumn:
                return True
# if king moves horizontal:
            if ((ord(column) + 1) == ord(newColumn) or (ord(column) - 1) == ord(newColumn)) and row == newRow:
                return True
# if king moves diagonal:
            if ((ord(column) + 1) == ord(newColumn) or (ord(column) - 1) == ord(newColumn)) and (row + 1 == newRow or row - 1 == newRow):
                return True
            else:
                return False
        else:
            return False
    else: 
        return False

# purpose: def checkQueenMove() will check if a move is possible for a queen game piece to make
# parameter: currentPos, nextPos
# return: True or False

def checkQueenMove(currentPos, nextPos):
    if checkMoved(currentPos, nextPos):
        if checkBounds(nextPos):
            if checkRookMove(currentPos, nextPos) or checkBishopMove(currentPos, nextPos) or checkKingMove(currentPos, nextPos):
                return True
            else:
                return False

# purpose: def isValidMove() will check if a move is possible for a specified chess piece
# parameter: piece, currentPos, nextPos
# return: True or False

def isValidMove(piece, currentPos, nextPos):
    if checkMoved(currentPos, nextPos):
        if checkBounds(nextPos):
            if piece.lower() == "rook":
                isvalid = checkRookMove(currentPos, nextPos)
            elif piece.lower() == "bishop":
                isvalid = checkBishopMove(currentPos, nextPos)
            elif piece.lower() == "king":
                isvalid = checkKingMove(currentPos, nextPos)
            elif piece.lower() == "queen":
                isvalid = checkQueenMove(currentPos, nextPos)
            else:
                
                isvalid =  False
        else:
            isvalid = False
    else:
        isvalid = False 

    print(isvalid)   


