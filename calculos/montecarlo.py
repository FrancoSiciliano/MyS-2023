import numpy
from sympy import sympify, lambdify, symbols, exp
import matplotlib.pyplot as plt


class Algoritmo_montecarlo:
    def __init__(self, f_x, a, b, n):
        aux = f_x.replace("sec", "1/cos")
        aux = aux.replace("e", str(exp(1)))
        x = symbols('x')
        expr = sympify(aux)
        self.f = lambdify(x, expr, 'numpy')
        self.a = a
        self.b = b
        self.n = n
        self.ptos_pos = []
        self.ptos_neg = []
        self.ptos_nul = []

    def calcular(self):
        puntos_dentro = 0

        punto_max = -numpy.inf
        punto_min = numpy.inf
        h = self.b - self.a

        for i in numpy.arange(self.a, self.b + 0.5, 0.5):
            x = i
            res = self.f(x)
            if res > punto_max:
                punto_max = res
            if res < punto_min:
                punto_min = res

        if punto_min < 0:
            m = punto_max - punto_min
        else:
            m = punto_max

        for i in range(0, self.n):
            coord_x = numpy.random.uniform(self.a, self.b)
            min_val = 0

            if punto_min < 0:
                min_val = punto_min

            coord_y = numpy.random.uniform(min_val, punto_max)
            x = coord_x
            y = self.f(x)

            if 0 <= coord_y < y:
                puntos_dentro += 1
                self.ptos_pos.append((coord_x, coord_y))
            elif 0 > coord_y > y:
                puntos_dentro -= 1
                self.ptos_neg.append((coord_x, coord_y))
            else:
                self.ptos_nul.append((coord_x, coord_y))

        resultado = (puntos_dentro / self.n) * m * h

        return resultado

    def graficar(self):
        x_vals = numpy.linspace(self.a, self.b, 1000)
        y_vals = self.f(x_vals)
        plt.plot(x_vals, y_vals, label='f(x)')

        plt.fill_between(x_vals, y_vals, interpolate=True, color='lightblue')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Integración por Monte Carlo')

        if len(self.ptos_pos) > 0:
            x_plot, y_plot = zip(*self.ptos_pos)
            plt.scatter(x_plot, y_plot, label="positivos", c="green")

        if len(self.ptos_neg) > 0:
            x_plot, y_plot = zip(*self.ptos_neg)
            plt.scatter(x_plot, y_plot, label="negativos", c="red")

        if len(self.ptos_nul) > 0:
            x_plot, y_plot = zip(*self.ptos_nul)
            plt.scatter(x_plot, y_plot, label="nulos", c="blue")

        plt.legend(loc='upper right')
        plt.show()


test = Algoritmo_montecarlo("sin(x)", 1, 5, 500000)
print(test.calcular())
test.graficar()
