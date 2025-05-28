import sys
from parser import parse_equation


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
