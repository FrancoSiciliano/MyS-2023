from sympy import sympify, lambdify, symbols, exp

def rectangulos(f_x, a, b, n):
    f_x = f_x.replace("sec", "1/cos")
    f_x = f_x.replace("e", str(exp(1)))
    x = symbols('x')
    expr = sympify(f_x)
    f = lambdify(x, expr, 'numpy')

    h = (b-a)/n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)

    return integral * h

