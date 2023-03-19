def f(x):
    return eval(function_entry.get())
def rectangulos(a, b, n):
    h = (b-a)/n
    integral = 0
    for i in range(n):
        print(i)
        integral += f(a + i * h)

    return integral * h

