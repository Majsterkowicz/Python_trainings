# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python

# When working with color values it can sometimes be useful to
# extract the individual red, green, and blue (RGB) component values
# for a color. Implement a function that meets these requirements:

# Accepts a case-insensitive hexadecimal color string as its
# parameter (ex. "#FF9933" or "#ff9933")
# Returns a Map<String, int> with the structure
# {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
# Note: your implementation does not need to support the shorthand
# form of hexadecimal notation (ie "#FFF")

# Example
# "#FF9933" --> {r: 255, g: 153, b: 51}


def hex_string_to_RGB(input):
    r_num: int = int((input[1:3]), 16)
    g_num: int = int((input[3:5]), 16)
    b_num: int = int((input[5:7]), 16)
    return {'r': r_num, 'g': g_num, 'b': b_num}


input_hex: str = "#ff9933"
print(hex_string_to_RGB(input_hex))
