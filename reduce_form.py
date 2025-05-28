from typing import Dict


def reduce_form(left: dict, right: dict) -> Dict[int, float]:
    for power, coef in right.items():
        if power in left:
            left[power] -= coef
        else:
            left[power] = -coef
    return left
