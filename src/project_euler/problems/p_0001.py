def _sum_divisible(multiple: int, divisor: int) -> int:
    """
    Calculate the sum of all integers that are divisible by a given `divisor` up to a given `multiple`,
    using the arithmetic series formula.

    Args:
    - multiple (int): The upper limit of the range of integers to check (exclusive).
    - divisor (int): The integer to check divisibility against.

    Returns:
    - int: The sum of all integers in the range [1, `multiple`) that are divisible by `divisor`.
    """
    p = (multiple - 1) // divisor
    return divisor * p * (p + 1) // 2


def p_0001(below: int = 1000) -> int:
    """
    Calculates the sum of all the multiples of 3 or 5 below `below` using a more efficient mathematical approach.

    Args:
    - below (int): The maximum number to consider (default is 1000).

    Returns:
    - int: The sum of all multiples of 3 or 5 below `below`.
    """
    return (
        _sum_divisible(below, 3) + _sum_divisible(below, 5) - _sum_divisible(below, 15)
    )
