import numpy
from sympy import sympify, lambdify, symbols, exp


def montecarlo(f_x, a, b, n):
    f_x = f_x.replace("sec", "1/cos")
    f_x = f_x.replace("e", str(exp(1)))
    x = symbols('x')
    expr = sympify(f_x)
    f = lambdify(x, expr, 'numpy')

    puntos_dentro = 0
    punto_max = -numpy.inf
    punto_min = numpy.inf
    h = b - a

    for i in range(a, b + 1):
        x = i
        res = f(x)
        if res > punto_max:
            punto_max = res
        if res < punto_min:
            punto_min = res

    m = punto_max - punto_min

    for i in range(0, n):
        coord_x = numpy.random.uniform(a, b)
        coord_y = numpy.random.uniform(punto_min, punto_max)
        x = coord_x
        y = f(x)

        if 0 <= coord_y < y:
            puntos_dentro += 1
        elif 0 > coord_y > y:
            puntos_dentro -= 1

    resultado = (puntos_dentro / n) * m * h

    return resultado
