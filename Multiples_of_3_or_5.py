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
