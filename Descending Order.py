def descending_order(num: int) -> int:
    # number_list = []
    # new_number: str = ""
    # new_int: int = 0
    # for n in str(num):
    #     number_list.append(n)
    # number_list.sort(reverse=True)
    new_int = int(''.join(sorted([n for n in str(num)], reverse=True)))
    # number_list.sort(reverse=True)
    # for x in number_list:
    #     new_number += x
    print(new_int)
    return (int(new_int))


test_number: int = 12345
print(descending_order(test_number))
