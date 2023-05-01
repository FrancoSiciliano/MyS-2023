import numpy as np
import matplotlib.pyplot as plt

from utils.parse import parse_local as pl

class AlgoritmoTrapecios:

    def __init__(self, f_x, a, b, n):
        self.f = pl(f_x)
        self.a = a
        self.b = b
        self.n = n
        self.Coordenadas_trapcios = []
        self.resultado = 0

    def calcular(self):
        h = (self.b - self.a) / self.n
        result = 0.5 * (self.f(self.a) + self.f(self.b))
        self.Coordenadas_trapcios.append((self.a, self.f(self.a)))
        for i in range(1, self.n):
            x_k = self.a + i * h
            result += self.f(x_k)
            self.Coordenadas_trapcios.append((x_k, self.f(x_k)))
        self.Coordenadas_trapcios.append((self.b, self.f(self.b)))
        result *= h
        self.resultado = result
        return result

    def graficar(self):

        plt.title('Integración por método de los trapecios')
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = self.f(x_vals)

        plt.close(None)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x_vals, y_vals, label='f(x)')
        for i in range(self.n):
            x_trap = [self.Coordenadas_trapcios[i][0], self.Coordenadas_trapcios[i+1][0]]
            y_trap = [self.Coordenadas_trapcios[i][1], self.Coordenadas_trapcios[i+1][1]]
            plt.fill_between(x_trap, y_trap, alpha=0.3)

        plt.title(f'Integración por método de los trapecios')
        plt.annotate(f"Resultado: {self.resultado:.2f}", (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
        plt.show()