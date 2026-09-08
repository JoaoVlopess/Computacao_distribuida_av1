from math import comb, ceil


def validar_parametros(n: int, k: int, p: float) -> None:
    """
    Verifica se os parâmetros estão dentro dos limites definidos
    pelo problema.
    """

    if n <= 0:
        raise ValueError("n deve ser maior que 0.")

    if k <= 0 or k > n:
        raise ValueError("k deve satisfazer 0 < k <= n.")

    if p < 0 or p > 1:
        raise ValueError("p deve estar entre 0 e 1.")


def disponibilidade_analitica(n: int, k: int, p: float) -> float:
    """
    Calcula a disponibilidade de um serviço replicado.

    Fórmula:

        A(n, k, p) =
        somatório de i=k até n de:
        C(n, i) * p^i * (1-p)^(n-i)

    onde:
        n = número total de servidores
        k = número mínimo de servidores disponíveis
        p = probabilidade de cada servidor estar disponível
    """

    validar_parametros(n, k, p)

    disponibilidade = 0.0

    for i in range(k, n + 1):
        disponibilidade += (
            comb(n, i)
            * (p ** i)
            * ((1 - p) ** (n - i))
        )

    return disponibilidade


def disponibilidade_k1(n: int, p: float) -> float:
    """
    Caso extremo k = 1.

    Basta pelo menos um servidor estar disponível.

    A = 1 - (1-p)^n
    """

    return 1 - ((1 - p) ** n)


def disponibilidade_kn(n: int, p: float) -> float:
    """
    Caso extremo k = n.

    Todos os servidores precisam estar disponíveis.

    A = p^n
    """

    return p ** n


def calcular_k_metade(n: int) -> int:
    """
    Calcula o valor utilizado para o caso k = n/2.

    Como k precisa ser inteiro, utilizamos ceil(n/2).

    Exemplo:
        n = 10 -> k = 5
        n = 5  -> k = 3
    """

    return ceil(n / 2)