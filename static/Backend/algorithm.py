import random


# coinToss determines who goes first
def coinToss(Value):
    randToss = random.randint(0, 1)

    if Value == randToss:
        return True
    else:
        return False


# Check to see if there is a win condition satisfied
def checkWinCond(currentBoard):
    # There is 8 possible checks for 3 in a row: 3 rows, 3 columns, 2 diagonal possibilities
    # Since I am using a 1 dimentional array I need to iterate through the values in jumps of 3
    # Checking rows
    xWin = "xWin"
    yWin = "yWin"
    for row in currentBoard[::3]:
        if row == "x":
            if currentBoard[1] and currentBoard[2] == "x":
                return xWin
        if row == "o":
            if currentBoard[1] and currentBoard[2] == "o":
                return yWin
    # Checking Columns
    for colm in currentBoard[:3]:
        if colm == "x":
            if currentBoard[3] and currentBoard[6] == "x":
                return xWin
        if colm == "o":
            if currentBoard[3] and currentBoard[6] == "o":
                return yWin
    # Checking Diagonal [0]-->[4]-->[8]
    if currentBoard[0] and currentBoard[4] and currentBoard[8] == "x":
        return xWin
    if currentBoard[0] and currentBoard[4] and currentBoard[8] == "o":
        return yWin
    # Checking Diagonal [2]-->[4]-->[8]
    if currentBoard[0] and currentBoard[4] and currentBoard[8] == "x":
        return xWin
    if currentBoard[0] and currentBoard[4] and currentBoard[8] == "o":
        return yWin

    return False


# AI logic & processing
def calcNextMove(curBoard):
    winner = checkWinCond(curBoard)
    if winner:
        print(winner)
        return True
    else:
        xPos = [i for i, e in enumerate(curBoard) if e == "x"]
        print("Current X Pos: ", xPos)
        return True
