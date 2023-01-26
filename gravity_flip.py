#  Take a list of numbers and sort it


def flip(d, a):
    if d == "R":
        a.sort()
        return a
    else:
        a.sort(reverse=True)
        return a


print(flip("L", [2, 4, 3, 1, 5]))
