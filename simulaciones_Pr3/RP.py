from sympy.ntheory.residue_ntheory import primitive_root
import sys

# Dependencies:
# pip install sympy
#
# Example usage:
# RP.py 17
if __name__ == "__main__":
    p = int(sys.argv[1]) # prime number passed as command line argument
    g = primitive_root(p, smallest=False)
    print(f"Una raíz primitiva módulo {p} es: {g}")