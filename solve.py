from typing import Dict
from get_degree import get_degree


def print_degree(equation: Dict[int, float]) -> int:
    degree = get_degree(equation)
    if 0 < degree < 3:
        print(f"Polynomial degree: {degree}")
    return degree


def solve(equation: Dict[int, float]) -> str:
    """
    equation: dict, dict of the equation on a reduce form. ex: f(x) = 0
    return: str, value(s) of x for f(x) = 0.

    Get the degree of the equation,
    then process to solve it by using the delta if necessary.
    """
    degree = print_degree(equation)

    a = equation.get(2, 0)
    b = equation.get(1, 0)
    c = equation.get(0, 0)
    if degree == 0:
        return "Any real number is a solution." if c == 0 else "No solution."

    elif degree == 1:
        if not b == 0:
            return f"The solution is:\n{-c / b}"
        return "No solution."

    elif degree == 2:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b - delta**0.5) / (2 * a)
            x2 = (-b + delta**0.5) / (2 * a)
            return f"Discriminant is strictly positive, the two solutions are\n{x1}\n{x2}"
        elif delta == 0:
            x = -b / (2 * a)
            return f"The solution is:\n{x}"
        else:
            real = -b / (2 * a)
            imag = (abs(delta)**0.5) / (2 * a)
            return f"Discriminant is strictly negative, the two complex solutions are:\n{real} - {imag}i\n{real} + {imag}i"
    return f"The polynomial degree {degree} is strictly greater than 2, I can't solve."
