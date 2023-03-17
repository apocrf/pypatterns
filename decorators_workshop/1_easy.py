def multiplier(initial_string: str = "test", multiplicator: int = 3) -> str:
    """_summary_

    Args:
        initial_string (str, optional): _description_. Defaults to "test".
        multiplicator (int, optional): _description_. Defaults to 3.

    Returns:
        str: _description_
    """

    product_string = []

    for i in range(multiplicator):
        if i % 2 == 0:
            product_string.append(initial_string)
        else:
            product_string.append(initial_string.upper())

    return "".join(product_string)


# print(multiplier())

my_func = multiplier
print(my_func)
# <function multiplier at 0x7ffb2da13240> - обьект функции в памяти

print(my_func())
# testTESTtest - результат вызова