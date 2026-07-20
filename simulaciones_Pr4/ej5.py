import random
import time
import math
from transf_inversa import discreteGenerators as dg

# Parámetros
n = 10
p = 0.3

# ========== MÉTODO I: Transformada inversa ==========
def binomial_inverse(n, p):
    """Usa discreteGenerators.binomial de la clase"""
    return dg.binomial(n, p)

# ========== MÉTODO II: Simulación de n ensayos Bernoulli ==========
def binomial_trials(n, p):
    """Simula n ensayos Bernoulli y cuenta éxitos"""
    exitos = 0
    for _ in range(n):
        if dg.bernoulli(p) == 1:
            exitos += 1
    return exitos

# ========== a) Comparación de eficiencia ==========
def ejercicio5a(n_simulaciones=10000):
    print(f"\n{'='*65}")
    print(f"a) Comparación para Bin({n}, {p}) con {n_simulaciones}\
           simulaciones")
    print(f"{'='*65}\n")
    
    # Método I: Transformada inversa
    inicio = time.time()
    muestras_inv = [binomial_inverse(n, p) for _ in range(n_simulaciones)]
    tiempo_inv = time.time() - inicio
    
    # Método II: n ensayos Bernoulli
    inicio = time.time()
    muestras_ens = [binomial_trials(n, p) for _ in range(n_simulaciones)]
    tiempo_ens = time.time() - inicio
    
    print(f"{'Método':<35} | {'Tiempo (s)':>10}")
    print("-" * 50)
    print(f"{'I - Transformada inversa':<35} | {tiempo_inv:10.4f}")
    print(f"{'II - n ensayos Bernoulli':<35} | {tiempo_ens:10.4f}")
    
    # Eficiencia relativa
    if tiempo_inv < tiempo_ens:
        print(f"\nTransformada inversa es {tiempo_ens/tiempo_inv:.2f}x\
              más rápida")
    else:
        print(f"\nn ensayos Bernoulli es {tiempo_inv/tiempo_ens:.2f}x\
              más rápido")
    
    return muestras_inv, muestras_ens

# ========== b) Análisis de resultados ==========
def analyze_samples(muestras, metodo_nombre):
    """Calcula el valor con mayor ocurrencia y proporciones de 0 y 10"""
    frecuencias = [0] * (n + 1)
    for x in muestras:
        frecuencias[x] += 1
    
    total = len(muestras)
    proporciones = [f/total for f in frecuencias]
    
    # Valor con mayor ocurrencia (moda)
    moda = max(range(n + 1), key=lambda i: frecuencias[i])
    prob_moda = proporciones[moda]
    
    # Proporciones de 0 y 10
    prob_0 = proporciones[0]
    prob_10 = proporciones[10]
    
    print(f"\n{metodo_nombre}")
    print(f"  Valor con mayor ocurrencia: {moda} (prob observada:\
           {prob_moda:.4f})")
    print(f"  Proporción de X=0: {prob_0:.6f}")
    print(f"  Proporción de X=10: {prob_10:.6f}")
    
    return moda, prob_moda, prob_0, prob_10

# ========== c) Valores teóricos de la Binomial ==========
def theoretical_probability(k, n, p):
    """Calcula P(X=k) para Bin(n,p)"""
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

def show_theoretical():
    print(f"\n{'='*65}")
    print("c) Valores teóricos de Bin(10, 0.3)")
    print(f"{'='*65}")
    
    # Valor más probable (moda)
    moda_teorica = int((n + 1) * p)
    prob_moda_teorica = theoretical_probability(moda_teorica, n, p)
    prob_0_teorica = theoretical_probability(0, n, p)
    prob_10_teorica = theoretical_probability(10, n, p)
    
    print(f"Valor con mayor ocurrencia (moda): {moda_teorica}")
    print(f"  Probabilidad teórica: {prob_moda_teorica:.4f}")
    print(f"P(X=0) teórica: {prob_0_teorica:.6f} = (0.7)^10 = {0.7**10:.6f}")
    print(f"P(X=10) teórica: {prob_10_teorica:.8f} = (0.3)^10 = {0.3**10:.8f}")
    
    return moda_teorica, prob_moda_teorica, prob_0_teorica, prob_10_teorica

# ========== COMPARACIÓN CON TEÓRICOS ==========
def compare_with_theoretical(muestras_inv, muestras_ens):
    moda_teo, prob_moda_teo, prob_0_teo, prob_10_teo = show_theoretical()
    
    # Calcular frecuencias observadas
    freqs_inv = [muestras_inv.count(i)/len(muestras_inv) for i in range(n+1)]
    freqs_ens = [muestras_ens.count(i)/len(muestras_ens) for i in range(n+1)]
    
    print(f"\n{'='*65}")
    print("Diferencias entre observado y teórico:")
    print(f"{'='*65}")
    
    print(f"\nMétodo I (Transformada inversa):")
    print(f"  Diferencia en moda:\
           {abs(freqs_inv[moda_teo] - prob_moda_teo):.6f}")
    print(f"  Diferencia en P(X=0): {abs(freqs_inv[0] - prob_0_teo):.6f}")
    print(f"  Diferencia en P(X=10): {abs(freqs_inv[10] - prob_10_teo):.8f}")
    
    print(f"\nMétodo II (n ensayos Bernoulli):")
    print(f"  Diferencia en moda:\
           {abs(freqs_ens[moda_teo] - prob_moda_teo):.6f}")
    print(f"  Diferencia en P(X=0): {abs(freqs_ens[0] - prob_0_teo):.6f}")
    print(f"  Diferencia en P(X=10): {abs(freqs_ens[10] - prob_10_teo):.8f}")

# ========== EJECUCIÓN PRINCIPAL ==========
if __name__ == "__main__":
    # Parte a: Comparar eficiencia
    muestras_inv, muestras_ens = ejercicio5a(10000)
    
    # Parte b: Analizar resultados
    print(f"\n{'='*65}")
    print("b) Resultados observados")
    print(f"{'='*65}")
    
    analyze_samples(muestras_inv, "Método I - Transformada inversa:")
    analyze_samples(muestras_ens, "Método II - n ensayos Bernoulli:")
    
    # Parte c: Comparar con teóricos
    compare_with_theoretical(muestras_inv, muestras_ens)