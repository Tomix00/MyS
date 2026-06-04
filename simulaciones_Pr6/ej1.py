import random
import math

def ejercicio_1():
    # parameters
    d = 0.1
    mu_teo = 0
    sigma_teo = 1

    # init (n = 1)
    n = 1
    x = random.gauss(mu_teo, sigma_teo)
    mean = x
    scuad = 0.0

    # simulation loop 
    while (n <= 100 or math.sqrt(scuad / n) >= d):
        n += 1
        x = random.gauss(mu_teo, sigma_teo)
        mean_ant = mean

        # update
        mean = mean_ant + (x - mean_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (mean - mean_ant)**2
    
    return n, mean, scuad


if __name__ == "__main__":
    n, mean, var = ejercicio_1()
    print(f"n: {n} \nmean: {mean} \nvar: {var}\n")