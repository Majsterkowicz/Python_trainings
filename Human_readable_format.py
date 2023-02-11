# Write a function, which takes a non-negative integer (sec)
# as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(sec):
    h: int = sec // 3600
    m: int = (sec % 3600) // 60
    s: int = sec % 60
    return '%s:%s:%s' % (str(h).zfill(2), str(m).zfill(2), str(s).zfill(2))
    # return '({}) {}-{}'.format(str1, str2, str3)


test_seconds: int = 8666
print(make_readable(test_seconds))
