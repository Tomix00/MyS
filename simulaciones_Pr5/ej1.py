import math
from random import random

def ejercicio1a():
    U = random()
    if U < 0.25:
        return 2 + 2 * math.sqrt(U)
    else:
        return 6 - 2 * math.sqrt(3 * (1 - U))

def ejercicio1b():
    U = random()
    if U < 0.6:
        return -3 + math.sqrt(9 + 35 * U / 3)
    else:
        return ((35 * U -19) / 2) ** (1/3)

def ejercicio1c():
    U = random()
    if U < 1/16:
        return 0.25 * math.sqrt(16 * U)
    else:
        return 4 * U - 0.25