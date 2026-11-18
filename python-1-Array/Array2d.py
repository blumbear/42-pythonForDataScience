# import numpy as np 

def slice_me(family: list, start: int, end: int) -> list:
    tmp = len(family[0])
    for i in family:
        if len(i) != tmp:
            raise AssertionError("List in family must have the same size.")
    print(f"My shape is : ({len(family)}, {tmp})")
    family = family[start:end]
    print(f"My new shape is : ({len(family)}, {tmp})")
    return family

if __name__ == "__main__":
    family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print("-----")
        print(slice_me(family, 1, -2))
        print("-----")
        print(slice_me(5, 1, -2))
    except AssertionError as e:
        print("AssertionError : ", e)
    except ValueError as e :
        print("ValueError: ", e)
    except:
        print("Error")
