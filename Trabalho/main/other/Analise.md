  <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
    </script>

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

Dados T,P, como os tamanho de Text e Pattern, respectivamente. No pior caso temos a chamada **match**(i, j+2) e  **match**(i+1, j), onde podemos definir com base em T e P da seguinte forma

$$\Theta(T - i)\ \ \ \text{e} \ \ \  \Theta(P-2j)$$

Isso pelo fato de P ser decrementado 2 a cada rodada e T 1 a cada rodada neste caso.

Assim, se tomarmos por hipotese que a quantidade de operações da função `IsMatch` é definida por $\begin{pmatrix}i+j \\ i \end{pmatrix}$ Podemos definir a função e complexidade como,

$$\sum_{i=0}^T \sum_{j=0}^\frac{P}{2} \begin{pmatrix}i+j \\ i \end{pmatrix} \Theta(T-i+P-2j)$$

Dai,

$$\Rightarrow \Theta(T+P)\sum_{i=0}^T \sum_{j=0}^\frac{P}{2} \begin{pmatrix}i+j \\ i \end{pmatrix}$$

onde, utilizando a propriedade $\sum^n_{i=0} \begin{pmatrix}n\\i\end{pmatrix} = 2^n$, temos


$$\Rightarrow O(\ (T+P)\cdot 2^{T+\frac{P}{2}})$$

----------------

Para o algoritmo com Programação Dinâmica, temos T, P, como tamanhos e os indices i, j, respectivamente. O trabalho para processar match(i,j) é O(1) pelo fato da memorização, assim para $i=0,...,T$ e $j=0, ... ,P$ feito uma vez para cada, logo P e T operações O(1), logo

$$O(TP)$$


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

* $\sum^n_{i=0} \begin{pmatrix}n\\i\end{pmatrix} = 2^n$

---------------------

Forma Básica:  
$$T(N) = c \cdot b ^{aN} \cdot N^d \cdot log^eN$$
$$log(T(N)) = log(c) + a\cdot N \cdot log(b) + d \cdot log(N) + e\cdot log logN$$

$$ \in \begin{cases} \Theta(N) & b^a > 1 \\ \Theta(log N) & b^a=1,\ d>0 \\ \Theta(log log N) & b^a =1,\ d=1 \end{cases} $$