import numpy
import matplotlib.pyplot as plt
from utils.parse import parse_local as pl


class AlgoritmoMontecarlo:

    def __init__(self, f_x, a, b, n):
        self.f = pl(f_x)
        self.a = a
        self.b = b
        self.n = n
        self.ptos_pos = []
        self.ptos_neg = []
        self.ptos_nul = []
        self.resultado = 0

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

        self.resultado = (puntos_dentro / self.n) * m * h

        return self.resultado

    def graficar(self):
        x_vals = numpy.linspace(self.a, self.b, 1000)
        y_vals = self.f(x_vals)
        plt.close(None)
        plt.plot(x_vals, y_vals, label='f(x)')

        plt.fill_between(x_vals, y_vals, interpolate=True, color='lightblue')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Integración por Monte Carlo')

        cant_pos = len(self.ptos_pos)
        cant_neg = len(self.ptos_neg)
        cant_nul = len(self.ptos_nul)

        if cant_pos > 0:
            x_plot, y_plot = zip(*self.ptos_pos)
            plt.scatter(x_plot, y_plot, label=f"positivos = {cant_pos}", c="green")

        if cant_neg > 0:
            x_plot, y_plot = zip(*self.ptos_neg)
            plt.scatter(x_plot, y_plot, label=f"negativos = {cant_neg}", c="red")

        if cant_nul > 0:
            x_plot, y_plot = zip(*self.ptos_nul)
            plt.scatter(x_plot, y_plot, label=f"nulos = {cant_nul}", c="blue")

        plt.legend(loc='upper right')
        plt.annotate(f"Resultado: {self.resultado:.2f}", (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.show()
