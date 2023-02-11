# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
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

# Another solutions from CodeWars:


def make_readable_1(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


def make_readable_2(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


def make_readable_3(seconds):
    h = seconds/60**2
    m = (seconds % 60**2)/60
    s = (seconds % 60**2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)


test_seconds: int = 8666
print(make_readable(test_seconds))
