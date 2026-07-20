import random
import math

def var_muestral(xs):
    n = len(xs)
    m = sum(xs) / n
    return sum((x - m) ** 2 for x in xs) / (n - 1)

def bootstrap_var_s2(datos, B=10000):
    s2_obs = var_muestral(datos)
    s2_boot = []
    for _ in range(B):
        muestra = [random.choice(datos) for _ in range(len(datos))]
        s2_boot.append(var_muestral(muestra))
    media_boot = sum(s2_boot) / B
    var_boot = sum((s - media_boot) ** 2 for s in s2_boot) / (B - 1)
    return s2_obs, media_boot, var_boot

def ejercicio6():
    # a) n=2, X=[1,3]
    datos_a = [1, 3]
    s2, _, var_s2 = bootstrap_var_s2(datos_a)
    print(f"a) n=2, X={datos_a}")
    print(f"   S² observado = {s2:.4f}")
    print(f"   Var bootstrap de S² = {var_s2:.4f}")

    # b) n=15
    datos_b = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
    s2, _, var_s2 = bootstrap_var_s2(datos_b)
    print(f"\nb) n=15")
    print(f"   S² observado = {s2:.4f}")
    print(f"   Var bootstrap de S² = {var_s2:.4f}")

if __name__ == "__main__":
    ejercicio6()
