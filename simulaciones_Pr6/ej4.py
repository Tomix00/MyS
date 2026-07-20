import random
import math
from statistics import NormalDist

z = NormalDist().inv_cdf(0.975)

def estimate_p(target_se=0.01, min_n=100):
    n = 0
    mean = 0.0
    M2 = 0.0
    while True:
        n += 1
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        inside = 1.0 if x * x + y * y <= 1 else 0.0
        delta = inside - mean
        mean += delta / n
        M2 += delta * (inside - mean)
        if n >= min_n:
            var = M2 / (n - 1)
            se = math.sqrt(var / n)
            if se < target_se:
                break
    return n, mean, se

def ejercicio4():
    # a) SE(p_hat) < 0.01
    n, p_est, se_p = estimate_p(0.01)
    pi_est = 4 * p_est
    print(f"a) SE<0.01: n={n}, p_est={p_est:.4f}, pi={pi_est:.4f}")
    # b) IC 95% for pi with width < target_width
    for target_width in [0.1, 0.05, 0.001]:
        # width = 2 * z * SE(pi_hat) = 2 * z * 4 * SE(p_hat)
        # SE(p_hat) < target_width / (8 * z)
        target_se_p = target_width / (8 * z)
        n, p_est, se_p = estimate_p(target_se_p, min_n=100)
        pi_est = 4 * p_est
        se_pi = 4 * se_p
        ci = (pi_est - z * se_pi, pi_est + z * se_pi)
        actual_width = ci[1] - ci[0]
        print(f"b) ancho<{target_width}: n={n}, pi={pi_est:.4f}, IC=[{ci[0]:.4f},{ci[1]:.4f}] (ancho real={actual_width:.6f})")

if __name__ == "__main__":
    ejercicio4()
