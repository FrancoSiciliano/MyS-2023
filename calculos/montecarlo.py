import numpy
from sympy import sympify, lambdify, symbols, exp
import matplotlib.pyplot as plt


def montecarlo(f_x, a, b, n):
    f_x = f_x.replace("sec", "1/cos")
    f_x = f_x.replace("e", str(exp(1)))
    x = symbols('x')
    expr = sympify(f_x)
    f = lambdify(x, expr, 'numpy')

    puntos_dentro = 0

    positivos = []
    negativos = []
    nulos = []

    punto_max = -numpy.inf
    punto_min = numpy.inf
    h = b - a

    for i in numpy.arange(a, b + 0.5, 0.5):
        x = i
        res = f(x)
        if res > punto_max:
            punto_max = res
        if res < punto_min:
            punto_min = res

    if punto_min < 0:
        m = punto_max - punto_min
    else:
        m = punto_max

    x_vals = numpy.linspace(a, b, 1000)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')

    plt.fill_between(x_vals, y_vals, interpolate=True, color='lightblue')

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Integración por Monte Carlo')

    # Show the plot

    for i in range(0, n):
        coord_x = numpy.random.uniform(a, b)
        min_val = 0

        if punto_min < 0:
            min_val = punto_min

        coord_y = numpy.random.uniform(min_val, punto_max)
        x = coord_x
        y = f(x)

        if 0 <= coord_y < y:
            puntos_dentro += 1
            positivos.append((coord_x, coord_y))
        elif 0 > coord_y > y:
            puntos_dentro -= 1
            negativos.append((coord_x, coord_y))
        else:
            nulos.append((coord_x, coord_y))

    if len(positivos) > 0:
        x_plot, y_plot = zip(*positivos)
        plt.scatter(x_plot, y_plot, label="positivos", c="green")

    if len(negativos) > 0:
        x_plot, y_plot = zip(*negativos)
        plt.scatter(x_plot, y_plot, label="negativos", c="red")

    if len(nulos) > 0:
        x_plot, y_plot = zip(*nulos)
        plt.scatter(x_plot, y_plot, label="nulos", c="blue")

    plt.legend(loc='upper right')
    resultado = (puntos_dentro / n) * m * h
    plt.show()

    return resultado



res = montecarlo("sin(x)", 1, 5, 500)
print(res)
