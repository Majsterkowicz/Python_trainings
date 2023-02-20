# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python

# Given is a md5 hash of a five digits long PIN. It is given as string.
# Md5 is a function to hash your password: "password123" ===>
# "482c811da5d5b4bc6d497ffa98491e38"

# Why is this useful? Hash functions like md5 can create a hash from
# string in a short time and it is impossible to find out the password,
# if you only got the hash. The only way is cracking it, means try
# every combination, hash it and compare it with the hash you want to crack.
# (There are also other ways of attacking md5 but that's another story)
# Every Website and OS is storing their passwords as hashes, so if a hacker
# gets access to the database, he can do nothing, as long the password
# is safe enough.


import hashlib
from hashlib import md5         # for example no2
from itertools import product   # for example no2


def crack(hash: str) -> str:
    for x in range(0, 100000):
        str_pin: str = "{:05}".format(x)
        pin_hashed: str = (hashlib.md5(str_pin.encode())).hexdigest()
        if hash == pin_hashed:
            return str_pin


# some solutions of users of CodeWars
def crack_1(hash):
    for i in range(100000):
        if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash:
            return str(i).zfill(5)
        

def crack_2(hash):
    for bs in map(bytes, product(b'0123456789', repeat=5)):
        if md5(bytes(bs)).hexdigest() == hash:
            return bs.decode()


# given_hash: str = "827ccb0eea8a706c4c34a16891f84e7b"          # hashed "12345"
given_hash: str = "d3eb9a9233e52948740d7eb8c3062d14"          # hashed "99999"
# given_hash: str = "e72581f8614727a152dec6fcfc739ad2"            # hashed "00005"
print(crack(given_hash))
