# https://www.codewars.com/kata/5521d84b95c172461d0000a4/train/python

# Convert a number to a binary coded decimal (BCD).

# You can assume input will always be an integer.
# If it is a negative number then simply place a minus sign
# in front of the output string. Output will be a string with
# each digit of the input represented as 4 bits (0 padded) with
# a space between each set of 4 bits.

# Ex.

# n =  10 -> "0001 0000"
# n = -10 -> "-0001 0000"


def to_bcd(n):
    # value = str(n)
    # result = []
    # for x in value:
    #     result.append(f'{int(x):04b}')
    # return ' '.join(result)
    if n >= 0:
        return ' '.join((f'{int(x):04b}') for x in str(n))
    else:
        return "-" + ' '.join((f'{abs(int(x)):04b}') for x in str(abs(n)))


test_int: int = -16
print(to_bcd(test_int))
