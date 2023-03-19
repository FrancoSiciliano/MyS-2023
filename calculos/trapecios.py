from Tools.scripts.nm2def import symbols
import numpy
from sympy import sympify, lambdify, symbols, exp

def trapecios(f_x, a, b, n):
    f_x = f_x.replace("sec", "1/cos")
    f_x = f_x.replace("e", str(exp(1)))
    x = symbols('x')
    expr = sympify(f_x)
    f = lambdify(x, expr, 'numpy')
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_k = a + i * h
        result += f(x_k)
    result *= h
    return result


a = int(input("ingrese el limite inferior(desde):"))
b = int(input("ingrese el limete superior(hasta):"))
n = int(input("ingrese el numero de subintervalos"))
f = str(input("ingrese la funcion: "))

integral = trapecios(f, a, b, n)

print(f"La aproximación de la integral de f(x) en [{a}, {b}] con {n} subintervalos es: {integral}")