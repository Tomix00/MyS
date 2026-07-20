import random
import numpy as np
from scipy.stats import norm
from scipy.stats import binom

def parcial3():
    
    # ---------- 2-a, 2-b ----------
    datos = [27, 25, 80, 79, 61, 55, 31, 35, 60, 8, 87, 89, 41, 90, 96, 63]
    n = len(datos)

    datos_ordenados = sorted(datos)
    mediana_orig = (datos_ordenados[7] + datos_ordenados[8]) / 2

    def mediana_muestral(muestra):
        muestra_ord = sorted(muestra)
        return (muestra_ord[7] + muestra_ord[8]) / 2

    N = 5000
    replicas = []

    for _ in range(N):
        muestra_boot = random.choices(datos, k=n)
        theta_star = mediana_muestral(muestra_boot)
        replicas.append(theta_star)

    replicas = np.array(replicas)

    ecm_boot = np.mean((replicas - mediana_orig) ** 2)
    var_boot = np.var(replicas, ddof=1)

    print(f"2-a) ECM bootstrap (N={N}): {ecm_boot:.4f}\n")
    print(f"2-b) Varianza bootstrap (N={N}): {var_boot:.4f}\n")
    print("-" * 20)

    # ---------- 3-b ----------

    datos = np.array([
        491.455,
        496.387,
        491.175,
        502.551,
        509.838,
        491.708,
        501.39,
        496.717,
        494.769,
        503.901,
        502.351,
        503.617,
        501.754,
        497.783,
        501.019,
        501.494,
        502.689,
        501.762,
        509.541,
        504.808,
        507.551,
        498.701,
        501.114,
        504.87,
        506.344,
        511.543,
        496.488,
        498.155,
        501.201,
        507.446])

    n = len(datos)
    datos_ord = np.sort(datos)

    F0 = norm.cdf(datos_ord, loc=500, scale=5)

    j = np.arange(1, n+1)
    D_plus = np.max(j/n - F0)
    D_minus = np.max(F0 - (j-1)/n)
    D_obs = max(D_plus, D_minus)

    print(f"3-b) D_obs = {D_obs:.6f}\n")

    # ---------- 3-c ----------

    def ks_uniform(muestra):
        """Devuelve el estadístico D para una muestra uniforme (teórica U(0,1))."""
        n = len(muestra)
        u_ord = np.sort(muestra)
        j = np.arange(1, n+1)
        D_plus = np.max(j/n - u_ord)
        D_minus = np.max(u_ord - (j-1)/n)
        return max(D_plus, D_minus)

    M = 10000
    n = 30

    D_sim = np.zeros(M)
    for i in range(M):
        uniformes = np.random.uniform(0, 1, n)
        D_sim[i] = ks_uniform(uniformes)

    p_valor = np.mean(D_sim >= D_obs)
    print(f"3-c) p-valor simulado = {p_valor:.5f}\n")
    print("-" * 20)

    # ---------- 4-c ----------

    obs = np.array([25, 68, 70, 37])
    n_total = 200
    p_est = (0*25 + 1*68 + 2*70 + 3*37) / (n_total*3)  # 0.5316

    probs_est = [binom.pmf(k, 3, p_est) for k in range(4)]
    exp_est = n_total * np.array(probs_est)
    chi2_obs = np.sum((obs - exp_est)**2 / exp_est)

    M = 10000
    mayor = 0
    for _ in range(M):
        muestra = np.random.binomial(3, p_est, n_total)
        obs_sim = np.bincount(muestra, minlength=4)
        media_sim = np.mean(muestra)
        p_sim = media_sim / 3
        probs_sim = [binom.pmf(k, 3, p_sim) for k in range(4)]
        exp_sim = n_total * np.array(probs_sim)
        chi2_sim = np.sum((obs_sim - exp_sim)**2 / exp_sim)
        if chi2_sim >= chi2_obs:
            mayor += 1

    p_valor_sim = mayor / M
    print(f"4-c) p-valor simulado: {p_valor_sim:.5f}\n")


if __name__=="__main__":
    parcial3()