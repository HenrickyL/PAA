<ol>
<li>Análise:]</li>
</ol>
<p>Pode com mais detalhes no GitHub: <a href="https://github.com/HenrickyL/PAA/tree/main/Atividade03">https://github.com/HenrickyL/PAA/tree/main/Atividade03</a></p>
<p>a. Uilizando o "RazãoDobrando" como foi mostrado pelo professor em aula, temos o seguinte código:</p>
<pre><code>
def RazaoDobrando(method):
    N = 25
    prev = 0
    while(True):
        a = [randint(-N,N) for i in range(N)]
        ini = time()
        method(a)
        fin = time()

        t = fin - ini
        if(prev&gt;0): print(t/prev)

        prev =t
        N = 2*N
</code></pre>
<p>Agora para cada algoritmo temos as seguintes entradas</p>
<pre><code>
RazaoDobrando(bubleSort)
------------------------
2.9617202268431
4.021700973352481
4.492263132836058
4.222843415207158
3.9563898829380726
4.067672988690772
4.302464125058466
4.523606225845223
4.4485859334708655
</code></pre>
<pre><code>
RazaoDobrando(mergeSort)
------------------------
1.0162213740458015
1.9647887323943662
2.0041816009557945
1.7495678092399405
2.4320079048689904
2.056460764672093
2.057363200348812
2.18067936474297
2.235665617374218
2.1224032499407377
2.174511169988578
2.1481418416001956
2.1448230314187184
2.1457192011036996
</code></pre>
<p>Para determinar o grau do algoritmo temos que usar a fórmula base: \(T(n) = c\cdot N^d \cdot \log^e(n)\) e apartir dela podemos obter</p>
<p>$$\lim_{n\rightarrow \inf} \dfrac{T(2n)}{T(n)} = 2^d$$</p>
<p>Daqui podemos, apartir dos valores que convergem para cada caso encontrar um valor de <strong>d </strong>que indique o grau da função. Logo para o bubleSort temos que \(2^d = 4\rightarrow d = 2\), assim \(\theta(n^2)\). E para o MergeSorte temos que \(2^d = 2\rightarrow d = 1\), assim \(\theta(n)\) e isso que dizer que no caso médio é aproximdamente linear.</p>
<p> </p>
<p>b. Utilizando como base que para o bubleSort doubrou-se o valor n = 25 cerca de 9 vezes, logo \(25\cdot 2^9 = 12800\)  e 12 vezes \(25\cdot 2^{12} = 102400\) para o MergeSort, vou verificar o valor para um vetor 10 vezes maior para o buble e 13 vezes maior para  o merge em cada caso usando as expressões do item anterior.<br /><br />Neste problema usei a Regressão linear nos dados aplicados no logaritmo como no vídeo do professor, pode ser visto no github, assim,</p>
<p> </p>
<pre><code>
def DrawLogGraphic(file, color='b'):
    title = 'log '+file.replace('.txt','')
    A = np.loadtxt(file)
    x = [i[0] for i in A]
    lx = np.log2(x)   #{----------
    y = [i[1] for i in A]
    ly = np.log2(y)   #{----------

    plt.plot(lx,ly, 'o:',color=color, label=title)
    plt.title(title,fontweight='bold')
    plt.xlabel(r"$\log{N}$")
    plt.ylabel(r"$\log{T(N)}$")
    model = LinearRegression().fit(lx.reshape(-1,1),ly) #{----------
    print('slope:', model.coef_)
    plt.plot(lx, model.intercept_+model.coef_*lx, 'r', label="{a}x^2+{b}".format(b=model.intercept_,a=model.coef_))
    plt.legend()
    plt.show()
    return lambda x: model.intercept_+model.coef_*x #{----------
#Uso --------------------------
FBuble = DrawLogGraphic('bubleSort.txt')
FMerge = DrawLogGraphic('mergeSort.txt')
</code></pre>
<p>aqui apliquei o log nos resultados e retorneu uma função lambda que com um valor x eu retorno o valor y equivalente. (obs: x deve estar no formato log2(x))</p>
<pre><code>
def Estimando(method,N, name):
    a = [randint(-N,N) for i in range(N)]
    ini = time()
    method(a)
    fin = time()
    t = (fin - ini)*1000 #milisegundos
    print("{name} T({n}) = {t}".format(name=name,n=N, t=t))
    return t
</code></pre>
<pre><code>
t = Estimando(bubleSort, 25*(2**10),'BubleSort')
print(np.log2(t))
-------------------------------
BubleSort T(25600) = 68156.08143806458
16.056554771269546
</code></pre>
<pre><code>
t = Estimando(mergeSort,25*(2**13),'MergeSort')
print(np.log2(t))
---------------------------------
MergeSort T(204800) = 785.0098609924316
9.616566966473927
</code></pre>
<pre><code>
FBuble(np.log2(25*(2**10))) # 15.8514046
Merge(np.log2(25*(2**13))) # 9.2896132
</code></pre>
<p>Até aqui foram muitos código e pode ter sido difícil de entender, mas resumindo,<br /><br /></p>
<p>$$f(x) = k_1\cdot x + k_2 \mid x = \log_2 n $$</p>
<p>Onde \(k_1\) e \(k_2\) são os coeficientes de uma reta que define os dois algoritmos. Dai Apartir dos dados obtidos rodando os algoritmos pude gerar gráficos e apicando a regra do logaritmo para obter uma função linear que define o crescimento dos mesmo. E por fim, pude estimar o valor que demoraria os cada algoritmo, como podemos ver</p>
<table class="tg" border="1">
<thead>
<tr><th class="tg-0pky"> </th><th class="tg-fymr">N</th><th class="tg-fymr">\(\log T_m \)</th><th class="tg-fymr">\(T_m\) (ms)</th><th class="tg-fymr">\(\log T_p\)</th><th class="tg-0lax"><span style="font-weight: bold;">\(E_r\) %</span></th></tr>
</thead>
<tbody>
<tr>
<td class="tg-fymr">Buble</td>
<td class="tg-0pky">25600</td>
<td class="tg-0pky">16.099</td>
<td class="tg-0pky">70216.60</td>
<td class="tg-0pky">15.85</td>
<td class="tg-0lax">1.5</td>
</tr>
<tr>
<td class="tg-fymr">Merge</td>
<td class="tg-0pky">204800</td>
<td class="tg-0pky">9.546</td>
<td class="tg-0pky">747.99</td>
<td class="tg-0pky">9.29</td>
<td class="tg-0lax">2.7</td>
</tr>
</tbody>
</table>
<p>Aqui temos a tabela com o log do tempo medido para aplicar na função e o tempo previsto (também em log). E como podemos ver deu para prever com umas porcentagem de erro relativo menor que 5%.</p>
<p> </p>