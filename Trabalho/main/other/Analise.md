# PAA

## Análise Teórica

$$\text{ \textbf{Forma Básica:  }} \  \ c\cdot b^{an}\cdot n^d \cdot \log^e n$$

Ordem de crescimento:

* maior $b^a$
* $b^a$ empata $\Rightarrow$ maior $d$
* $b^a$ e $d$ empata $\Rightarrow$ maior $e$


Se $b^a \ > \ 1 \ \ \Rightarrow T(n)\ \ \text{   Exponencial}$ 


$f(m) \in \Theta(g(n)) \Rightarrow c_1\cdot g(n) \leq f(n) \leq c_2\cdot g(n)$


$f(m) \in O(g(n)) \Rightarrow \exist c > 0 \ \ | \ \ f(n) \leq c\cdot g(n)$

---------------------

**Definição:** Dadas as strings **text** e **pattern** com tamanhos T e P, tal que $t_i$ e $p_j$ são elementos dada as posições, onde 

  * $0 \leq i < T$
  * $0 \leq j < P$
  * **text** é formada por caracteres `{a..z}`
  * **pattern** é formada por caracteres (`a..z, *, .`).
    *  `.` define um caractere qualquer em  (`a..z`)
    *  `*` define 0 ou n repetições do caractere antecessor, este pertencendo a `.` 
  
  Temos que `isMatch(text,pattern)` que retorna `Match(i,j)`, para $i=0$ e $j=0$, e este retorna se **text** é formada por **pattern** através do algoritmo.

----------------

Dados T,P, como os tamanho de Text e Pattern, respectivamente. No pior caso temos a chamada **match**(i, j+2) e  **match**(i+1, j), ou $\Theta(i,j+2)$ e $\Theta(i+1,j)$.

* $\Theta(0,0) = \Theta(0,2) + \Theta(1,0)$
  
  * $\Theta(0,2) = \Theta(0,4) + \Theta(2,2)$
  * $\Theta(1,0) = \Theta(1,2) + \Theta(2,0)$


----------------

### Propriedade da Combinação:

* $\begin{pmatrix}n \\
0 
\end{pmatrix} = 1$

* $\begin{pmatrix}n \\
n 
\end{pmatrix} = 1$

* $\begin{pmatrix}n \\
p
\end{pmatrix} = \begin{pmatrix}n \\
n-p
\end{pmatrix}$

* $\begin{pmatrix}n \\
p
\end{pmatrix} + \begin{pmatrix}n \\
p+1
\end{pmatrix} = \begin{pmatrix}n+1 \\
p+1
\end{pmatrix}$

* $$\sum^n_{i=0} \begin{pmatrix}n\\i\end{pmatrix} = 2^n$$