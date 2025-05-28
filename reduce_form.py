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


def format_reduced_form(coeffs: dict) -> str:
    if not coeffs:
        return "Reduced form: 0 = 0"

    terms = []
    for exp in sorted(coeffs.keys(), reverse=True):
        coef = coeffs[exp]
        if coef == 0:
            continue

        sign = '+' if coef > 0 else '-'
        abs_coef = abs(coef)

        if exp == 0:
            term = f"{abs_coef}"
        elif exp == 1:
            term = f"{abs_coef} * x"
        else:
            term = f"{abs_coef} * x^{exp}"

        terms.append((sign, term))

    if not terms:
        return "Reduced form: 0 = 0"

    first_sign, first_term = terms[0]
    reduced = f"{'' if first_sign == '+' else '-'}{first_term}"

    for sign, term in terms[1:]:
        reduced += f" {sign} {term}"

    return f"Reduced form: {reduced} = 0"
