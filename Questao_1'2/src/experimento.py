import numpy as np
import pandas as pd

from src.disponibilidade import (
    disponibilidade_analitica,
    calcular_k_metade
)

from src.simulador import simular_disponibilidade


def executar_experimentos(
    valores_n,
    valores_p,
    rodadas=100_000,
    seed=42
):
    """
    Executa os experimentos para:

    k = 1
    k = ceil(n/2)
    k = n

    Retorna um DataFrame contendo:
    - n
    - k
    - tipo de k
    - p
    - disponibilidade analítica
    - disponibilidade experimental
    - erro absoluto
    """

    resultados = []

    # Seed fixa para permitir reprodutibilidade
    rng = np.random.default_rng(seed)

    for n in valores_n:

        casos_k = {
            "k = 1": 1,
            "k = n/2": calcular_k_metade(n),
            "k = n": n
        }

        for nome_caso, k in casos_k.items():

            for p in valores_p:

                analitica = disponibilidade_analitica(
                    n=n,
                    k=k,
                    p=p
                )

                experimental = simular_disponibilidade(
                    n=n,
                    k=k,
                    p=p,
                    rodadas=rodadas,
                    rng=rng
                )

                erro_absoluto = abs(
                    analitica - experimental
                )

                resultados.append({
                    "n": n,
                    "caso": nome_caso,
                    "k": k,
                    "p": p,
                    "disponibilidade_analitica": analitica,
                    "disponibilidade_experimental": experimental,
                    "erro_absoluto": erro_absoluto
                })

    return pd.DataFrame(resultados)