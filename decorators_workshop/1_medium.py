# 1
def summator(*args: int) -> int:
    """_summary_

    Returns:
        int: _description_
    """
    result = 0
    for elem in args:
        result += elem
    return result


# print(summator(1, 2, 3, 4, 5))

# 2
def summator_2(
    first: int, second: int, third: int, fourth: int, *args: int, **kwargs: int
) -> int:
    """_summary_

    Args:
        first (int): _description_
        second (int): _description_
        third (int): _description_
        fourth (int): _description_

    Returns:
        int: _description_
    """
    result = sum((first, second, third, fourth))
    for elem in args:
        result += elem

    for elem in kwargs.values():
        result += elem

    return result

# print(summator_2(1))
# TypeError: summator_2() missing 3 required positional arguments: 'second', 'third', and 'fourth'
# ошибка так как функция ожидает еще 3 позиционных аргумента


# print(summator_2(1, 2, 3, 4,first=1))
# TypeError: summator_2() got multiple values for argument 'first'
# ошибка так как first уже передан позиционно

t = (1, 2, 3, 4)

print(summator_2(*t))

d = {"first": 1, "second": 2, "third": 3, "fourth": 4}

# print(summator_2(*d))
# TypeError: unsupported operand type(s) for +: 'int' and 'str' - так мы распакуем ключи

print(summator_2(**d)) # так распаковка произошла правильно, имени српоставлися ключ и присвоилось значение
