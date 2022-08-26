# <center> PAA - Atividade 01


1. Nesta questão rodei até o n/2 para rodar uma quantidade menor de vezes, mas para numeros grandes acaba rodando mais que o necessário. O método da fatoração por primos roda menos, mas não temos como obter primos sem fazer um loop.
   
```html
<pre><code>
int SqrtFloor(int n)
   for i from 1  to n/2 do
      if(i*i == n)
        return i;
    throw "without whole roots";
</code></pre>
```
Q2) Nesta questão fiz da forma mais simplificada, onde verifico se o elemento da primeira lista está na segunda de forma que se eu achar eu adiciono ele no meu vetor de resposta, removo usando a função de mover, puxando os elementos das posições seguintes O(m) (porque a ordem importa, não posso remover em O(1)). E paro o loop. Este Algoritmo é acaba se tornando O(nm^2)

```html
<pre><code>
//remover puxando os proximos
void remove(int[] v, int pos) //O(m)
    for i from pos to v.length-1 do
        v[i] =v[i+1];
    v.pop();//remover o ultimo


int[] findRecurrence( int[] v, int[] w) //O(n*m^2)
    int[] res = [] // lista vazia
    for i from 0 to v.length do 
        for j from 0 to w.length do // O(m^2)
            if(v[i]==w[j])
                res.push(v[j]); //adiciono
                remove(w,j); //O(m)
                break
    return res;
</code></pre>
```

3. Solução:
* $a^3\cdot a^5$
$$a^3\cdot a^5 \Rightarrow a^8$$

* $3^a\cdot 5^a$

$$3^a\cdot 5^a \Rightarrow  \\ 3^a\cdot (\frac{3}{3}\cdot 5)^a \rightarrow\\ 3^a\cdot (\frac{15}{3})^a \rightarrow 3^a\cdot \frac{15^a}{3^a} \rightarrow\\ 15^a$$

* $3^a + 5^a$

$$3^a + 5^a$$

* aa


* $2^{6\cdot log_4(n)+7}$

$$2^{6\cdot log_4(n)+7} \Rightarrow \\ 2^{6\cdot log_4(n)}\cdot 2^7 \rightarrow (2^{log_4(n)})^6 \rightarrow\\ (n^{log_4(2)})^6 \rightarrow \\
(2^{\frac{1}{2}})^6 \Rightarrow n^3$$


 * $n^{\frac{3}{log_2(n)}}$

$$n^{\frac{3}{log_2(n)}}\Rightarrow n^{3\cdot \frac{1}{log_2(n)}}$$
apartir deste ponto podemos trabalhar sobre a função $\frac{1}{log_2(n)}$:
$$\frac{1}{log_2(n)}\rightarrow \frac{1}{\frac{log(n)}{log(2)}}\rightarrow \\ \frac{log(2)}{log(n)}\Rightarrow log_n(2)$$
Assim,

$$n^{3\cdot \frac{1}{log_2(n)}}\Rightarrow n^{3\cdot( log_n(2))}\rightarrow \\(n^{log_n(2)})^{3}\rightarrow (2^{log_n(n)})^{3}\rightarrow 2^3 \Rightarrow 8$$

* ee

* $\sum_{i=1}^n(2\cdot3^i - 4 \cdot i)$

$$\sum_{i=1}^n(2\cdot3^i - 4 \cdot i)\Rightarrow \sum_{i=1}^n(2\cdot3^i) - \sum_{i=1}^n(4 \cdot i) \rightarrow\\ 2\cdot\sum_{i=1}^n3^i - 4\cdot\sum_{i=1}^n i\rightarrow\\ 2\cdot\sum_{i=1}^n3^i - 4\cdot \frac{n\cdot(n+1)}{2} \rightarrow\\ 2\cdot(\sum_{i=1}^n3^i) - 4\cdot \frac{n\cdot(n+1)}{2}$$

Daqui, temos $\sum_{i=1}^n3^i$, onde vamos usar, $\sum_{i=0}^{n}a^i = \frac{a^{n+1}-1}{a-1}$ para $a\neq 1$, porém, temos que ajustar o indice de $i=1$, Vou pular o passo e colocar direto a formula, $\sum_{i=1}^{n}a^i = \frac{a(a^{n}-1)}{a-1}$, logo,
$$2\cdot(\sum_{i=1}^n3^i) - 4\cdot \frac{n\cdot(n+1)}{2} \Rightarrow 2\cdot\frac{3(3^{n}-1)}{3-1} - 4\cdot \frac{n\cdot(n+1)}{2}\rightarrow\\ \frac{6(3^{n}-1)}{2} - \frac{4\cdot n\cdot(n+1)}{2}\rightarrow\\ \frac{6(3^{n}-1)- 4\cdot n\cdot(n+1)}{2}\rightarrow\\\frac{6\cdot 3^{n}-6- 4n^2-4n}{2}\rightarrow\\\frac{2\cdot 3^{n+1}-6- 4n^2-4n}{2}$$

4. 
a)Prova por contradição

**Se $p^2$ é par então p é par**

Por contradição temos que mostrar que apartir de $P\rightarrow Q$, onde $Q=F$ e $P=V$, para 

P: "$p^2 = 2m$, $\forall m \in \Z$" e

Q: "$p = 2k$, $\forall k\in \Z$"

Dai, partindo de um p impar, $p=2k+1, \ \ \forall k \in \Z$, aplicado em P, temos que encontrar um número impar. Assim,

$$ p^2 \rightarrow (2k+1)^2 \rightarrow 4k^2+4k+1 \rightarrow \\ 2(2k^+2k) + 1 \Rightarrow p^2 = 2\cdot k'+1$$

Ou seja, $p^2$ é impar, mas isso não pode. Logo contradição.

Outra forma seria,

$$p^2 = 2\cdot m, \ \ \forall m \in \Z \Rightarrow\\
(2k+1)^2 = 2\cdot m \rightarrow 4k^2+4k+1 = 2\cdot m \rightarrow\\ m = \frac{4k^2 + 4k + 1}{2} \rightarrow\\ m = 2k^2 + 2k +\frac{1}{2}$$

Aqui temos que $m \in \R$ e isso é uma contradição com a hipotese.



b)Prova por indução

Provar por indução $S_n = \sum_{i=1}^n  \frac{1}{i(i+1)} = \frac{1}{1.2}+\frac{1}{2.3}+...+\frac{1}{n(n+1)}$

Temos que passar por dois passos, para provar por Indução, base da indução e passo indutivo. Ou seja, testar para o primeiro caso P(0) e achar para os proximos passos apartir dos anteriores P(n+1) = F(P(n)), ou seja, podemos achar o atual como uma função ou operação (F) do anterior.

Esse somatório tem valor 
$$\sum_{i=1}^n \frac{1}{i(i+1)} = \frac{n}{n+1}\\ \Rightarrow P_n = \frac{n}{n+1} \ \forall n\in N$$

Assim,
$$P_0 = \frac{0}{1}$$
$$P_1 = \frac{1}{2}$$

A base é verdadeira. Logo, para $P_k$,
$$P_k = \frac{1}{2}+\frac{1}{6}+...+\frac{1}{k(k+1)} = \frac{k}{k+1}$$
temos,
$$P_{k+1} =  (\frac{1}{2}+\frac{1}{6}+...+\frac{1}{k(k+1)}) + \frac{1}{(k+1)((k+1)+1)}$$
Aqui temos que $P_{k+1}$ em função de $P_k$.
$$P_{k+1} =  P_k + \frac{1}{(k+1)((k+1)+1)}\Rightarrow\\ \frac{k}{k+1} + (\frac{1}{(k+1)((k+1)+1)})\rightarrow\\ \frac{k}{k+1} + \frac{1}{(k+1)(k+2)} \rightarrow\\\frac{k}{k+1}\cdot (\frac{k+2}{k+2}) + \frac{1}{(k+1)(k+2)}\rightarrow\\\frac{k(k+2)}{(k+1)(k+2)} + \frac{1}{(k+1)(k+2)}\rightarrow\\ \frac{k(k+2) + 1}{(k+1)(k+2)}\rightarrow\\\frac{k^2+2k+1}{(k+1)(k+2)}\rightarrow\\ \frac{(k+1)^2}{(k+1)(k+2)}\Rightarrow\\\therefore P_{k+1} =\frac{k+1}{k+2}$$

Usando apenas operações sobre a ideia base achamos o valor de $P_k$, podemos perguntar aqui "ta certo? So vi um monte de conta e não faz sentido", mas está sim, se usarmos, $P_n = \frac{n}{n+1}$, podemos trocar n por n+1 e achar a fórmula esperada.

$$P_{n+1} = \frac{(n+1)}{(n+1)+1}\Rightarrow\\ \therefore P_{n+1} = \frac{n+1}{n+2}$$

Logo está provado.