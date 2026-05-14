from random import random
from transf_inversa import continousGenerators as cg

def generar_max():
    X1 = cg.exponentialL(1)
    X2 = cg.exponentialL(2)
    X3 = cg.exponentialL(3)
    return max(X1, X2, X3)

def generar_min():
    X1 = cg.exponentialL(1)
    X2 = cg.exponentialL(2)
    X3 = cg.exponentialL(3)
    return min(X1, X2, X3)

def simular():
    print(f"Muestra de M (máximo)")
    for _ in range(10):
        print(f"{generar_max():.4f}")

    print(f"\nMuestra de m (mínimo)")
    for _ in range(10):
        print(f"{generar_min():.4f}")

if __name__ == "__main__":
    simular()