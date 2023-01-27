# In this kata you will create a function that takes a my_list of non-negative
# integers and strings and returns a new my_list with the strings filtered out.

# Example:
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


def filter_list(my_list):
    new_list = []
    for x in my_list:
        if isinstance(x, int):
            new_list.append(x)
    return new_list
    # return my_list.remove(x for x in my_list if not (str(x).isdigit()))


test_list = [1, 'a', 6, 'b', 0, 15, 'c', 'b', '7', "b"]
print(filter_list(test_list))
