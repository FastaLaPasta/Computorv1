from typing import Dict


def reduce_form(left: dict, right: dict) -> Dict[int, float]:
    """
    left: dict, contain the left part of an initial equation
    right: dict, contain the right part of an initial equation
    return: dict, the final dict representation of the equation, ex:f(x) = 0

    Pass all the arguments on the right side to the left to get a dictionnary
    representation of f(x)=0 equation.
    """
    for power, coef in right.items():
        if power in left:
            left[power] -= coef
        else:
            left[power] = -coef
    return left
