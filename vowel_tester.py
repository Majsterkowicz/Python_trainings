def disemvowel(string: str) -> str:
    # letters: str = "aeiou"
    # lett: str = ""
    # result: str = ""
    # for lett in string:
    #     if lett not in letters:
    #         result = result + lett
    # return result
    return ''.join(lett for lett in string if lett not in "aeiouAEIOU")


test_string: str = "Testuj razem z nami obywatelami"
print(disemvowel(test_string))
print("dupa")
