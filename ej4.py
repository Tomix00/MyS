import math

"""
a)
    Sea X_i el tiempo en ser atentida con distr. \mathcal{E}(\lambda_i) para i=1,2,3
    Sea C la caja que elige el cliente

    Se pregunta,
        P(X\lt 4) = P(X_1\lt 4 | C=1)\cdot P(C=1) + P(X_2\lt 4 | C=2)\cdot P(C=2) + P(X_3\lt 4 | C=3)\cdot P(C=3)
        P(X\lt 4) = F_1(4) \cdot 0.4 + F_2(4) \cdot 0.32 + F_3(5) \cdot 0.28
                  = [1-exp(-3\cdot 4)]0.4 + [1-exp(-4\cdot 4)] \cdot 0.32 + [1-exp(-5\cdot 4)] \cdot 0.28
                  = 
        
b)

    Se pregunta
        P(C=k | X\ge 4) = \frac{P(C=k , X\ge 4)}{P(X\ge 4)} # por bayes
                        = \frac{P(X\ge 4 , C=k)}{P(X\ge 4)}
                        = \frac{1 - P(X\lt 4 , C=k)}{P(X\ge 4)}
                        = \frac{1 - {}}{P(X\ge 4)}

"""



print((1-math.exp(-3* 4))*0.4 + (1-math.exp(-4* 4)) * 0.32 + (1-math.exp(-5* 4)) * 0.28)