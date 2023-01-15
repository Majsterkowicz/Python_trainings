def highest_and_lowest(numbers: str) -> str:
    number_current: str = ""
    # string_max: str = "0"
    # string_min: str = "0"
    # number_max: int = 0
    # number_min: int = 0
    counter: int = 0
    # first_number: bool = True
    number_list = []
    print(numbers)

    for x in numbers:
        counter += 1
        if x.isdigit() or x == "-":
            print("x= " + x)
            number_current += x
            print("number_current= " + number_current)
        if x == " " or len(numbers) == counter:
            number_list.append(int(number_current))
            number_current = ""
    #         print("counter" + str(counter))
    #         print("spacja")

            # if first_number is True:
            #     number_max = int(number_current)
            #     number_min = int(number_current)
            #     number_current = ""
            #     first_number = False
    #         elif int(number_current) > number_max:
    #             print("number_max" + str(number_max))
    #             number_max = int(number_current)
    #             print("number_max= " + str(number_max))
    #             number_current = ""
    #         elif int(number_current) < number_max:
    #             if int(number_current) < number_min:
    #                 number_min = int(number_current)
    #             print("number_min" + str(number_min))
    #             print("number_min= " + str(number_min))
    #             number_current = ""
    # string_max = str(number_max)
    # string_min = str(number_min)
    print(number_list)
    return (str(max(number_list)) + " " + str(min(number_list)))
    # return (string_max + " " + string_min)


test_numbers: str = "1 1 10"
print(highest_and_lowest(test_numbers))
