___
<u>Índice:</u>
^indice

1. [[#^ejercicio1|Ejercicio 1 - Resuelto]]
2. [[#^ejercicio2|Ejercicio 2 - Resuelto]]
3. [[#^ejercicio3|Ejercicio 3 - Resuelto]]
4. [[#^ejercicio4|Ejercicio 4 - Resuelto]]
5. [[#^ejercicio5|Ejercicio 5 - Resuelto]]
6. [[#^ejercicio6|Ejercicio 6 - Resuelto]]
7. [[#^ejercicio7|Ejercicio 7 - Resuelto]]
8. [[#^ejercicio8|Ejercicio 8 - Resuelto]]
9. [[#^ejercicio9|Ejercicio 9 - Resuelto]]
10. [[#^ejercicio10|Ejercicio 10 - Resuelto]]
11. [[#^ejercicio11|Ejercicio 11 - Resuelto]]
12. [[#^ejercicio12|Ejercicio 12 - Resuelto]]
13. [[#^ejercicio13|Ejercicio 13 - Resuelto]]
14. [[#^ejercicio14|Ejercicio 14 - Resuelto]]
15. [[#^ejercicio15|Ejercicio 15 - Resuelto]]
16. [[#^ejercicio16|Ejercicio 16 - Resuelto]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Considerar un proceso de Poisson en el cual los eventos ocurren con intensidad de $0,3$ por hora. ¿Cuál es la probabilidad de que ningún evento ocurra entre las 10 de la mañana y las 2 de la tarde?

<u>Solución:</u>

Sea $N(t)$ el proceso de Poisson que cuenta la cantidad de eventos para un $t$ en horas con intensidad $\lambda=0,3$, es decir $N(0)=0$ por definición, $N(t)=\lambda\cdot t$. Notar que dado que $t$ se mide en horas, $10am \implies t=10$ y $2pm \implies t=14$.
Se pregunta, $$P(N(14)-N(10)=0)=P(N(4)=0)=\frac{(0,3\cdot 4)^{0}}{0!}e^{\Large-(0,3\cdot 4)}=e^{\Large-(0,3\cdot 4)}\approx 0,3011$$


___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Los desperfectos que se producen en un cable submarino siguen un proceso de Poisson con intensidad $\lambda=0,1$ por kilometro.
- a) ¿Cuál es la probabilidad de que no se produzcan desperfectos en los primeros dos kilómetros?
- b) Sabiendo que no hay desperfectos en los primeros kilómetros, ¿Cuál es la probabilidad de que no haya tampoco desperfectos en el tercer kilómetro?

<u>Solución:</u>

Sea $N(t)$ el proceso de Poisson que cuenta la cantidad de desperfectos con respecto a un $t$ en kilómetros y con intensidad $\lambda=0,1$.
- a) Se pregunta $$P(N(2)=0)=e^{\Large-(0,1\cdot 2)}\approx 0,8187$$
- b) Por la propiedad de incrementos independientes, el evento "no desperfectos en $[0,2]$" es independiente de lo que ocurra en el intervalo $[2,3]$. Además por la propiedad de estacionariedad, la distribución en el tercer kilometro es la misma que cualquier otro kilometro. Entonces $$\begin{align}P(N(3)-N(2)=0 \,|\, N(2)=0)=&\,\frac{P(N(3)-N(2)=0 , N(2)=0)}{P(N(2)=0)} \\=&\, \frac{P(N(3)-N(2)=0 )\cdot P( N(2)=0)}{P(N(2)=0)} \\=&\, P(N(3)-N(2)=0) \\=&\, P(N(1)=0) \\=&\,e^{\large -(0,1\cdot 1)}\\\approx&\, 0,9048 \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Cierta oficina pública mantiene registros del número de personas que van a realizar un determinado trámite durante la mañana (de $8$ a $13$ hs). Estos registros muestran que, en promedio, llegan 15 personas por hora, y que el número de personas que arriba constituye un proceso de Poisson homogéneo.
- a) ¿Cuál es la probabilidad de que lleguen más de 20 personas en la última hora de atención?
- b) ¿Cuál es la probabilidad de que durante la mañana lleguen exactamente $100$ personas, sabiendo que desde las $9$hs hasta las $12$hs llegaron $80$?

<u>Solución:</u>

Sea $N(t)$ el proceso de Poisson que cuenta el numero de personas para un $t$ en horas y intensidad $\lambda=15$. Notar que entre $8:00$ y $13:00$ hay $5$hs en total.
- a) Dado que la ultima hora de atención es de $12:00$ a $13:00$, hay $1$hr. Se pregunta $$P(N(1)\gt 20)=1-P(N(1)\le 20)=1-\sum_{k=0}^{20} \frac{e^{\large -15}\cdot 15^k}{k!}\approx 1-0,917 = 0,083$$
- b) Se pregunta $$\begin{align}P(N(5)=100 \,|\, N(4)-N(1)=80)=&\,P(N(5)=100 \,|\, N(3)=80)\\ =&\,\frac{P(N(5)=100 , N(3)=80)}{P(N(3)=80)} \\ =&\,\frac{P(N(5)-N(3)=100-80 , N(3)=80)}{P(N(3)=80)}\\=&\,\frac{P(N(2)=20 , N(3)=80)}{P(N(3)=80)}\\=&\, \frac{P(N(2)=20 )\cdot P( N(3)=80)}{P(N(3)=80)} \\=&\,P(N(2)=20)\\=&\,\frac{e^{\large-(15\cdot 2)}(15\cdot 2)^{20}}{20!}\\ \approx& \,0.0085 \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> En una empresa electrónica se observa que el número de componentes que fallan en un período de tiempo $t$ corresponde a un proceso Poisson. Además, se sabe que ocurren aproximadamente ocho fallos antes de cumplir $100$ horas de funcionamiento.
- a) ¿Cuál es la probabilidad de que un componente falle en $25$ horas?.
- b) ¿y que fallen no más de dos componentes en $50$ horas?
- c) ¿Cuál es la probabilidad de que fallen por lo menos diez componentes en $125$ horas?

<u>Solución:</u>

Sea $N(t)$ el proceso de Poisson que cuenta la cantidad de componentes que falla, con respecto a un tiempo $t$ y intensidad $\lambda = {\large\frac{8}{100}}=0,08$
- a) Se pregunta $$P(N(25)=1) = \frac{e^{\large-(0,08\cdot25)}(0,08\cdot25)^{1}}{1!}\approx 0,2706$$
- b) Se pregunta $$P(N(50)\le 2) = \sum_{k=0}^{2} P(N(50)=k) = \sum_{k=0}^{2}\frac{e^{\large-(0,08\cdot 50)}(0,08\cdot 50)^k}{k!}\approx 0,2381$$
- c) Se pregunta $$P(N(125)\ge 10)=1-P(N(125)\le9)=1-\sum_{k=0}^{9}\frac{e^{\large-(0,08\cdot 125)}(0,08\cdot 125)^k}{k!}\approx 1-0,4579 \approx 0,5421$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u>  Para un proceso Poisson con intensidad $\lambda$, determinar $P(N(s) = k \,|\, N(t) = n)$, considerando dos casos:
- a) $s < t$
- b) $s > t$

<u>Solución:</u>

- a) Se pregunta $$\begin{align} P(N(s) = k \,|\, N(t) = n) =&\, \frac{P(N(s) = k ,N(t) = n)}{P(N(t)=n)} \\=&\, \frac{P(N(s) = k )\cdot P(N(t)-N(s) = n-k)}{P(N(t)=n)} \end{align}$$Por estacionariedad, $N(t)-N(s)\sim Poisson(\lambda(t-s))$, $$P(N(s) = k \,|\, N(t) = n) = \frac{1}{\large\frac{e^{\Large-\lambda t}(\lambda t)^n}{n!}} \cdot \frac{e^{\large -\lambda s}(\lambda s)^k}{k!} \cdot \frac{e^{\large -\lambda(t-s)}(\lambda(t-s))^{n-k}}{(n-k)!}$$Simplificando $e^{-\lambda s}\cdot e^{-\lambda(t-s)}=e^{-\lambda t}$, queda: $$\begin{align}=&\,\frac{(\lambda s)^k (\lambda(t-s))^{n-k}}{k!(n-k)!} \cdot \frac{n!}{(\lambda t)^n} \\=&\, \frac{n!}{k!(n-k)!}\cdot \frac{s^k(t-s)^{n-k}}{t^n} \\ P(N(s)=k\,|\, N(t)=n)=&\, \binom{n}{k}\left(\frac{s}{t}\right)^k \left(1-\frac{s}{t}\right)^{n-k} \qquad, 0\le k\le n \end{align}$$
- b) Se pregunta $$\begin{align} P(N(s)=k \,|\, N(t)=n) =&\, \frac{P(N(s)=k \,,\, N(t)=n)}{P(N(t)=n)}\\=&\, \frac{P(N(s)-N(t)=k-n \,,\, N(t)=n)}{P(N(t)=n)}\\=&\, \frac{P(N(s)-N(t)=k-n)\cdot P(N(t)=n)}{P(N(t)=n)}\\=&\, P(N(s)-N(t)=k-n)  \end{align}$$ Por estacionariedad $N(s)-N(t) \sim Poisson(\lambda(t-s))$ y teniendo en cuenta que si $k\lt n$ la probabilidad es $0$, $$P(N(s)=k \,|\, N(t)=n) = P(N(s)-N(t)=k-n) = \begin{cases}\large \frac{e^{\large-\lambda(s-t)}(\lambda(s-t))^{k-n}}{(k-n)!}&, k\ge n \\ 0&, k\lt n \end{cases}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Los clientes llegan a un banco de acuerdo a un proceso de Poisson con intensidad constante $\lambda$ (dada en horas). En la primera hora han llegado dos clientes. ¿Cuál es la probabilidad de que:
- a) ambos hayan llegado en los primeros $20$ minutos?,
- b) al menos uno de ellos haya llegado en los primeros $20$ minutos?

<u>Solución:</u>

Sea $N(t)$ el Proceso de Poisson que cuenta la cantidad de clientes que llegan al banco con respecto a un tiempo $t$ en horas e intensidad $\lambda$.
Notar que si $t=1hs=60min$
Se sabe que $N(1)=2$

- a) Por la propiedad de condicional del ejercicio anterior en el caso de $s\lt t$, tenemos $$P(N(s)=k\,|\, N(t)=n)=\binom{n}{k}\left(\frac{s}{t}\right)^k \left(1-\frac{s}{t}\right)^{n-k}$$ donde $s=1/3,\quad t=1,\quad n=k=2$, $$\begin{align} P(N(1/3)=2\,|\, N(1)=2)=\,&\binom{2}{2}\left(\frac{1/3}{1}\right)^2 \left(1-\frac{1/3}{1}\right)^{2-2} \\=\,& 1\left(\frac{1}{3}\right)^2 1 \\=\,& \frac{1}{9} \end{align}$$
- b) Se pregunta, $$\begin{align} P(N(1/3)\ge 1\,|\, N(1)=2)=\,& 1-P(N(1/3)\lt 1\,|\, N(1)=2) \\=\,& 1-P(N(1/3)=0\,|\, N(1)=2) \\=\,& 1-\left[ \binom{2}{0}\left(\frac{1/3}{1}\right)^0 \left(1-\frac{1/3}{1}\right)^{2} \right] \\=\,& 1- \left(1-\frac{1/3}{1}\right)^{2} \\=\,& 1-\frac{4}{9} \\=\,& \frac{5}{9} \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Un barrabrava de Talleres quiere llegar al Kempes desde Parque Don Bosco cruzando la circunvalación. Los autos pasan de acuerdo con un proceso de Poisson de intensidad $\lambda = 3$ por minuto. Si cruza corriendo la ruta sin mirar si vienen autos
- a) ¿Cuál es la probabilidad de que salga ileso si tarda $s$ segundos en cruzarla? Asuma que si está sobre la ruta cuando pasa un auto, entonces saldrá herido. Calcular para $s = 2, 5, 10$ y $20$.
- b) ¿Cuál es la probabilidad de que salga ileso si cuando cruza la ruta y pasa un auto tiene un $80\%$ de probabilidades de ser atropellado ?

<u>Solución:</u>

Sea $N(s)$ el Proceso de Poisson que cuenta la cantidad de autos que pasan con respecto a un tiempo $s$ en minutos y intensidad $\lambda = \frac{3}{60}=0.05$.

- a) Se pregunta $$\begin{align}&P(N(s)=0)= e^{\large-\lambda s}=e^{\large -0.05s} \\ \\ &s=2 \rightarrow e^{\large -0.05\cdot 2} \approx 0.9048 \\& s=5 \rightarrow e^{\large -0.05\cdot 5}\approx 0.7788 \\& s=10 \rightarrow e^{\large -0.05\cdot 10}\approx 0.6065 \\& s=20 \rightarrow e^{\large -0.05\cdot 5}\approx 0.3678 \end{align}$$
- b) Utilizando la regla de adelgazamiento, tenemos el Proceso de Poisson $H(s)$ que cuenta el numero de autos que atropellan con intensidad $\lambda p$ con $\lambda=0.05$ y $p=0.8$, ahora se pregunta $$P(H(s)=0) = e^{\large-0.05\cdot 0.8 \cdot s} = e^{\large -0.04\cdot s}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Suponer que, en el Ejercicio anterior, el barrabrava es lo suficientemente ágil para esquivar un auto, pero si se encuentra con dos o más autos mientras intenta cruzar, entonces sale herido.
- a) ¿Cuál es la probabilidad que salga ileso si le toma s segundos cruzar la ruta? Calcular para $s= 5, 10, 20$ y $30$.
- b) Si el primer auto aparece a los $s1$ segundos,
	- i) ¿Cuál es la probabilidad de que haya $2$ autos en $s$ segundos, con $s > s1$?.
	- ii) ¿Cuál es la probabilidad de que el hincha salga ileso en este caso? Calcular para $s = 10, 20$ y $30$ y $s1 = 5$.

<u>Solución:</u>

Tenemos el Proceso de Poisson $N(t)$ con $\lambda = 0.05$.
Sabemos que sale herido si $N(s)\ge 2$, y similarmente ileso si $N(s)\le 1$

- a) Se pregunta $$\begin{align} P(N(s)\le 1)=\,& P(N(s)=0) + P(N(s)=1) \\=\,& e^{-\large \lambda s} + e^{-\large\lambda s}(\lambda s) \\=\,& e^{-\large\lambda s}(1+\lambda s) \end{align}$$ con $\lambda=0.05$. $$\begin{align}& s=5 \rightarrow e^{-\large 0.05\cdot 5}(1+0.05\cdot 5) \approx 0.9735 \\& s=10 \rightarrow e^{-\large 0.05\cdot 10}(1+0.05\cdot 10) \approx 0.9097 \\& s=20 \rightarrow e^{-\large 0.05\cdot 20}(1+0.05\cdot 20) \approx 0.7357 \\& s=30 \rightarrow e^{-\large 0.05\cdot 30}(1+0.05\cdot 30) \approx 0.5578 \end{align}$$
- b) 
	- i) Se pregunta $$\begin{align} P(N(s)=2\,|\,N(s1)=1)=\,& \frac{P(N(s)=2\,,\,N(s1)=1)}{P(N(s1)=1)} \\=\,& \frac{P(N(s)-N(s1)=2-1\,,\,N(s1)=1)}{P(N(s1)=1)} \\=\,& \frac{P(N(s-s1)=1)\cdot(N(s1)=1)}{P(N(s1)=1)} \\=\,& P(N(s-s1)=1) \\=\,& e^{\large -0.05(s-s1)}(0.05(s-s1)) \end{align}$$
	- ii) Se pregunta $$\begin{align} P(N(s)=1\,|\, N(s1)=1) =\,& \frac{P(N(s)=1\,,\, N(s1)=1)}{P(N(s1)=1)} \\=\,& \frac{P(N(s)-N(s1)=1-1\,,\, N(s1)=1)}{P(N(s1)=1)} \\=\,& \frac{P(N(s-s1)=0)\cdot( N(s1)=1)}{P(N(s1)=1)} \\=\,& P(N(s-s1)=0 \\=\,& e^{\large -0.05(s-s1)} \end{align}$$ Calculando con $s1=5$ $$\begin{align}& s=10 \rightarrow e^{\large -0.05(10-5)} \approx 0.7788 \\& s=20 \rightarrow e^{\large -0.05(20-5)} \approx 0.4723 \\& s=30 \rightarrow e^{\large -0.05(30-5)} \approx 0.2865 \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Luke, Obi Wan y Yoda están al frente de tres colas separadas en la cafetería esperando a ser atendidos. Los clientes son atendidos en las tres colas de acuerdo a procesos de Poisson independientes con parámetros respectivos de $1, 2$ y $3$ minutos.
- a) Hallar la probabilidad de que Yoda sea atendido primero.
- b) Hallar la probabilidad de que Obi Wan sea atendido antes que Yoda.
- c) Hallar el tiempo de espera esperado para la primera persona atendida.

<u>Solución:</u>

Sean $X_L, X_O$ y $X_Y$ los tiempos de atención para Luke, Obi Wan y Yoda respectivamente. Cada uno de ellos siguen una distribución exponencial con parámetro $\lambda$ igual a la tasa de atención. Tenemos que $$\begin{align}& X_L \sim \mathcal{E}(\lambda_L = 1/1) \\& X_O\sim \mathcal{E}(\lambda_O = 1/2) \\& X_Y \sim \mathcal{E}(\lambda_Y = 1/3) \end{align}$$
- a) Se pregunta $$\begin{align}P(X_Y = min\{X_L,X_O,X_Y\}) =\,& \frac{\lambda_Y}{\lambda_L+\lambda_O+\lambda_Y} \\=\,& \frac{1/3}{1+1/2+1/3} \\=\,& \frac{2}{11}\end{align}$$
- b) Se pregunta $$\begin{align} P(X_O\lt X_Y) =\,& \frac{\lambda_O}{\lambda_O+\lambda_Y} \\=\,& \frac{1/2}{1/2+1/3}\\=\,& \frac{3}{5} \end{align}$$
- c) Sabiendo que $min[X_L,X_O,X_Y] \sim \mathcal{E}(\lambda_L+\lambda_O+\lambda_Y)$ se pregunta $$\begin{align}E[min[X_L,X_O,X_Y]] =\,& \frac{1}{\lambda_L+\lambda_O+\lambda_Y} \\=\,& \frac{1}{1+1/2+1/3} \\=\,& \frac{6}{11} \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u> A partir de las $6$ de la mañana, los autos, colectivos y motos llegan a un peaje de autopista según procesos de Poisson independientes. Los autos llegan aproximadamente una vez cada $5$ minutos. Los colectivos llegan aproximadamente una vez cada $10$ minutos. Las motos llegan aproximadamente una vez cada $30$ minutos.
- a) Hallar la probabilidad de que en los primeros $20$ minutos lleguen a la cabina exactamente tres vehículos: dos autos y una moto.
- b) En el peaje, la probabilidad de que un conductor tenga el cambio exacto es de $1/4$, independientemente del vehículo. Encontrar la probabilidad de que ningún vehículo tenga el cambio exacto en los primeros $10$ minutos.

<u>Solución:</u>

Sean los Procesos de Poisson
$N_A(t)$ aquel que cuenta la cantidad de autos que pasan con intensidad $\lambda =1/5$,
$N_C(t)$ aquel que cuenta la cantidad de colectivos que pasan con intensidad $\lambda = 1/10$ y
$N_M(t)$ aquel que cuenta la cantidad de motos que pasan con intensidad $\lambda = 1/30$.
Todos los Procesos son independientes.

- a) Se pregunta $$\begin{align}& P(N_A(20)=2,N_C(20)=0,N_M(20)=1)\\ \\=\,& P(N_A(20)=2)\cdot P(N_C(20)=0)\cdot P(N_M(20)=1) \\=\,& \left[ e^{\large 1/5 \cdot 20 }\frac{(1/5 \cdot 20)^2}{2!} \right]\cdot \left[ e^{\large 1/10 \cdot 20 }\frac{(1/10\cdot 20)^0}{0!} \right]\cdot \left[ e^{\large 1/30\cdot 20 }\frac{(1/30\cdot 20)^1}{1!} \right] \\=\,& (8e^{-4})\cdot(e^{-2})\cdot(e^{-2/3}\frac{2}{3}) \\=\,& e^{-20/3}\frac{16}{3} \end{align}$$
- b) Sea el Proceso de Poisson $N(t)=N_A(t)+N_C(t)+N_M(t)$ que cuenta la cantidad de vehículos que pasan independientemente del tipo de vehículo. Este tiene intensidad $\lambda=\lambda_A+\lambda_C+\lambda_M = 1/3$. Por la propiedad de adelgazamiento podemos filtrar aquellos vehículos que tengan cambio exacto, obteniendo así el Proceso de Poisson $N_{cambio}(t)$ con intensidad $\lambda_{cambio}=1/3\cdot 1/4=1/12$. Se pregunta $$P(N_{cambio}(10)=0)=e^{\large -1/12\cdot 10}=e^{\large -5/6}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 11</u> ([[#^indice|Índice]])
^ejercicio11

<u>Enunciado:</u> Se tienen dos procesos de Poisson independientes, $N_1(t)$ y $N_2(t),$ con $t \ge 0$, y tasas $\lambda_1 = 1$ y $\lambda_2 = 2$, respectivamente. Sea $N(t)$ la superposición de estos procesos: $N(t) = N_1(t) + N_2(t)$, $t \ge 0$.
- a) Calcular la probabilidad de que $N(1) = 2$ y $N(2) = 5$.
- b) Calcular la probabilidad de que $N_1(1) = 1$ dado que $N(1) = 2$.
- c) Calcular la probabilidad de que el segundo arribo en $N_1(t)$ ocurra antes que el tercer arribo en $N_2(t)$.

<u>Solución:</u>

- a) Se pregunta $$\begin{align} P(N(1)=2\,,\,N(2)=5) =\,& P(N(1)=2\,,\,N(2)-N(1)=5-2) \\=\,& P(N(1)=2\,,\,N(1)=3) \\=\,& P(N(1)=2)\cdot P(N(1)=3) \\=\,& \left[ e^{-3}\frac{(3)^2}{2!} \right]\cdot \left[ e^{-3}\frac{(3)^3}{3!} \right] \\=\,& e^{-6}\frac{81}{4} \end{align}$$
- b) Se pregunta $$\begin{align} P(N_1(1)=1 \,|\, N(1)=2) =\,& \frac{P(N_1(1)=1 \,,\, N(1)=2)}{P(N(1)=2)} \\=\,& \frac{P(N_1(1)=1 \,,\, N(1)-N_1(1)=2-1)}{P(N(1)=2)} \\=\,& \frac{P(N_1(1)=1 \,,\, N_2(1)=1)}{P(N(1)=2)} \\=\,& \frac{P(N_1(1)=1)\cdot P(N_2(1)=1)}{P(N(1)=2)} \\=\,& \frac{1}{\large e^{-3}\frac{3^2}{2!}}\cdot \left[ \left( e^{-1} \right)\cdot \left( e^{-2}\cdot 2 \right) \right] \\=\,& \frac{4}{9} \end{align}$$
- c) Sea $T_1^{(k)}$ el tiempo del k-esimo arribo en el proceso $N_1(t)$ y sea $T_2^{(m)}$ el tiempo del m-esimo arribo en el proceso $N_2(t)$. Se sabe que $T_1^{(2)} \sim Gamma(2,\lambda_1)$ y $T_2^{(3)} \sim Gamma(3,\lambda_2)$. Por independencia de $N_1$ y $N_2$, $T_1^{(2)}$ y $T_2^{(3)}$ son independientes. Se pregunta $$\begin{align} P(T_1^{(2)} \lt T_2^{(3)}) =\,& \int_0^{\infty} {P(T_1^{(2)}\lt t \,|\, T_2^{(3)}=t) \cdot f_{T_2^{(3)}}(t)} \,dt \\=\,& \int_0^{\infty} {P(T_1^{(2)}\lt t) \cdot f_{T_2^{(3)}}(t)} \,dt \\=\,& \int_0^{\infty} {\left[ \int_0^t {f_{T_1^{(2)}}(u)} \,du \right] \cdot f_{T_2^{(3)}}(t)} \,dt \\=\,& \int_0^{\infty} {\left[ \int_0^t {ue^{-u}} \,du \right] \cdot f_{T_2^{(3)}}(t)} \,dt \\=\,& \int_0^{\infty} {\left[ 1-e^{-t}(t+1) \right] \cdot f_{T_2^{(3)}}(t)} \,dt \\=\,& \int_0^{\infty} {\left[ 1-e^{-t}(t+1) \right] \cdot 4t^2 e^{-2t}} \,dt \\=\,& 4\left[\int_0^{\infty} {t^2 e^{-2t}} \,dt\right] - 4\left[\int_0^{\infty} {t^2(t+1)e^{-3t}} \,dt\right] \\=\,& 4\left[\frac{1}{4}\right] - 4\left[\frac{4}{27}\right] \\=\,& 1-\frac{16}{27} \\=\,& \frac{11}{27} \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 12</u> ([[#^indice|Índice]])
^ejercicio12

<u>Enunciado:</u> Supongamos que a la caja de un supermercado llegan dos tipos de clientes. Los que pagan en efectivo y los que pagan con tarjeta. Los que pagan con tarjeta llegan de acuerdo a un proceso de Poisson $N_1(t)$ con tasa de llegada de $3$ clientes por minuto, y los que pagan en efectivo llegan de acuerdo a un proceso de Poisson con tasa de llegada de $4$ clientes por minuto, y ambos procesos son independientes.
Calcular las probabilidades de los siguientes eventos:
- a) El primer cliente que llega a la caja pague en efectivo.
- b) Hayan llegado al menos $3$ clientes que pagan en efectivo antes del $5to$ cliente que paga con tarjeta.
- c) Hayan llegado exactamente $20$ clientes en los primeros $4$ minutos.

<u>Solución:</u>

Se tienen los Procesos de Poisson, $N_1(t)$ aquel que cuenta la cantidad de clientes con tarjeta con intensidad $\lambda=3$ y $N_2(t)$ aquel que cuenta la cantidad de clientes con efectivo con intensidad $\lambda=4.$
- a) Sea $T_1$ y $T_2$ los tiempos de arribo de los clientes con respecto a los procesos $N_1$ y $N_2$ respectivamente. Se sabe que $T_1\sim \mathcal{E}(\lambda_1)$ y $T_2\sim\mathcal{E}(\lambda_2)$. Se pregunta $$P(T_2\lt T_1)=\frac{\lambda_2}{\lambda_1+\lambda_2}=\frac{4}{3+4}=\frac{4}{7}$$
- b) El evento significa: cuando ocurre el $5to$ cliente con tarjeta, el número de efectivos que han ocurrido hasta ese momento es $\ge 3$. Tenemos que  $p_1 = 3/7$ y $p_2=4/7$. Sea la variable aleatoria $X$ = número de efectivos que ocurren antes del $5to$ tarjeta. $X\sim BN(r=5,p=3/7)$. Se pregunta $$\begin{align} P(X\ge 3) =\,& 1-P(X\le 2) \\=\,& 1-[P(X=0)+P(X=1)+P(X=2)] \\=\,& 1-\left[ \sum_{k=0}^2 \binom{k+4}{4}\left(\frac{3}{7}\right)^5\left(\frac{4}{7}\right)^k \right] \\\approx\,& 0.8734 \end{align}$$
- c) Sea el Proceso de Poisson $N(t)=N_1(t)+N_2(t)$ que cuenta la cantidad de clientes, con intensidad $\lambda = 3+4 = 7$. Se pregunta $$P(N(4)=20)=e^{\large -7\cdot 4}\frac{(7\cdot 4)^{20}}{20!}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 13</u> ([[#^indice|Índice]])
^ejercicio13

<u>Enunciado:</u>  En una intersección con mucho tráfico los accidentes se producen según un proceso de Poisson a un ritmo de dos accidentes por semana. En tres de cada cuatro accidentes está implicado el consumo de alcohol.
- a) ¿Cuál es la probabilidad de que la próxima semana se produzcan tres accidentes en los que esté implicado el alcohol?
- b) ¿Cuál es la probabilidad de que mañana se produzca al menos un accidente?
- c) Si se producen seis accidentes en febrero (cuatro semanas), ¿Cuál es la probabilidad de que en menos de la mitad de ellos esté implicado el alcohol?

<u>Solución:</u>

Sea el Proceso de Poisson $N(t)$ el cual cuenta la cantidad de accidentes con intensidad $\lambda=2$ por semana. Tenemos que la probabilidad de que el accidente sea por alcohol es $p=3/4$.

- a) Sea $N_A(t)$ el Proceso de Poisson que cuenta la cantidad de accidentes por alcohol con intensidad $\lambda_A=2\cdot 3/4 = 3/2$. Se pregunta $$P(N_A(1)=3)=e^{\large -3/2 \cdot 1}\frac{(3/2 \cdot 1)^3}{3!}=e^{\large -3/2}\frac{9}{16}$$
- b)  Se pregunta $$\begin{align}P(N(1/7)\ge 1) =\,&  1-P(N(1/7)\lt 1) \\=\,& 1-P(N(1/7)=0) \\=\,& 1- e^{\large -2\cdot 1/7} \end{align}$$
- c) Sabiendo que $N_A(t) \,|\, N(t)=n \sim \mathcal{B}(n,p)$, con $p=3/4$. Se pregunta $$\begin{align} P(N_A(4)\le 2 \,|\, N(4)=6) =\,& \sum_{k=0}^2 {P(N_A(4)=k \,|\, N(4)=6)} \\=\,& \sum_{k=0}^2 \binom{6}{k}(3/4)^k(1-3/4)^{6-k} \end{align}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 14</u> ([[#^indice|Índice]])
^ejercicio14

<u>Enunciado:</u> En una estación de servicio, los clientes llegan de acuerdo con un proceso de Poisson no homogéneo con función de intensidad $$\lambda(t)=3+\frac{4}{t+1}\qquad t\gt0,\qquad\text{donde }t\text{ se mide en horas}$$
- a) ¿Cuál es la probabilidad que lleguen $5$ clientes en la primera hora?.
- b) Si llegaron $8$ clientes en las dos primeras horas, ¿Cuál es la probabilidad que hayan llegado $5$ clientes en la segunda hora?

<u>Solución:</u>

Sea el Proceso de Poisson $N(t)$ que cuenta la cantidad de clientes, con función de intensidad $\lambda(t)$.

- a) Se pregunta $P(N(1)=5)$, para ello necesitamos calcular $$\begin{align} m(0,1) =\,& \int_0^1 {3+\frac{4}{t+1}} \,dt \\=\,& 3+4\cdot ln(2) \end{align}$$ ahora, obtenemos $$P(N(1)=5) = e^{\large -m(0,1)}\frac{(m(0,1))^5}{5!} = e^{\large -3+4\cdot ln(2)}\frac{(3+4\cdot ln(2))^5}{5!}$$
- b) Se pregunta $$P(N(2)-N(1)=5 \,|\, N(2)=8) = P(N(1)=3 \,|\, N(2)=8)$$ sabiendo que $N(1) \,|\, N(2)=n \sim \mathcal{B}(n,{\displaystyle \frac{m(0,1)}{m(0,2)}})$, obtenemos, $$P(N(1)=3 \,|\, N(2)=8) = \binom{8}{3}\left( \frac{m(0,1)}{m(0,2)} \right)^3 \left(1- \frac{m(0,1)}{m(0,2)} \right)^5$$, ya tenemos $m(0,1)$, calculamos $$m(0,2) = \int_0^2 {3+\frac{4}{t+1}} \,dt = 6+4\cdot ln(3)$$, luego $$P(N(1)=3 \,|\, N(2)=8) = \binom{8}{3}\left( \frac{3+4\cdot ln(2)}{6+4\cdot ln(3)} \right)^3 \left(1- \frac{3+4\cdot ln(2)}{6+4\cdot ln(3)} \right)^5$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 15</u> ([[#^indice|Índice]])
^ejercicio15

<u>Enunciado:</u>  Los reclamos a una empresa se reciben de acuerdo a un proceso de Poisson no homogéneo $N_t$ , $t \ge 0$ ($t$ en horas), con intensidad $$\lambda(t)=\large\begin{cases} \frac{1}{2}t&\text{para }0\lt t\le 5 \\ \\ \frac{t+5}{4}&\text{para }t\ge 5 \end{cases}$$
- a) Calcular la probabilidad de que hayan recibido exactamente $15$ reclamos en las primeras $4$ horas.
- b) Calcular la probabilidad de que hayan recibido exactamente $15$ reclamos en $(1, 5]$.
- c) Dado que en las primeras $4$ horas se recibieron $15$ reclamos, calcular la probabilidad de que el número de reclamos ascienda a $16$ a la hora $6$.

<u>Solución:</u>

Sea el Proceso de Poisson $N(t)$ aquel que cuenta la cantidad de reclamos que recibe la empresa, con función de intensidad $\lambda(t)$.

- a) Se pregunta $P(N(4)=15)$, necesitamos $$m(0,4)=\int_0^4 {\frac{1}{2} t} \,dt = 4$$por lo tanto, $$P(N(4)=15) = e^{\large -4}\frac{4^{15}}{15!}$$
- b) Se pregunta $P(N(5)-N(1)=15)$, necesitamos $$m(1,5)=\int_1^5 {\frac{1}{2}t} \,dt = 6$$por lo tanto, $$P(N(5)-N(1)=15) = e^{\large -6}\frac{6^{15}}{15!}$$
- c) Se pregunta $$\begin{align}P(N(6)=16 \,|\, N(4)=15) =\,& P(N(6)-N(4)=16-15 \,|\, N(4)=15) \\=\,& P(N(6)-N(4)=1 \,|\, N(4)=15) \\=\,& P(N(6)-N(4)=1) \end{align}$$necesitamos $$\begin{align}m(4,6) =\,& \int_4^6 {\lambda(t)} \,dt \\=\,& \int_4^5 {\frac{1}{2}t} \,dt + \int_5^6 {\frac{t+5}{4}} \,dt \\=\,& \frac{9}{4} + \frac{21}{8} \\=\,& \frac{39}{8} \end{align}$$entonces, $$P(N(6)-N(4)=1) = e^{\large -38/8}\frac{38}{8}$$

___
<div style="page-break-after: always;"></div>

## <u>Ejercicio 16</u> ([[#^indice|Índice]])
^ejercicio16

<u>Enunciado:</u> Sean $N(t)$ y $M(t)$ procesos estocásticos de Poisson homogéneos independientes con tasas $\lambda_1$ y $\lambda_2$ respectivamente por unidad de tiempo.

- a) Demostrar que el proceso $Z(t) = N(t) + M(t)$ es un proceso de Poisson homogéneo con tasa instantánea $\lambda_1 + \lambda_2$.
- b) ¿Qué ocurriría con $Z(t) = N(t) + M(t)$ si los procesos $N(t)$ y $M(t)$ fuesen no homogéneos?


<u>Solución:</u>

Se demuestran ambos ejercicios mediante la comprobación de las propiedades que definen los Procesos de Poisson homogéneos y no homogéneos.

___