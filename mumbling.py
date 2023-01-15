def accum(s: str) -> str:
    sub_str: str = ""
    new_str: str = ""
    counter: int = 0
    s = s.casefold()
    for x in s:
        counter += 1
        sub_str = x * counter
        new_str += sub_str.capitalize()
        # ''.join(sub_str.capitalize())
    return (new_str)


test_str: str = "addSae"
print(accum(test_str))
