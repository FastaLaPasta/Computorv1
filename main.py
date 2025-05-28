import sys
from typing import Dict


def parse_equation(expression: str) -> Dict[int, float]:
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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 main.py "3 * x^2 + 2 * x^1 + 2 * x^0 = 1 * x^0"')
        sys.exit(1)

    equation = sys.argv[1]

    if "=" not in equation:
        print("Invalid input: no '=' found.")
        sys.exit(1)

    left, right = equation.split("=")
    left_side = parse_equation(left)
    right_side = parse_equation(right)

    print("Membre gauche :", left_side)
    print("Membre droit  :", right_side)
