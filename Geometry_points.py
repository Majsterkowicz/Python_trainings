# https://www.codewars.com/kata/58dced7b702b805b200000be/train/python

# This series of katas will introduce you to basics of doing geometry with computers.

# Point objects have attributes x and y.

# Write a function calculating distance between Point a and Point b.

# Input coordinates fit in range −50⩽x,y⩽50 -50 \leqslant x,y \leqslant 50 −50⩽x,y⩽50.
# Tests compare expected result and actual answer with tolerance of 1e-6.

import math

def distance_between_points(pointA, pointB):
    disX: int = pointB[0] - pointA[0]
    disY: int = pointB[1] - pointA[1]
    result: float = math.sqrt(pow(disX, 2) + pow(disY, 2))
    if result % 1 != 0:
        result = ("{:.6f}".format(result))
    else:
        result = ("{:.0f}".format(result))
    return result

point1: int = (0, 6)
point2: int = (4, 7)
print(distance_between_points(point1, point2))