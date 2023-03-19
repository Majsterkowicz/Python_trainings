# https://www.codewars.com/kata/632408defa1507004aa4f2b5/train/python

# This kata is about static method that should return different values.

# On the first call it must be 1, on the second and others - it must
# be a double from previous value.

# Look tests for more examples, good luck :)


class Class:
    counter: int = 0

    @staticmethod
    def get_number():
        result: int = 2 ** Class.counter
        Class.counter += 1
        return result


print(Class.get_number())
print(Class.get_number())
print(Class.get_number())
