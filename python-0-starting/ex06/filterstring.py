import sys
from ft_filter import ft_filter


def main(string: str, size: int) -> list:
    """The program output a list of words from S that have a length
    greater than N."""
    tmp = string.split(' ')
    return ft_filter(lambda obj: len(obj) > size, tmp)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 3:
            raise AssertionError("more than 2 argument is provided")
        elif len(sys.argv) < 3:
            raise AssertionError("less than 2 argument is provided")
        else:
            test = int(sys.argv[2])
            print(main(sys.argv[1], int(sys.argv[2])))
    except AssertionError as e:
        print("AssertionError :", e)
    except ValueError:
        print("Wrong Value, you must give a string",
              "and an integer, in this order.")

# print(main.__doc__)