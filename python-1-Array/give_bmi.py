# import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float])-> list[int | float]:
    """ This function take 2 lists of integers or floats in input and returns a list
    of BMI value. """
    if len(height) != len(weight):
        raise AssertionError("The length of list are not equal.")
    # if not all ((np.issubdtype(height.dtype, np.number) and np.issubdtype(weight.dtype, np.number))):
    if not all (isinstance(x, (int, float)) for lst in (height, weight) for x in lst):
        raise AssertionError(f"The type of values must be {int} or {float}.")

    res = []
    for w, h in zip(weight, height):
        if w <= 0 or h <= 0:
            raise AssertionError("The weight and the height must be positive.")
            return []
        res.append(w/((h)**2))
    return res
    

def apply_limit(bmi: list[int | float], limit: int)-> list[bool]:
    """ This function accepts a list of integers or floats and 
    an integer representing a limit as parameters. It returns a 
    list of booleans (True if above the limit)."""
    # if not all ((np.issubdtype(height.dtype, np.number) and np.issubdtype(weight.dtype, np.number))):
    if not all (isinstance(x, (int, float)) for x in (bmi)):
        raise AssertionError(f"The type of values in list must be {int} or {float}.")
    if not isinstance(limit, int):
        raise AssertionError(f"The type of limit must be {int}")
    return [x > limit for x in bmi]


if __name__ == "__main__":
    try:
        res = give_bmi([2.71, 1.15], [165.3, 38.4])
        print(res)
        print(apply_limit(res, 25))
        # print(give_bmi(["2"], [165.3]))
    except AssertionError as e:
        print("AssertionError :", e)
