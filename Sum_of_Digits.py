# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n. If that value has more than
# one digit, continue reducing in this way until a single-digit number
# is produced. The input will be a non-negative integer.

# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# import math


def digital_root(n):
    new_number: int = 0
    while n > 9:
        # k: int = math.floor(math.log10(n) + 1)    # calculating number of digits
        new_number += n % 10
        n = n // 10
        if n < 10:
            n = new_number + n
            new_number = 0
    return n


# Other solutions of this Kata:


def digital_root_1(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


def digital_root_2(n):
    return n % 9 or n and 9


def digital_root_3(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


test_numer: int = 1170490020726345572
print(digital_root(test_numer))
