def square_digits(num: int) -> int:
    # result: str = ""
    # for n in str(num):
    #     result = result + str(int(n)*int(n))
    # return int(result)
    return int(''.join(str(int(n) * int(n)) for n in str(num)))


test_number: int = 1234
print((square_digits(test_number)) + 10)
