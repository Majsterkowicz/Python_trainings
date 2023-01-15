def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        return s[int((len(s)+1)/2)-1:int((len(s)+1)/2)]


test_string: str = "1234567"
print(get_middle(test_string))
