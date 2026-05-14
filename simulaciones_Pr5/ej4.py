from random import random
from transf_inversa import continousGenerators as cg

def generar_X():
    Y = cg.exponential1()
    
    U = random()
    X = U ** (1 / Y)
    return X
