import random


def summator_3(
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
    # if args:
    for elem in args[:2]:
        result += elem

    # if kwargs: можно не проверять, проверка происходит автоматически
    kwargs_len = len(kwargs.values())
    random_index_from_dictvalues = random.randint(1, kwargs_len)
    elem = tuple(kwargs.values())[random_index_from_dictvalues - 1]
    result += elem

    return result


print(summator_3(1, 2, 3, 4, 5, 6, 7, 8, kw1=9, kw2=10))
