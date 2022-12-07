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

Dados T,P, como os tamanho de Text e Pattern, respectivamente. No pior caso temos a chamada **match**(i, j+2)