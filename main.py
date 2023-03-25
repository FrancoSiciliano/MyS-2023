import sys
sys.path.append('.\\utils')
sys.path.append('.\\metodos')
from metodos import AlgoritmoEulerMejorado, AlgoritmoEuler

res = AlgoritmoEulerMejorado("x + t", 0, 5, 10)
print(res.calcular())
res.graficar()

res = AlgoritmoEuler("x + t", 0, 5, 10)
res.calcular()
res.graficar()