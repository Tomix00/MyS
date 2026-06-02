#from random import random
#import numpy as np
#
#def gen():
#    n = 1
#    sample = [np.random.normal(loc=0, scale=1, size=None)]
#    variance = 0
#    mean = sample[0]
#
#    while n <= 100 or np.sqrt(variance)/np.sqrt(n) >= 0.1:
#        n+=1
#        
#        xi = np.random.normal(size=None)
#        sample.append(xi)
#        new_mean = mean + (xi - mean)/(n+1)
#
#        variance = (1 - 1/n)*variance + (n+1)*(new_mean - mean)**2
#        mean = new_mean
#
#    return sample, variance, mean
#
#print(f"Tamaño de la muestra {len(gen()[0])},\n\
#        Varianza muestral: {gen()[1]},\n\
#        Media muestral: {gen()[2]} ----------- desviación: {gen()[1]**0.5}")

import numpy as np
import os

def ejercicio1_a(num_simulaciones=1000):
    np.random.seed(42)
    n_finales = []
    for _ in range(num_simulaciones):
        n = 0
        media = 0
        S2 = 0
        while True:
            x = np.random.normal(0, 1)
            n += 1
            if n == 1:
                media = x
                S2 = 0
            else:
                media_ant = media
                media = media_ant + (x - media_ant) / n
                if n == 2:
                    S2 = (x - media_ant)**2 / (n-1)
                else:
                    S2 = S2 * (1 - 1/(n-2)) + n * (media - media_ant)**2
            S = np.sqrt(S2) if n > 1 else 0
            if n >= 100 and S / np.sqrt(n) < 0.1:
                break
        n_finales.append(n)
    return np.mean(n_finales)

def ejercicio1_b():
    np.random.seed(42)
    n = 0
    media = 0
    S2 = 0
    while True:
        x = np.random.normal(0, 1)
        n += 1
        if n == 1:
            media = x
            S2 = 0
        else:
            media_ant = media
            media = media_ant + (x - media_ant) / n
            if n == 2:
                S2 = (x - media_ant)**2 / (n-1)
            else:
                S2 = S2 * (1 - 1/(n-2)) + n * (media - media_ant)**2
        S = np.sqrt(S2) if n > 1 else 0
        if n >= 100 and S / np.sqrt(n) < 0.1:
            break
    return n

def ejercicio1_c():
    np.random.seed(42)
    n = 0
    media = 0
    S2 = 0
    while True:
        x = np.random.normal(0, 1)
        n += 1
        if n == 1:
            media = x
            S2 = 0
        else:
            media_ant = media
            media = media_ant + (x - media_ant) / n
            if n == 2:
                S2 = (x - media_ant)**2 / (n-1)
            else:
                S2 = S2 * (1 - 1/(n-2)) + n * (media - media_ant)**2
        S = np.sqrt(S2) if n > 1 else 0
        if n >= 100 and S / np.sqrt(n) < 0.1:
            break
    return media

def ejercicio1_d():
    np.random.seed(42)
    n = 0
    media = 0
    S2 = 0
    while True:
        x = np.random.normal(0, 1)
        n += 1
        if n == 1:
            media = x
            S2 = 0
        else:
            media_ant = media
            media = media_ant + (x - media_ant) / n
            if n == 2:
                S2 = (x - media_ant)**2 / (n-1)
            else:
                S2 = S2 * (1 - 1/(n-2)) + n * (media - media_ant)**2
        S = np.sqrt(S2) if n > 1 else 0
        if n >= 100 and S / np.sqrt(n) < 0.1:
            break
    return S2

if __name__ == "__main__":
    os.system('clear')
    a = ejercicio1_a()
    b = ejercicio1_b()
    c = ejercicio1_c()
    d = ejercicio1_d()

    print(f"a) El nro de datos esperado es: {a}\n")
    print(f"b) El nro de datos generados efectivamente es: {b}\n")
    print(f"c) La media muestral es: {c}\n")
    print(f"d) La varianza muestral es: {d}\n")