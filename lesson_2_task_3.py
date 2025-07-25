import math


def square(side):
    if (side != math.ceil(side)):
        return math.ceil(side*side)
    else:
        return side*side


res = square(3.5)
print(res)
