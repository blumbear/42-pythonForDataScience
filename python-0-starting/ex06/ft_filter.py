def higher_than(a: int) -> bool:
    return a > 8


def ft_filter(func, object: any):
    """Return an iterator yielding those items of iterable for
    which function(item) is true. If function is None, return
    the items that are true."""
    if func is None:
        return [obj for obj in object if obj]
    return [obj for obj in object if func(obj) is True]


# def main():
#     data = [1, 5, 10, 3, 8, 15, 0, -2]

#     # Ton résultat vs le filter() natif
#     mine = list(ft_filter(higher_than, data))
#     ref = list(filter(higher_than, data))

#     print("data    :", data)
#     print("ft_filter:", mine)
#     print("filter   :", ref)
#     print("OK" if mine == ref else "KO")

#     # Cas limites
#     assert list(ft_filter(higher_than, [])) == []
#     print('1')
#     # Avec None comme fonction : garde les éléments "truthy"
#     assert list(ft_filter(None, [0, 1, "", "a", None])) == [1, "a"]
#     print('2')
#     print("Tous les tests passent")


# if __name__ == "__main__":
#     try:
#         main()
#     except AssertionError as e:
#         print("AssertionError: ", e)
