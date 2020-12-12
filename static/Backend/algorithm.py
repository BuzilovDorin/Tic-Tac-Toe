import random
import math


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
    draw = "draw"
    index = 0
    if "none" not in currentBoard:
        return draw
    for row in currentBoard[::3]:
        if row == "x":
            if currentBoard[index + 1] == "x" and currentBoard[index + 2] == "x":
                return xWin
        if row == "o":
            if currentBoard[index + 1] == "o" and currentBoard[index + 2] == "o":
                return yWin
        index += 3
    # Checking Columns
    index = 0
    for colm in currentBoard[:3]:
        if colm == "x":
            if currentBoard[index + 3] == "x" and currentBoard[index + 6] == "x":
                return xWin
        if colm == "o":
            if currentBoard[index + 3] == "o" and currentBoard[index + 6] == "o":
                return yWin
        index += 1
    # Checking Diagonal [0]-->[4]-->[8]
    if currentBoard[0] == "x" and currentBoard[4] == "x" and currentBoard[8] == "x":
        return xWin
    if currentBoard[0] == "o" and currentBoard[4] == "o" and currentBoard[8] == "o":
        return yWin
    # Checking Diagonal [2]-->[4]-->[8]
    if currentBoard[2] == "x" and currentBoard[4] == "x" and currentBoard[6] == "x":
        return xWin
    if currentBoard[2] == "o" and currentBoard[4] == "o" and currentBoard[6] == "o":
        return yWin


def calcNextMove(maxOrMin, curBoard):
    # Check if human Player has won
    winner = checkWinCond(curBoard)
    if winner:
        return winner

    else:
        # AI logic & processing
        print(maxOrMin)
        xPos = [i for i, e in enumerate(curBoard) if e == "x"]
        print("Current X Pos: ", xPos)

        # Check if AI has won
        winner = checkWinCond(curBoard)
        if winner:
            return winner


board = ["o", "x", "o", "x", "x", "o", "none", "o",  "none"]


def checkWinCond(currentBoard):
    # There is 8 possible checks for 3 in a row: 3 rows, 3 columns, 2 diagonal possibilities
    # Since I am using a 1 dimentional array I need to iterate through the values in jumps of 3
    # Checking rows
    xWin = "xWin"
    yWin = "yWin"
    draw = "draw"
    index = 0
    if "none" not in currentBoard:
        return draw
    for row in currentBoard[::3]:
        if row == "x":
            if currentBoard[index + 1] == "x" and currentBoard[index + 2] == "x":
                return xWin
        if row == "o":
            if currentBoard[index + 1] == "o" and currentBoard[index + 2] == "o":
                return yWin
        index += 3
    # Checking Columns
    index = 0
    for colm in currentBoard[:3]:
        if colm == "x":
            if currentBoard[index + 3] == "x" and currentBoard[index + 6] == "x":
                return xWin
        if colm == "o":
            if currentBoard[index + 3] == "o" and currentBoard[index + 6] == "o":
                return yWin
        index += 1
    # Checking Diagonal [0]-->[4]-->[8]
    if currentBoard[0] == "x" and currentBoard[4] == "x" and currentBoard[8] == "x":
        return xWin
    if currentBoard[0] == "o" and currentBoard[4] == "o" and currentBoard[8] == "o":
        return yWin
    # Checking Diagonal [2]-->[4]-->[8]
    if currentBoard[2] == "x" and currentBoard[4] == "x" and currentBoard[6] == "x":
        return xWin
    if currentBoard[2] == "o" and currentBoard[4] == "o" and currentBoard[6] == "o":
        return yWin


def miniMax(currBoard, depth, MinOrMax):
    w = checkWinCond(currBoard)
    if w:
        return w

    # Maximizing = True (first move)
    if MinOrMax == True:
        bestMove = -math.inf
        print("best move start:"), bestMove
        i = 0
        for n in currBoard:
            if n == "none":
                print("######", i)
                board[i] = "o"
                i + 1
                score = miniMax(currBoard, depth + 1, not MinOrMax)
                i - 1
                board[i] = "none"
                bestMove = max(score, bestMove)
                print("best move :", bestMove)
            else:
                i += 1
                pass
        print(bestMove)
        return bestMove
    else:
        # Maximizing = False (Second move)
        bestMove = math.inf
        print("best move start:"), bestMove
        i = 0
        for n in currBoard:
            if n == "none":
                print("######", i)
                board[i] = "x"
                i + 1
                score = miniMax(currBoard, depth + 1, not MinOrMax)
                i - 1
                board[i] = "none"
                bestMove = max(score, bestMove)
                print("best move :", bestMove)
            else:
                i += 1
                pass
        print(bestMove)
        return bestMove


nM = miniMax(board, 0, True)
print(nM)
print(board)
