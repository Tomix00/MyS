from generators import generators as Generators
import sys


def estimate_percentage_in_sphere(seed: int, n_points: int, m: int = 2**31) -> float:
    """
    Estima el porcentaje de puntos (u1,u2,u3), (u4,u5,u6), ...
    que caen dentro de la esfera de centro (M/2,M/2,M/2)
    y radio M/10 en el cubo [0,M)^3.
    """
    x = seed
    center = m / 2.0
    radius2 = (m / 10.0) ** 2
    inside = 0

    for _ in range(n_points):
        x = Generators.randu(x)
        u1 = x
        x = Generators.randu(x)
        u2 = x
        x = Generators.randu(x)
        u3 = x

        d2 = (u1 - center) ** 2 + (u2 - center) ** 2 + (u3 - center) ** 2
        if d2 <= radius2:
            inside += 1

    return 100.0 * inside / n_points

def epis_2(seed: int, n_points: int, m:int = 2**31) -> float:
    """
    Estima el porcentaje de puntos (u1,u2,u3), (u4,u5,u6), ...
    que caen dentro de la esfera de centro (M/2,M/2,M/2)
    y radio M/10 en el cubo [0,M)^3 utilizando el generador von Neumann.
    """
    x = seed
    center = m / 2.0
    radius2 = (m / 10.0) ** 2
    inside = 0

    for _ in range(n_points):
        x = Generators.randu2(x)
        u1 = x
        x = Generators.randu2(x)
        u2 = x
        x = Generators.randu2(x)
        u3 = x

        d2 = (u1 - center) ** 2 + (u2 - center) ** 2 + (u3 - center) ** 2
        if d2 <= radius2:
            inside += 1

    return 100.0 * inside / n_points

def main():
    seed = int(sys.argv[1])
    n_points = int(sys.argv[2])
    if(len(sys.argv) != 3):
        print("Usage: python ej1d.py <seed> <n_points>")
        sys.exit(1)
    elif(seed <= 0 or n_points <= 0):
        print("Seed and number of points must be positive integers.")
        sys.exit(1)

    percentage = estimate_percentage_in_sphere(seed=seed, n_points=n_points)
    print(f"Using RANDU generator:")
    print(f"Puntos simulados: {n_points}")
    print(f"Porcentaje estimado dentro de la esfera: {percentage:.6f}%")

    percentage2 = epis_2(seed=seed, n_points=n_points)
    print(f"Using RANDU2 generator:")
    print(f"Puntos simulados: {n_points}")
    print(f"Porcentaje estimado dentro de la esfera: {percentage2:.6f}%")


if __name__ == "__main__":
    main()
