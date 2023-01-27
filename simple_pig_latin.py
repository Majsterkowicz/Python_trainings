# Move the first letter of each word to the end of it, then add "ay"
# to the end of the word. Leave punctuation marks untouched.

# Examples:
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text: str) -> str:
    # string: str = ""
    # string = text.split(" ")
    # result: str = ""
    # for x in string:
        # letter: str = x[.1]
        # new_string: str = " " + x[1:] + x[:1] + "ay"
        # result += new_string
    s: str = ' '.join(x[1:] + x[:1] + "ay" for x in text.split(" ") if x.isalpha())
    if text[-1:].isalpha():
        return s
    else:
        return s + " " + text[-1:]


test_text: str = "O tempora o mores !"
print(pig_it(test_text))
