def higher_than(a: int) -> bool:
    return a > 8


def ft_filter(func, object: any):
    return [obj for obj in object if func(obj) is True]


print(ft_filter(higher_than, [1, 12, 45, 2, 4, 51]))
