# MyS

Modeling and Simulation (*Modelado y Simulación*) — practical exercises in Monte Carlo methods, pseudorandom number generation, inverse transform sampling, acceptance-rejection, and sequential estimation.

## Structure

```
simulaciones_Pr3/      PRNG generators (LCG, middle-square, RANDU, Park-Miller) + basic exercises
simulaciones_Pr4/      Discrete inverse transform method + permutations
simulaciones_Pr5/      Continuous inverse transform + acceptance-rejection + composition
simulaciones_Pr6/      Sequential estimation + Monte Carlo integration with stopping rules
parcial1/              Exam 1 (intact — evaluation deliverable)
parcial2/              Exam 2 (intact — evaluation deliverable)
Practicos_Resueltos/   Exercise statements in Obsidian markdown
conceptos/            Theory PDFs (9 chapters, cap1–cap9)
```

## Tools

Each `simulaciones_Pr*` folder is self-contained with its own copies of shared utilities.

- **`generators.py`** — PRNG class with methods: `genMul`, `genMix`, `genComb_sum`, `vonNeumann`, `randu`, `randu2`
- **`graphics.py`** — CLI scatter-plot generator for congruential PRNGs. Usage: `python graphics.py <seed> <a> <c> <M> <iterations>`
- **`RP.py`** — CLI primitive root finder. Usage: `python RP.py <prime>`
- **`transf_inversa.py`** — Classes `discreteGenerators` (uniform, geometric, Bernoulli, Poisson, binomial), `continousGenerators` (exponential, gamma), and `permutation` (Fisher-Yates shuffle)

## Running

Each `ej*.py` is a standalone script:

```
python simulaciones_Pr3/ej1.py <seed> <n_points>
python simulaciones_Pr4/ej2.py
python simulaciones_Pr5/ej8.py
python simulaciones_Pr6/ej1.py
```

## Installation

```
pip install -r requirements.txt
```

Requires Python 3.12+. External dependencies: `matplotlib`, `numpy`, `sympy`.
