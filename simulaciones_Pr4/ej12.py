import math
from random import random

# -------------------------------------------------------------------
# La función QueDevuelve(p1, p2) genera X ~ Geom(p1) e Y ~ Geom(p2)
# y devuelve M = min(X, Y). Se demuestra que:
#
#   P(M > n) = P(X > n) * P(Y > n) = (1-p1)^n * (1-p2)^n
#            = [(1-p1)(1-p2)]^n.
#
# Por lo tanto, M tiene distribución geométrica con parámetro
# p = 1 - (1-p1)(1-p2) = p1 + p2 - p1*p2.
#
# Para p1=0.05, p2=0.2 se obtiene p = 0.05 + 0.2 - 0.01 = 0.24.
# Así, QueDevuelve(0.05, 0.2) genera M ~ Geom(0.24).
# -------------------------------------------------------------------

def ejercicio12():
    u = random()
    p = 0.24
    return int(math.log(1 - u) / math.log(1 - p)) + 1