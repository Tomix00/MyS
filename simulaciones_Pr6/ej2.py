import numpy as np
import os

def ejercicio2_i_a():
    np.random.seed(42)
    n = 0
    suma = 0.0
    suma_cuad = 0.0
    while True:
        u = np.random.uniform(0, 1)
        f = np.exp(u) / np.sqrt(2 * u)
        n += 1
        suma += f
        suma_cuad += f * f
        estimador = suma / n
        var_estimador = (suma_cuad / n - estimador**2) / n
        if n >= 100 and np.sqrt(var_estimador) < 0.01:
            break
    return estimador

def ejercicio2_ii_a():
    np.random.seed(42)
    n = 0
    suma_x2 = 0.0
    suma_x2_cuad = 0.0
    while True:
        x = np.random.normal(0, 1/np.sqrt(2))
        x2 = x * x
        n += 1
        suma_x2 += x2
        suma_x2_cuad += x2 * x2
        estimador_x2 = suma_x2 / n
        var_estimador_x2 = (suma_x2_cuad / n - estimador_x2**2) / n
        if n >= 100 and np.sqrt(var_estimador_x2) < 0.01:
            break
    integral = np.sqrt(np.pi) * estimador_x2
    return integral

if __name__ == "__main__":
    os.system('clear')
    a = ejercicio2_i_a()
    b = ejercicio2_ii_a()

    print(f"a-i) Valor estaimdo: {a}\n")
    print(f"a-ii) Valor estimado: {b}\n")