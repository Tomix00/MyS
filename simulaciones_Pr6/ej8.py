import random
import math

def lambda_t(t):
    """8h cycle: 4→14→4"""
    t_mod = t % 8
    if t_mod <= 4:
        return 4 + (14 - 4) * t_mod / 4
    else:
        return 14 - (14 - 4) * (t_mod - 4) / 4

LAMBDA_MAX = 14
MU_ADM = 15
MU_DIAG = 12
T_OPEN = 16

def simulate_once():
    t = 0.0
    queue_adm = 0
    queue_diag = 0
    adm_busy = False
    diag_busy = False
    n_patients = 0
    total_time = 0.0
    next_arrival = -math.log(random.random()) / LAMBDA_MAX
    next_adm_end = float('inf')
    next_diag_end = float('inf')

    while t < T_OPEN or queue_adm > 0 or queue_diag > 0 or adm_busy or diag_busy:
        next_event = min(next_arrival if t < T_OPEN else float('inf'),
                         next_adm_end, next_diag_end)

        if next_event == next_arrival:
            t = next_arrival
            queue_adm += 1
            if t < T_OPEN:
                next_arrival = t - math.log(random.random()) / LAMBDA_MAX
            if not adm_busy:
                next_adm_end = t - math.log(random.random()) / MU_ADM
                adm_busy = True
                queue_adm -= 1

        elif next_event == next_adm_end:
            t = next_adm_end
            adm_busy = False
            # pasa a diagnostico
            queue_diag += 1
            if not diag_busy:
                next_diag_end = t - math.log(random.random()) / MU_DIAG
                diag_busy = True
                queue_diag -= 1
            if queue_adm > 0:
                next_adm_end = t - math.log(random.random()) / MU_ADM
                adm_busy = True
                queue_adm -= 1

        else:
            t = next_diag_end
            diag_busy = False
            n_patients += 1
            total_time += t  # tiempo de salida
            if queue_diag > 0:
                next_diag_end = t - math.log(random.random()) / MU_DIAG
                diag_busy = True
                queue_diag -= 1

    remaining = queue_adm + queue_diag
    return n_patients, total_time, remaining, t

def ejercicio8():
    n = 0
    s_avg_time = 0.0
    s2_avg_time = 0.0
    s_remaining = 0.0
    s2_remaining = 0.0
    s_extra_time = 0.0
    s2_extra_time = 0.0
    min_reps = 100

    while True:
        n += 1
        count, total_t, rem, finish_t = simulate_once()
        avg_time = total_t / count if count > 0 else 0
        extra = finish_t - T_OPEN if finish_t > T_OPEN else 0

        # Update streams for 3 estimators
        for val, s, s2 in [(avg_time, 's_avg_time', 's2_avg_time'),
                           (rem > 0, 's_remaining', 's2_remaining'),
                           (extra, 's_extra_time', 's2_extra_time')]:
            pass

        s_avg_time += avg_time
        s2_avg_time += avg_time * avg_time
        s_remaining += (1.0 if rem > 0 else 0.0)
        s2_remaining += (1.0 if rem > 0 else 0.0)
        s_extra_time += extra
        s2_extra_time += extra * extra

        if n >= min_reps:
            for s, s2 in [(s_avg_time, s2_avg_time),
                          (s_remaining, s2_remaining),
                          (s_extra_time, s2_extra_time)]:
                pass
            se_avg = math.sqrt(max((s2_avg_time / n - (s_avg_time / n) ** 2) / n, 0))
            se_rem = math.sqrt(max((s2_remaining / n - (s_remaining / n) ** 2) / n, 0))
            se_extra = math.sqrt(max((s2_extra_time / n - (s_extra_time / n) ** 2) / n, 0))
            if all(s < 0.01 for s in [se_avg, se_rem, se_extra]):
                break

    mean_avg = s_avg_time / n
    mean_rem = s_remaining / n
    mean_extra = s_extra_time / n
    z = 1.96

    print(f"b) Tiempo promedio en sistema: {mean_avg:.4f} IC95=[{mean_avg-z*se_avg:.4f},{mean_avg+z*se_avg:.4f}] (n={n})")
    print(f"c) P(quedan pacientes): {mean_rem:.4f} IC95=[{mean_rem-z*se_rem:.4f},{mean_rem+z*se_rem:.4f}]")
    print(f"d) Tiempo extra esperado: {mean_extra:.4f} IC95=[{mean_extra-z*se_extra:.4f},{mean_extra+z*se_extra:.4f}]")

if __name__ == "__main__":
    ejercicio8()
