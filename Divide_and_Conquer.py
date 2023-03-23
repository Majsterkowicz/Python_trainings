# https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python

# Given a mixed array of number and string representations of integers,
# add up the non-string integers and subtract the total of the string integers.

# Return as a number.


def div_con(arr) -> int:
    result: int = 0
    for x in arr:
        if isinstance(x, int):
            result += x
        else:
            result -= int(x)
    return result


# solution of other CodeWars users:

def div_con_2(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)


def div_con_3(x):
    return sum([a for a in x if isinstance(a, int)]) - sum([int(a) for a in x if not isinstance(a, int)])


test_array = [9, 3, '7', '3', 4, "3"]
print(div_con(test_array))
