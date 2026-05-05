from random import random
import math
from transf_inversa import discreteGenerators as dg

def generar_suma():
    dado1 = dg.udiscretemk(1,6)
    dado2 = dg.udiscretemk(1,6)
    return dado1 + dado2

def simular():
    vistas = set()
    lanzamientos = 0
    while(len(vistas)<11):
        suma = generar_suma()
        vistas.add(suma)
        lanzamientos += 1
    return lanzamientos

def estimar(repeticiones):
    resultados = []
    for _ in range(repeticiones):
        resultados.append(simular())

    media = sum(resultados) / repeticiones
    varianza = sum((x-media)**2 for x in resultados) / repeticiones
    desviacion = varianza ** 0.5

    p_ge_15 = sum(1 for x in resultados if x>=15) / repeticiones
    p_le_9 = sum(1 for x in resultados if x<=9)/ repeticiones

    return media, desviacion, p_ge_15, p_le_9

print("100 repeticinoes:", estimar(100))
print("1.000 repeticiones:", estimar(1000))
print("10.000 repeticiones:", estimar(10000))
print("100.000 repeticiones:", estimar(100000))
