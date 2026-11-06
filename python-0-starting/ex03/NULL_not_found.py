def NULL_not_found(object: any) -> int:
    if object is None:
        tmp = "Nothing: None"
    elif isinstance(object, bool):
        tmp = "Fake: False"
    elif isinstance(object, float):
        tmp = "Cheese: nan"
    elif isinstance(object, int):
        tmp = "Zero: 0"
    elif object == '':
        tmp = "Empty: "
    else:
        print("Type not found")
        return 1
    print(tmp, type(object))
    return 0
