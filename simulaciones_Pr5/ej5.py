from random import random
from transf_inversa import continousGenerators as cg

def generate_max():
    X1 = cg.exponentialL(1)
    X2 = cg.exponentialL(2)
    X3 = cg.exponentialL(3)
    return max(X1, X2, X3)

def generate_min():
    X1 = cg.exponentialL(1)
    X2 = cg.exponentialL(2)
    X3 = cg.exponentialL(3)
    return min(X1, X2, X3)

def ejercicio5():
    print(f"Muestra de M (máximo)")
    for _ in range(10):
        print(f"{generate_max():.4f}")

    print(f"\nMuestra de m (mínimo)")
    for _ in range(10):
        print(f"{generate_min():.4f}")

if __name__ == "__main__":
    ejercicio5()