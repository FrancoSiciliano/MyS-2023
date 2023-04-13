import sys
sys.path.append('.\\utils')
sys.path.append('.\\metodos')
from metodos import AlgoritmoTrapecios

res = AlgoritmoTrapecios("sen(x)",1,10,10)
res.calcular()
res.graficar()
