# In this kata, you need to return the number of bytes (aka. memory size)
# a given object takes up.

# Different variable types will be given, but they will all be valid.
# Also, random generation for strings takes out of Unicode, not the
# regular 255 ascii letters.


import sys


def total_bytes(object):
    return sys.getsizeof(object)


test_object = "78"
print(total_bytes(test_object))
