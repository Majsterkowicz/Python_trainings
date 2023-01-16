# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
# This time no story, no theory.
# The examples below show you how to write function 'accum':
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s: str) -> str:
    # sub_str: str = ""
    new_str: str = ""
    counter: int = 0
    # s = s.casefold()
    for x in s.casefold():
        counter += 1
        # sub_str = x * counter
        # new_str += "-" + (x * counter).capitalize()
        '-'.join(("-" + (x * counter).capitalize()).capitalize())
    # return (('-'.join(x * range(s) for x in (s.casefold()))))
    return (new_str[1:])


test_str: str = "addSae"
print(accum(test_str))
