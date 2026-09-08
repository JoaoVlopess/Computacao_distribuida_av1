# Exercício 1.1 — Disponibilidade de Serviços Replicados

## Computação Distribuída

Este exercício tem como objetivo deduzir uma fórmula matemática capaz de calcular a disponibilidade de um serviço replicado em múltiplos servidores.

A disponibilidade depende dos seguintes parâmetros:

- `n`: número total de servidores;
- `k`: número mínimo de servidores disponíveis necessário para o serviço funcionar corretamente;
- `p`: probabilidade de cada servidor estar disponível em um determinado instante.

Assume-se que os servidores possuem comportamentos independentes entre si.

---

## 1. Definição do problema

Cada servidor pode estar em um de dois estados:

```text
Disponível
Indisponível
```

A probabilidade de um servidor estar disponível é:

```text
p
```

Logo, a probabilidade de ele estar indisponível é:

```text
1 - p
```

O serviço é considerado disponível sempre que existirem pelo menos `k` servidores disponíveis entre os `n` servidores existentes.

---

## 2. Caso extremo: k = 1

Quando:

```text
k = 1
```

basta que um único servidor esteja disponível para que o serviço funcione.

A única situação em que o serviço fica indisponível é quando todos os servidores estão indisponíveis ao mesmo tempo.

A probabilidade de um servidor estar indisponível é:

```text
1 - p
```

Como existem `n` servidores independentes, a probabilidade de todos estarem indisponíveis é:

```text
(1 - p)^n
```

Portanto:

```text
P(serviço indisponível) = (1 - p)^n
```

Como a disponibilidade é o complemento da indisponibilidade:

```text
A(n, 1, p) = 1 - (1 - p)^n
```

Logo:

```text
A(n, 1, p) = 1 - (1 - p)^n
```

---

## 3. Caso extremo: k = n

Quando:

```text
k = n
```

todos os servidores precisam estar disponíveis simultaneamente.

Cada servidor possui probabilidade `p` de estar disponível.

Como os servidores são considerados independentes:

```text
A(n, n, p) = p * p * ... * p
```

para `n` servidores.

Portanto:

```text
A(n, n, p) = p^n
```

---

## 4. Caso geral

Agora é necessário encontrar uma expressão capaz de representar qualquer valor de:

```text
1 <= k <= n
```

Seja `X` a quantidade de servidores disponíveis em determinado instante.

Como existem `n` servidores independentes e cada servidor possui probabilidade `p` de estar disponível, a variável `X` segue uma distribuição binomial:

```text
X ~ Binomial(n, p)
```

A probabilidade de exatamente `i` servidores estarem disponíveis é:

```text
P(X = i) = C(n, i) * p^i * (1 - p)^(n - i)
```

onde:

```text
C(n, i)
```

representa a combinação de `n` servidores tomados `i` a `i`.

Essa combinação é calculada por:

```text
C(n, i) = n! / (i! * (n - i)!)
```

---

## 5. Interpretação da fórmula binomial

Na expressão:

```text
P(X = i) = C(n, i) * p^i * (1 - p)^(n - i)
```

cada parte possui um significado.

### C(n, i)

Representa a quantidade de maneiras diferentes de escolher quais `i` servidores estarão disponíveis entre os `n` servidores existentes.

### p^i

Representa a probabilidade de os `i` servidores selecionados estarem disponíveis.

### (1 - p)^(n - i)

Representa a probabilidade de os outros `n - i` servidores estarem indisponíveis.

---

## 6. Disponibilidade do serviço

O serviço não exige necessariamente exatamente `k` servidores.

Ele funciona quando existem **pelo menos `k` servidores disponíveis**.

Portanto:

```text
X >= k
```

Isso significa que são considerados os seguintes casos:

```text
k
k + 1
k + 2
...
n
```

A disponibilidade é então a soma das probabilidades de todos esses casos.

Assim:

```text
A(n, k, p) =
Σ[i = k até n] C(n, i) * p^i * (1 - p)^(n - i)
```

Portanto, a fórmula geral da disponibilidade é:

```text
A(n, k, p) =
Σ[i = k até n] (n! / (i! * (n - i)!)) * p^i * (1 - p)^(n - i)
```

---

## 7. Fórmula final

A disponibilidade de um serviço replicado em `n` servidores, em que pelo menos `k` deles precisam estar disponíveis e cada servidor possui probabilidade `p` de disponibilidade, é dada por:

```text
A(n, k, p) =
Σ[i = k até n] C(n, i) * p^i * (1 - p)^(n - i)
```

com:

```text
n > 0
0 < k <= n
0 <= p <= 1
```

---

## 8. Verificação dos casos extremos

A fórmula geral também deve produzir corretamente os resultados encontrados anteriormente.

### Caso k = n

Se:

```text
k = n
```

a soma possui apenas um termo:

```text
i = n
```

Então:

```text
A(n, n, p) =
C(n, n) * p^n * (1 - p)^0
```

Sabemos que:

```text
C(n, n) = 1
```

e:

```text
(1 - p)^0 = 1
```

Logo:

```text
A(n, n, p) = p^n
```

que é exatamente o resultado obtido anteriormente.

---

### Caso k = 1

Quando:

```text
k = 1
```

o serviço funciona sempre que existe pelo menos um servidor disponível.

A única situação de falha ocorre quando nenhum servidor está disponível.

A probabilidade de isso acontecer é:

```text
(1 - p)^n
```

Logo:

```text
A(n, 1, p) = 1 - (1 - p)^n
```

Novamente, o resultado coincide com o caso extremo obtido inicialmente.

---

## 9. Exemplo numérico

Considere:

```text
n = 3
k = 2
p = 0.9
```

Existem três servidores e pelo menos dois precisam estar disponíveis para que o serviço funcione.

O serviço estará disponível quando:

```text
2 servidores estiverem disponíveis
ou
3 servidores estiverem disponíveis
```

Aplicando a fórmula:

```text
A(3, 2, 0.9) =
C(3, 2) * 0.9^2 * 0.1^1
+
C(3, 3) * 0.9^3 * 0.1^0
```

Calculando as combinações:

```text
C(3, 2) = 3
C(3, 3) = 1
```

Então:

```text
A =
3 * 0.9^2 * 0.1
+
1 * 0.9^3
```

```text
A =
3 * 0.81 * 0.1
+
0.729
```

```text
A =
0.243
+
0.729
```

```text
A = 0.972
```

Portanto:

```text
A = 97,2%
```

A disponibilidade do serviço nesse cenário é de aproximadamente `97,2%`.

---

## 10. Interpretação

Os casos extremos mostram comportamentos diferentes.

Quando:

```text
k = 1
```

basta um servidor estar disponível.

Nesse cenário, adicionar novas réplicas tende a aumentar a disponibilidade do serviço.

Por outro lado, quando:

```text
k = n
```

todos os servidores precisam estar disponíveis.

Nesse caso, adicionar novos servidores tende a reduzir a disponibilidade total, pois existe uma quantidade maior de componentes que precisam estar funcionando simultaneamente.

Para valores intermediários de `k`, o comportamento fica entre esses dois extremos.

---

## 11. Conclusão

A disponibilidade de um serviço replicado pode ser representada por uma distribuição binomial.

A fórmula encontrada foi:

```text
A(n, k, p) =
Σ[i = k até n] C(n, i) * p^i * (1 - p)^(n - i)
```

Ela representa a probabilidade de existirem pelo menos `k` servidores disponíveis entre os `n` servidores do sistema.

Os casos extremos também são obtidos a partir da mesma formulação:

```text
k = 1:
A(n, 1, p) = 1 - (1 - p)^n
```

```text
k = n:
A(n, n, p) = p^n
```

A fórmula deduzida neste exercício serve como base para o Exercício 1.2, no qual a disponibilidade é calculada computacionalmente e comparada com resultados obtidos através de simulação estocástica.