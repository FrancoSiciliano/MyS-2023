import matplotlib.pyplot as plt
from utils.parse import parse_local_t as pt


class AlgoritmoEuler:

    def __init__(self, f_x, x0, b, n):
        self.f = pt(f_x)
        self.x0 = x0
        self.b = b
        self.n = n
        self.ptos_calculados = [(0, x0)]

    def calcular(self):
        h = (self.b / self.n)
        for i in range(1, self.n + 1):
            coord_t_ant, coord_x_ant = self.ptos_calculados[i - 1]
            x_n = coord_x_ant + (h * self.f(coord_x_ant, coord_t_ant))
            self.ptos_calculados.append((i * h, x_n))
        return self.ptos_calculados[-1][1]

    def graficar(self):
        plt.close(None)

        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.title('PVI - Euler')

        x_plot, y_plot = zip(*self.ptos_calculados)
        plt.scatter(x_plot, y_plot, label="puntos calculados", c="red")
        plt.plot(x_plot, y_plot, c="green")

        plt.legend(loc="best")

        plt.show()

    def punto(self, t):
        if 0 <= t <= len(self.ptos_calculados):
            return self.ptos_calculados[t][1]
