# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

# Your goal in this kata is to implement a difference function, which
# subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list
# b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed
# from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    # output_a = []
    # for elmnt in a:
    #     if elmnt not in b:
    #         output_a.append(elmnt)
    # return output_a
    setb = set(b)
    return [elmnt for elmnt in a if elmnt not in setb]


# some others solutions from CodeWars users:
def array_diff_1(a, b):
    return filter(lambda i: i not in b, a)


def array_diff_2(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a


def array_diff_3(a, b):
    for n in b:
        while (n in a):
            a.remove(n)
    return a


test_array_a = [1, 2, 3, 2, 3, 3, 2, 1, 5]
test_array_b = [1, 2]
print(array_diff(test_array_a, test_array_b))
