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
    for row in currentBoard[::3]:
        if currentBoard[index] == "x" and currentBoard[index] == currentBoard[index + 1] and currentBoard[index + 1] == currentBoard[index + 2]:
            return xWin
        elif currentBoard[index] == "o" and currentBoard[index] == currentBoard[index + 1] and currentBoard[index + 1] == currentBoard[index + 2]:
            return yWin
        index += 3
    # Checking Columns
    index = 0
    for colm in currentBoard[:3]:
        if currentBoard[index] == "x" and currentBoard[index] == currentBoard[index + 3] and currentBoard[index + 3] == currentBoard[index + 6]:
            return xWin
        if currentBoard[index] == "o" and currentBoard[index] == currentBoard[index + 3] and currentBoard[index + 3] == currentBoard[index + 6]:
            return yWin
        index += 1
    # Checking Diagonal [0]-->[4]-->[8]
    if currentBoard[0] == "x" and currentBoard[4] == "x" and currentBoard[8] == "x":
        return xWin
    if currentBoard[0] == "o" and currentBoard[4] == "o" and currentBoard[8] == "o":
        return yWin
    # Checking Diagonal [2]-->[4]-->[6]
    if currentBoard[2] == "x" and currentBoard[4] == "x" and currentBoard[6] == "x":
        return xWin
    if currentBoard[2] == "o" and currentBoard[4] == "o" and currentBoard[6] == "o":
        return yWin
    if "none" not in currentBoard:
        return draw
    else:
        return None


def calcNextMove(curBoard, depth, MaxMin):
    # next AI Move
    bestScore = -math.inf
    nextMove = 0
    i = 0
    for n in curBoard:
        if n == "none":
            curBoard[i] = "o"
            mMScore = miniMax(curBoard, depth, MaxMin)
            print("Depth:", depth, "[Nth Number:]", i, "___", mMScore)
            curBoard[i] = "none"
            if mMScore > bestScore:
                bestScore = mMScore
                nextMove = i
            i += 1
        else:
            i += 1
            print("skipped")
    return nextMove


scores = {
    "xWin": 1,
    "yWin": -1,
    "draw": 0
}


# miniMax Algorithm
def miniMax(currBoard, depth, MinOrMax):
    # if(depth <= 1):
    #     print(currBoard)
    # Check if AI has won
    result = checkWinCond(currBoard)
    if result != None:
        return scores[result]

    if MinOrMax:
        MinOrMax = not MinOrMax
        bestScore = -math.inf
        i = 0
        for n in currBoard:
            if n == "none":
                currBoard[i] = "o"
                score = miniMax(currBoard, depth + 1, False)
                currBoard[i] = "none"
                bestScore = max(score, bestScore)
            i += 1
        return bestScore
    else:
        bestScore = math.inf
        i = 0
        for n in currBoard:
            if n == "none":
                currBoard[i] = "x"
                score = miniMax(currBoard, depth + 1, True)
                currBoard[i] = "none"
                bestScore = min(score, bestScore)
            i += 1
        return bestScore
