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

$$2^{6\cdot log_4(n)+7} \Rightarrow \\ 2^{6\cdot log_4(n)}\cdot 2^7 \rightarrow$$
a expressão $2^{6\cdot log_4(n)}$ ela pode ser modificada usando o $a^{n\cdot b}=(a^n)^b=(a^b)^n$.
 $$2^{6\cdot log_4(n)} \Rightarrow\\ (2^6)^{log_4(n)} \rightarrow (2^2\cdot2^2\cdot2^2)^{log_4(n)} \rightarrow\\ (4\cdot4\cdot4)^{log_4(n)} \rightarrow 4^{log_4(n)}\cdot 4^{log_4(n)}\cdot 4^{log_4(n)}\rightarrow\\ n^{log_4(4)}\cdot n^{log_4(4)}\cdot n^{log_4(4)} \rightarrow n^3$$
 $$\therefore 128\cdot n^3$$

 * $n^{\frac{3}{log_2(n)}}$

$$n^{\frac{3}{log_2(n)}}\Rightarrow $$
* ee

* $\sum_{i=1}^n(2\cdot3^i - 4 \cdot i)$

$$\sum_{i=1}^n(2\cdot3^i - 4 \cdot i)\Rightarrow \sum_{i=1}^n(2\cdot3^i) - \sum_{i=1}^n(4 \cdot i) \rightarrow\\ 2\cdot\sum_{i=1}^n3^i - 4\cdot\sum_{i=1}^n i\rightarrow\\ 2\cdot\sum_{i=1}^n3^i - 4\cdot \frac{n\cdot(n+1)}{2} \rightarrow\\ 2\cdot\sum_{i=1}^n3^i - 4\cdot \frac{n\cdot(n+1)}{2}$$