import sys


less_than = lambda obj, size: len(obj) > size


def main(string: str, size: int) -> list:
    tmp = string.split(' ')
    res = [obj for obj in tmp if less_than(obj, size)]
    return res


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
