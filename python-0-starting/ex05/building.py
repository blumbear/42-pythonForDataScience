import sys


punctuation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"


def main(string: str) -> int:
    """ Takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters, digits and
    spaces."""
    res = {"upper": 0, "lower": 0, "punc": 0, "space": 0, "digit": 0}
    for i in string:
        if i.isupper():
            res["upper"] += 1
        elif i.islower():
            res["lower"] += 1
        elif i.isdigit():
            res["digit"] += 1
        elif i in punctuation:
            res["punc"] += 1
        elif i in " \n":
            res["space"] += 1

    print(f"The text contains {len(string)} characters:")
    print(res["upper"], "upper letters")
    print(res["lower"], "lower letters")
    print(res["punc"], "punctuation marks")
    print(res["space"], "spaces")
    print(res["digit"], "digits")


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 1:
            print("Give a string as an argument.\nExemple: \"test12Rqzd  ',\"")
        else:
            main(sys.argv[1])
    except AssertionError as e:
        print("AssertionError :", e)

# print(main.__doc__)
# "aqsdqsd   a ZA 1  :;,:,23\nmllqsjkd"
