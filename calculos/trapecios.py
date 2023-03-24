import numpy as np
from Tools.scripts.nm2def import symbols
import numpy
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, symbols, exp

from utils.parse import parse_local as pl

class Algoritmo_trapecios:

    def __init__(self, f_x, a, b, n):
        self.f = pl(f_x)
        self.a = a
        self.b = b
        self.n = n
        self.Coordenadas_trapcios = []

    def trapecios(self):
        h = (self.b - self.a) / self.n
        result = 0.5 * (self.f(self.a) + self.f(self.b))
        self.Coordenadas_trapcios.append((self.a, self.f(self.a)))
        for i in range(1, self.n):
            x_k = self.a + i * h
            result += self.f(x_k)
            self.Coordenadas_trapcios.append((x_k, self.f(x_k)))
        self.Coordenadas_trapcios.append((self.b, self.f(self.b)))
        result *= h
        return result

    def graficar(self):
        x_vals = np.linspace(self.a, self.b, 1000)
        y_vals = self.f(x_vals)
        plt.plot(x_vals, y_vals, label='f(x)')
        for i in range(self.n):
            x_trap = [self.Coordenadas_trapcios[i][0], self.Coordenadas_trapcios[i+1][0]]
            y_trap = [self.Coordenadas_trapcios[i][1], self.Coordenadas_trapcios[i+1][1]]
            plt.fill_between(x_trap, y_trap, alpha=0.3)
        plt.show()

f_x = str(input("Ingrese la función: "))
a = int(input("Ingrese el límite inferior (desde): "))
b = int(input("Ingrese el límite superior (hasta): "))
n = int(input("Ingrese el número de subintervalos: "))

integral = Algoritmo_trapecios(f_x,a,b,n)

print(f"La aproximación de la integral de f(x) en [{a}, {b}] con {n} subintervalos es: {integral.trapecios()}")

integral.graficar()