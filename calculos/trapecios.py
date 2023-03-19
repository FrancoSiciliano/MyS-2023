def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_k = a + i * h
        result += f(x_k)
    result *= h
    return result

def f(x):
    return

a = int(input("ingrese el limite inferior(desde):"))
b = int(input("ingrese el limete superior(hasta):"))
n = int(input("ingrese el numero de subintervalos"))
func_str = "x**2"
f = eval("lambda x: " + func_str)
integral = trapezoidal_rule(f, a, b, n)

print(f"La aproximación de la integral de f(x) en [{a}, {b}] con {n} subintervalos es: {integral}")