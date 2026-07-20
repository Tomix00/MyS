import random
import math
import time

def metodo_ross(n):
    """Box-Muller"""
    muestras = []
    for _ in range(n // 2 + 1):
        u1 = random.random()
        u2 = random.random()
        r = math.sqrt(-2 * math.log(u1))
        theta = 2 * math.pi * u2
        muestras.append(r * math.cos(theta))
        muestras.append(r * math.sin(theta))
    return muestras[:n]

def metodo_polar(n):
    """Polar (Marsaglia)"""
    muestras = []
    while len(muestras) < n:
        v1 = 2 * random.random() - 1
        v2 = 2 * random.random() - 1
        w = v1 * v1 + v2 * v2
        if w <= 1:
            c = math.sqrt(-2 * math.log(w) / w)
            muestras.append(v1 * c)
            if len(muestras) < n:
                muestras.append(v2 * c)
    return muestras[:n]

def metodo_razon(n):
    """Razon entre uniformes (Kinderman-Monahan)"""
    muestras = []
    a = math.sqrt(2 / math.e)
    while len(muestras) < n:
        u = random.random()
        v = (2 * random.random() - 1) * a
        x = v / u
        if v * v <= -4 * u * u * math.log(u):
            muestras.append(x)
    return muestras[:n]

def ejercicio9():
    n = 10000
    for nombre, metodo in [("Ross (Box-Muller)", metodo_ross),
                            ("Polar", metodo_polar),
                            ("Razon uniformes", metodo_razon)]:
        inicio = time.time()
        muestras = metodo(n)
        tiempo = time.time() - inicio
        media = sum(muestras) / n
        var = sum((x - media) ** 2 for x in muestras) / n
        print(f"{nombre:20} | media={media:.4f} | var={var:.4f} | tiempo={tiempo:.4f}s")

if __name__ == "__main__":
    ejercicio9()
