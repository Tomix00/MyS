# MyS

Este repositorio contiene las resoluciones de los ejercicios practicos con sus
respectivos algoritmos para las simulaciones, a su vez que algunas herramientas
para facilitar las mismas.

## Tools


```generators.py```

Este archivo contiene
- generador congruencial lineal mixto [seed, a ,c, M]
- generador congruencial lineal multiplicativo [seed, a, M]
- generador congruencial combinado (mixto + multiplicativo) [seed, a ,c, M]
- generador middle-square (von Neumann) [seed]
- generador RANDU [seed]
- generador Park-Miller (RANDU2) [seed]

\* Aclaracion para el uso del generador combiando, los valores por entrada
son usados por los generadores mixto y multiplicativo, es decir si se ingresa
c en 0, el generador mixto se transforma en uno multiplicativo y no se
garantiza que tenga maximo periodo.

---

```graphics.py```

Este archivo grafica los valores generados de la forma (x_i, x_i+1), de los 
generadores mixto, multiplicativo y combinado, recibiendo por entrada,

- semilla
- a (constante multiplicativa)
- c (constante a sumar)
- M (valor de modulo)
- iteraciones 

---

```RP.py```

Este archivo encuentra la raiz primitiva mas grande de un numero, del caso que
no tenga, devuelve NONE.