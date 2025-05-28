import sys
from parse import parse_equation
from reduce_form import reduce_form, format_reduced_form
from get_degree import get_degree
from solve import solve


def main(equation: str):
    left, right = equation.split("=")
    left_side = parse_equation(left)
    right_side = parse_equation(right)
    reduce_equation = reduce_form(left_side, right_side)

    print(f"Reduced form: {format_reduced_form(reduce_equation)}")
    print(f"Polynomial degree: {get_degree(reduce_equation)}")
    print(solve(reduce_equation))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 main.py "3 * x^2 + 2 * x^1 + 2 * x^0 = 1 * x^0"')
        sys.exit(1)

    equation = sys.argv[1]
    if "=" not in equation:
        print("Invalid input: no '=' found.")
        sys.exit(1)
    main(equation)
