import sys
sys.path.append('.\\utils')
sys.path.append('.\\metodos')
from metodos import AlgoritmoEuler

res = AlgoritmoEuler("e^t/x^t", 0, 10, 20)
res.calcular()
res.graficar()
