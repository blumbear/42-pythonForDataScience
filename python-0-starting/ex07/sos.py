import sys


morse_alphabet = {
    # Lettres
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',

    # Chiffres
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',

    ' ': '/'
}


def sos(message: str) -> str:
    """A program that takes a string as an argument and encodes
    it into Morse Code:
    • The program supports space and alphanumeric characters
    • An alphanumeric character is represented by dots . and dashes -
    • Complete morse characters are separated by a single space
    • A space character is represented by a slash /"""
    res = ''
    for i in message:
        if i.upper() not in morse_alphabet:
            raise AssertionError("wrong character in string")
        res += (morse_alphabet[i.upper()] + " ")
    print(res[:-1])


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than 1 argument is provided")
        elif len(sys.argv) < 2:
            raise AssertionError("less than 1 argument is provided")
        else:
            sos(sys.argv[1])
    except AssertionError as e:
        print("AssertionError :", e)

print(sos.__doc__)
