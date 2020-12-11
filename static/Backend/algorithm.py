import random


# coinToss determines who goes first
def coinToss(Value):
    randToss = random.randint(0, 1)

    if Value == randToss:
        return True
    else:
        return False


# 3x3 Tic-Tac-Toe Grid
grid = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
