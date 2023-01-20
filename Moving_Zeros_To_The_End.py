# Write an algorithm that takes an array and moves all of the zeros
# to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3])
# returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    n: int = lst.count(0)
    if n == 0:
        return lst
    else:
        nlst = [i for i in lst if i != 0]
    for i in range(n):
        nlst.append(0)
    return nlst


test_list = [1, 0, 1, 2, 0, 1, 3, 5, 0, 5, 0, 0, 0, 5, 2, 3, 65, 2, 6]
print(move_zeros(test_list))
