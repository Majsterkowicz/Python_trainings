# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples
# of 3 or 5 below the number passed in. Additionally, if the number
# is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number: int) -> int:
    number_list = []
    temp_number3: int = 0
    temp_number5: int = 0
    if number > 3:
        while temp_number3 < number:
            number_list.append(temp_number3)
            temp_number3 += 3
        while temp_number5 < number:
            if temp_number5 not in number_list:
                number_list.append(temp_number5)
            temp_number5 += 5
        return sum(number_list)
    else:
        return 0


test_number: int = 10
print(solution(test_number))
