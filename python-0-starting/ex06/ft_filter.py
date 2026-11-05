def ft_filter(func, object: any):
    return [obj for obj in object if func(obj) is True]
