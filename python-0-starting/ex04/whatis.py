import sys


def whatis(number: int) -> str:
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return 1


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            number = int(sys.argv[1])
            whatis(number)
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: argument is not an integer")
