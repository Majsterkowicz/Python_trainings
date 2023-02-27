# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

# A Narcissistic Number (or Armstrong Number) is a positive number
# which is the sum of its own digits, each raised to the power of
# the number of digits in a given base. In this Kata, we will
# restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:

# Your code must return true or false (not 'true' and 'false')
# depending upon whether the given number is a Narcissistic
# number in base 10.

# This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs
# is not required, only valid positive non-zero integers
# will be passed into the function.


def narcissistic(n: int) -> bool:
    new_number: int = 0
    digits: int = len(str(n))
    nn: int = n
    while nn > 0:
        new_number += (nn % 10) ** digits
        nn = nn // 10
    if n == new_number and nn == 0:
        print(new_number)
        return True
    else:
        print(new_number)
        return False


# other solutions of CodeWars users:


def narcissistic_1(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))


def narcissistic_2(value):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)


def narcissistic_3(value):
    return bool(value == sum([int(a) ** len(str(value)) for a in str(value)]))


def narcissistic_4(value):
    vstr = str(value)
    nvalue = sum(int(i)**len(vstr) for i in vstr)
    return nvalue == value


test_number: int = 153
print(narcissistic(test_number))
