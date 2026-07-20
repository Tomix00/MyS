import random
import math

datos = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
n = len(datos)
media = sum(datos) / n
a, b = -5, 5

def bootstrap_p(B=10000):
    count = 0
    for _ in range(B):
        muestra = [random.choice(datos) for _ in range(n)]
        media_boot = sum(muestra) / n
        if a < media_boot - media < b:
            count += 1
    return count / B

def ejercicio5():
    p_est = bootstrap_p()
    print(f"Datos: {datos}")
    print(f"Media muestral: {media:.2f}")
    print(f"P( -5 < media - mu < 5 ) estimado: {p_est:.4f}")

if __name__ == "__main__":
    ejercicio5()
