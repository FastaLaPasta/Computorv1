import math
from typing import Dict
from get_degree import get_degree


def solve(equation: Dict[int, float]) -> str:
    degree = get_degree(equation)

    a = equation.get(2, 0)
    b = equation.get(1, 0)
    c = equation.get(0, 0)
    if degree == 0:
        return "All real numbers are solutions." if c == 0 else "No solution."

    elif degree == 1:
        if not b == 0:
            return -c / b
        return "No solution."

    elif degree == 2:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b - delta**0.5) / (2 * a)
            x2 = (-b + delta**0.5) / (2 * a)
            return f"Discriminant > 0. Two real solutions:\nx1 = {x1}\nx2 = {x2}"
        elif delta == 0:
            x = -b / (2 * a)
            return f"Discriminant = 0. One real solution:\nx = {x}"
        else:
            real = -b / (2 * a)
            imag = (abs(delta)**0.5) / (2 * a)
            return f"Discriminant < 0. Two complex solutions:\nx1 = {real} - {imag}i\nx2 = {real} + {imag}i"
    return f"Cannot solve polynomial of degree {degree}"
