def all_thing_is_obj(object: any) -> int:
    tmp = ''
    if isinstance(object, list):
        tmp = "List"
    elif isinstance(object, tuple):
        tmp = "Tuple"
    elif isinstance(object, set):
        tmp = "Set"
    elif isinstance(object, dict):
        tmp = "Dict"
    elif isinstance(object, str):
        tmp = object + " is in the kitchen"
    else:
        print("Type not found")
        return 42
    print(tmp, ':', type(object))
    return 42
