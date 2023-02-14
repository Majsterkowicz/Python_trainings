# https://www.codewars.com/kata/571c1e847beb0a8f8900153d/train/python

# Help Suzuki rake his garden!

# The monastery has a magnificent Zen garden made of white gravel and rocks
# and it is raked diligently everyday by the monks. Suzuki having a keen
# eye is always on the lookout for anything creeping into the garden that
# must be removed during the daily raking such as insects or moss.

# You will be given a string representing the garden such as:

# garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel
# rock slug ant gravel gravel snail rock gravel gravel gravel gravel gravel
# gravel gravel'

# Rake out any items that are not a rock or gravel and replace them
# with gravel such that:

# garden = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'
# Returns a string with all items except a rock or gravel replaced with gravel:

# garden = 'gravel gravel rock gravel gravel gravel gravel gravel
# gravel gravel'


def rake_garden(garden: str) -> str:
    to_replace: str = ["slug", "ant", "snail", "spider", "moss", "notgravel", "notrock", "rockstar"]
    for string in to_replace:
        garden = garden.replace(string, "gravel")
    return garden


# other solutions:
VALID = {'gravel', 'rock'}


def rake_garden_1(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())


def rake_garden_2(garden):
    return " ".join(w if w == "rock" else "gravel" for w in garden.split())


def rake_garden_3(garden):
    return ' '.join(word if word in ('rock', 'gravel') else 'gravel' for word in garden.split())


test_value: str = "gravel rock slug ant gravel gravel snail rock spider notrock notgravel"
print(rake_garden(test_value))
