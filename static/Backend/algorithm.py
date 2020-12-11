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

    return False


# AI logic & processing
def calcNextMove(curBoard):
    if checkWinCond(curBoard) == True:
        return False
    else:
        xPos = [i for i, e in enumerate(curBoard) if e == "x"]
        print(xPos)
        return True
