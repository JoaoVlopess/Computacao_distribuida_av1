# Exercício 1.2 — Disponibilidade de Serviços Replicados

## Computação Distribuída

Este projeto implementa e analisa a disponibilidade de um serviço replicado em múltiplos servidores, dando continuidade ao Exercício 1.1.

A análise é feita de duas formas:

1. **Cálculo analítico**, utilizando a fórmula matemática deduzida anteriormente.
2. **Simulação estocástica**, utilizando várias rodadas aleatórias para estimar a disponibilidade experimental.

Os resultados são comparados por meio de tabelas e gráficos 2D.

---

## 1. Objetivo

Analisar como a disponibilidade do serviço varia em função de:

- `n`: número total de servidores;
- `k`: número mínimo de servidores necessários;
- `p`: probabilidade de cada servidor estar disponível.

São utilizados principalmente os casos:

```text
k = 1
k = n/2
k = n
```

---

## 2. Fórmula utilizada

Seja `X` o número de servidores disponíveis.

Considerando que cada servidor está disponível independentemente com probabilidade `p`:

```text
X ~ Binomial(n, p)
```

A probabilidade de exatamente `i` servidores estarem disponíveis é:

```text
P(X = i) = C(n, i) * p^i * (1-p)^(n-i)
```

Como o serviço funciona quando pelo menos `k` servidores estão disponíveis:

```text
A(n, k, p) =
Σ[i=k até n] C(n, i) * p^i * (1-p)^(n-i)
```

### Casos extremos

Para `k = 1`:

```text
A(n, 1, p) = 1 - (1-p)^n
```

Para `k = n`:

```text
A(n, n, p) = p^n
```

Para o caso `k = n/2`, quando `n` é ímpar, é utilizado:

```text
k = ceil(n/2)
```

---

## 3. Estrutura do projeto

```text
exercicio_1_2/
│
├── main.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── disponibilidade.py
│   ├── simulador.py
│   ├── experimento.py
│   └── graficos.py
│
└── resultados/
    ├── tabelas/
    └── graficos/
```

### Arquivos

- `disponibilidade.py`: implementa o cálculo analítico.
- `simulador.py`: executa a simulação estocástica.
- `experimento.py`: compara os resultados analíticos e experimentais.
- `graficos.py`: gera os gráficos.
- `main.py`: executa todo o experimento.

---

## 4. Simulação estocástica

Em cada rodada da simulação:

1. É gerado um número aleatório entre `0` e `1` para cada servidor.
2. Se o valor for menor que `p`, o servidor é considerado disponível.
3. Conta-se quantos servidores estão disponíveis.
4. O serviço funciona caso a quantidade seja maior ou igual a `k`.

A disponibilidade experimental é calculada por:

```text
Disponibilidade experimental =
rodadas bem-sucedidas / total de rodadas
```

Por padrão, são utilizadas:

```text
100.000 rodadas
```

Também é utilizada uma semente fixa:

```python
seed = 42
```

para permitir a reprodução dos resultados.

---

## 5. Parâmetros analisados

Os valores utilizados para `n` são:

```python
[1, 2, 4, 8, 16]
```

Os valores de `p` variam entre:

```text
0 e 1
```

em intervalos de `0.05`.

Para cada valor de `n`, são analisados os casos:

```text
k = 1
k = ceil(n/2)
k = n
```

---

## 6. Dependências

O projeto utiliza:

- Python
- NumPy
- Pandas
- Matplotlib

Instale as dependências com:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém:

```text
numpy
pandas
matplotlib
```

---

## 7. Execução

Na pasta raiz do projeto, execute:

```bash
python main.py
```

ou:

```bash
python3 main.py
```

Os resultados serão salvos automaticamente na pasta:

```text
resultados/
```

---

## 8. Resultados

São geradas tabelas com:

- `n`
- `k`
- `p`
- disponibilidade analítica
- disponibilidade experimental
- erro absoluto

O erro é calculado por:

```text
erro = |analítico - experimental|
```

Também são gerados gráficos comparando os resultados teóricos e experimentais.

---

## 9. Análise esperada

### Caso `k = 1`

Quando apenas um servidor precisa estar disponível, aumentar o número de servidores tende a aumentar a disponibilidade do serviço.

```text
A(n, 1, p) = 1 - (1-p)^n
```

### Caso `k = n`

Quando todos os servidores precisam estar disponíveis, aumentar o número de servidores tende a reduzir a disponibilidade.

```text
A(n, n, p) = p^n
```

### Caso `k = n/2`

Apresenta um comportamento intermediário, relacionado à ideia de maioria ou quórum em sistemas distribuídos.

---

## 10. Comparação entre teoria e simulação

Os valores experimentais devem ficar próximos dos valores analíticos.

Quanto maior o número de rodadas, menor tende a ser a diferença entre teoria e simulação.

Por exemplo, para:

```text
n = 3
k = 2
p = 0.9
```

o valor analítico é:

```text
0.972
```

ou:

```text
97,2%
```

A simulação deve produzir um valor próximo desse resultado.

---

## 11. Conclusão

O exercício mostra que a replicação não aumenta a disponibilidade em todos os cenários.

Quando poucos servidores são necessários, a replicação tende a melhorar a disponibilidade. Quando todos os servidores são obrigatórios, o efeito pode ser o contrário.

A comparação entre o cálculo analítico e a simulação também permite verificar experimentalmente o comportamento previsto pela distribuição binomial.