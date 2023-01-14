def get_count(sentence: str) -> int:
    # letters: list = ["a", "e", "i", "o", "u"]
    # count: int = 0
    # for letter in "aeiou":
    #     count = count + sentence.lower().count(letter)
    # return count
    # count = [sentence.lower().count(letter) for letter in "aeiou"]
    # print(count)
    return sum(sentence.lower().count(letter) for letter in "aeiou")


test_string: str = "AaEeIiOofgfhgfjg"
print(get_count(test_string) == 8)
print("dupa")
