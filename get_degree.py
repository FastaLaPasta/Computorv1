def get_degree(equation: dict) -> int:
    """
    equation: dict
    return: integer

    find the max key(power of X) of an equation then return it
    """
    return max((key for key, value in equation.items()), default=0)
