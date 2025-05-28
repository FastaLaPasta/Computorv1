from typing import Dict


def parse_equation(expression: str) -> Dict[int, float]:
    """
    expression: str, A string representation of an equation.
    return: dict, Dict of power/coef for each part of the equation.

    return a dictionnary within the different parts of the equation.
    """
    expr = expression.replace(" ", "").replace("X", "x").replace("-", "+-")
    if expr.startswith('+'):
        expr = expr[1:]

    terms = [t for t in expr.split('+') if t]
    coeffs = {}

    for term in terms:
        term = term.replace('*', '')

        if 'x^' in term:
            # Term x^
            parts = term.split('x^')
            coeff = float(parts[0]) if parts[0] not in ['', '-'] else (1 if parts[0] != '-' else -1)
            exp = int(parts[1])
        elif 'x' in term:
            # Terme x
            coeff_str = term.replace('x', '')
            coeff = float(coeff_str) if coeff_str not in ['', '-'] else (1 if coeff_str != '-' else -1)
            exp = 1
        else:
            # Terme constant
            coeff = float(term)
            exp = 0

        coeffs[exp] = coeffs.get(exp, 0) + coeff

    return coeffs
