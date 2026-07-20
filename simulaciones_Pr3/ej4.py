import sys
import numpy as np

def ejercicio4c(n: int):
    menor4 = 0
    mayor4_por_caja = [0, 0, 0]

    for _ in range(n):
        u = np.random.random()
        if u < (0.4):
            caja = 0 # Caja 1
            media = 3
        elif u < (0.4 + 0.35):
            caja = 1 # Caja 2
            media = 4
        else:
            caja = 2 # Caja 3
            media = 5
        tiempo_espera = np.random.exponential(scale=media)

        if tiempo_espera < 4:
            menor4 += 1
        else:
            mayor4_por_caja[caja] += 1

    total_mayor4 = sum(mayor4_por_caja)
    prob_menor4 = menor4 / n

    if total_mayor4 > 0:
        prob_mayor4_c1 = mayor4_por_caja[0] / total_mayor4
        prob_mayor4_c2 = mayor4_por_caja[1] / total_mayor4
        prob_mayor4_c3 = mayor4_por_caja[2] / total_mayor4
    else:
        prob_mayor4_c1 = prob_mayor4_c2 = prob_mayor4_c3 = 0
    
    print(f"P(T < 4) ≈ {prob_menor4:.4f}")
    print(f"P(C1 | T>4) ≈ {prob_mayor4_c1:.4f}")
    print(f"P(C2 | T>4) ≈ {prob_mayor4_c2:.4f}")
    print(f"P(C3 | T>4) ≈ {prob_mayor4_c3:.4f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ej4.py <iterations>")
        sys.exit(1)
    elif int(sys.argv[1]) <= 0:
        print("Iterations must be a positive integer.")
        sys.exit(1)
    
    iteraciones = int(sys.argv[1])    
    ejercicio4c(iteraciones)

