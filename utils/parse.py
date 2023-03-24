from sympy import sympify, lambdify, symbols, exp


def parse_local(f_x):
    math_local = {"sen": "sin", "sec": "1/cos", "e": str(exp(1))}

    aux = f_x
    for elem in math_local.keys():
        aux = aux.replace(elem, math_local[elem])

    x = symbols('x')
    expr = sympify(aux)

    return lambdify(x, expr, 'numpy')
