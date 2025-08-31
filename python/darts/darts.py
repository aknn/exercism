import math

def score(x, y):
    """
    Calculate the score in a darts game.
    """
    distance = math.sqrt(x**2 + y**2)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    return 0