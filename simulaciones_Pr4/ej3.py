from random import random
import math
from transf_inversa import discreteGenerators as dg

def roll_dice_sum():
    dado1 = dg.udiscrete1n(6)
    dado2 = dg.udiscrete1n(6)
    return dado1 + dado2

def simulate_game():
    vistas = set()
    lanzamientos = 0
    while(len(vistas)<11):
        suma = roll_dice_sum()
        vistas.add(suma)
        lanzamientos += 1
    return lanzamientos

def ejercicio3(repeticiones):
    resultados = []
    for _ in range(repeticiones):
        resultados.append(simulate_game())

    media = sum(resultados) / repeticiones
    varianza = sum((x-media)**2 for x in resultados) / repeticiones
    desviacion = varianza ** 0.5

    p_ge_15 = sum(1 for x in resultados if x>=15) / repeticiones
    p_le_9 = sum(1 for x in resultados if x<=9)/ repeticiones

    return media, desviacion, p_ge_15, p_le_9

if __name__ == "__main__":
    repeticiones_lista = [100, 1000, 10000, 100000]
    
    print("Resultados de la simulación:\n")
    print(f"{'Reps':>8} | {'Media':>8} | {'Desvío':>8} | {'P(N>=15)':>10} | {'P(N<=9)':>10}")
    print("-" * 58)
    
    for reps in repeticiones_lista:
        media, desvio, prob_ge15, prob_le9 = ejercicio3(reps)
        print(f"{reps:8d} | {media:8.2f} | {desvio:8.2f} | {prob_ge15:10.4f} | {prob_le9:10.4f}")
