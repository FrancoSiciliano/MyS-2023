import matplotlib.pyplot as plt
import numpy as np

from utils.parse import parse_local


class AlgoritmoRectangulos:
    def __init__(self, f_x, a, b, n):
        self.f = parse_local(f_x)
        self.a = a
        self.b = b
        self.n = n

    def calcular_graficar(self):
        h = (self.b - self.a) / self.n
        integral = 0

        # Obtener valores mínimo y máximo de la función en el intervalo
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = self.f(x_vals)
        ymin, ymax = min(y_vals), max(y_vals)

        # Ajustar límites de la gráfica
        plt.xlim(self.a - h, self.b + h)
        plt.ylim(ymin - 0.1 * abs(ymin), ymax + 0.1 * abs(ymax))

        # Establecer valor máximo de altura de rectángulos
        max_height = ymax

        # Gráfico de la función
        plt.plot(x_vals, y_vals)
        plt.fill_between(x_vals, 0, y_vals, alpha=0.2)

        for i in range(self.n):
            result = self.f(self.a + i * h)
            integral += result
            plt.bar(self.a + i * h, result, h, alpha=0.2, edgecolor='black', linewidth=1, align='edge')

        # Mostrar gráfico y resultado de la integral
        plt.show()
        return integral * h


res = AlgoritmoRectangulos('sin(x)*e**x', 0, 100, 50)
res.calcular_graficar()
