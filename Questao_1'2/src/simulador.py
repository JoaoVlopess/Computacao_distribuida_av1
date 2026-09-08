import numpy as np

from src.disponibilidade import validar_parametros


def simular_disponibilidade(
    n: int,
    k: int,
    p: float,
    rodadas: int = 100_000,
    rng=None
) -> float:
    """
    Simula a disponibilidade de um serviço replicado.

    Para cada rodada:
    1. Gera um valor aleatório para cada servidor.
    2. Se o valor for menor que p, o servidor é considerado disponível.
    3. Conta quantos servidores estão disponíveis.
    4. O serviço funciona se a quantidade disponível for >= k.

    Retorna a proporção de rodadas em que o serviço esteve disponível.
    """

    validar_parametros(n, k, p)

    if rodadas <= 0:
        raise ValueError("O número de rodadas deve ser maior que zero.")

    if rng is None:
        rng = np.random.default_rng()

    # Matriz:
    # linhas = rodadas
    # colunas = servidores
    numeros_aleatorios = rng.random((rodadas, n))

    # True significa servidor disponível
    servidores_disponiveis = numeros_aleatorios < p

    # Conta quantos servidores estão disponíveis em cada rodada
    quantidade_disponivel = servidores_disponiveis.sum(axis=1)

    # O serviço funciona quando pelo menos k servidores estão disponíveis
    servico_disponivel = quantidade_disponivel >= k

    # Média de True/False:
    # True = 1
    # False = 0
    disponibilidade_experimental = servico_disponivel.mean()

    return disponibilidade_experimental