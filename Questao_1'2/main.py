from pathlib import Path

import numpy as np

from src.experimento import executar_experimentos
from src.graficos import (
    grafico_analitico_por_caso,
    grafico_comparacao,
    grafico_erro
)


def main():

    # --------------------------------
    # CONFIGURAÇÕES DO EXPERIMENTO
    # --------------------------------

    valores_n = [
        1,
        2,
        4,
        8,
        16
    ]

    valores_p = np.linspace(
        0,
        1,
        21
    )

    rodadas = 100_000

    seed = 42

    # --------------------------------
    # PASTAS
    # --------------------------------

    pasta_tabelas = Path(
        "resultados/tabelas"
    )

    pasta_graficos = Path(
        "resultados/graficos"
    )

    pasta_tabelas.mkdir(
        parents=True,
        exist_ok=True
    )

    pasta_graficos.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------
    # EXECUTAR EXPERIMENTOS
    # --------------------------------

    print("Executando experimentos...")

    df = executar_experimentos(
        valores_n=valores_n,
        valores_p=valores_p,
        rodadas=rodadas,
        seed=seed
    )

    # --------------------------------
    # SALVAR TABELA COMPLETA
    # --------------------------------

    caminho_csv = (
        pasta_tabelas
        / "resultados_completos.csv"
    )

    df.to_csv(
        caminho_csv,
        index=False
    )

    print(
        f"Tabela salva em: {caminho_csv}"
    )

    # --------------------------------
    # TABELAS SEPARADAS
    # --------------------------------

    df_analitico = df[
        [
            "n",
            "caso",
            "k",
            "p",
            "disponibilidade_analitica"
        ]
    ]

    df_analitico.to_csv(
        pasta_tabelas
        / "resultados_analiticos.csv",
        index=False
    )

    df_simulacao = df[
        [
            "n",
            "caso",
            "k",
            "p",
            "disponibilidade_experimental"
        ]
    ]

    df_simulacao.to_csv(
        pasta_tabelas
        / "resultados_simulacao.csv",
        index=False
    )

    # --------------------------------
    # GRÁFICOS
    # --------------------------------

    casos = [
        "k = 1",
        "k = n/2",
        "k = n"
    ]

    for caso in casos:

        grafico_analitico_por_caso(
            df,
            caso,
            pasta_graficos
        )

        grafico_comparacao(
            df,
            caso,
            pasta_graficos
        )

    grafico_erro(
        df,
        pasta_graficos
    )

    # --------------------------------
    # EXIBIR RESUMO
    # --------------------------------

    print()
    print("Experimento concluído!")
    print()

    print(
        "Erro absoluto médio:",
        df["erro_absoluto"].mean()
    )

    print(
        "Maior erro encontrado:",
        df["erro_absoluto"].max()
    )

    print()
    print(
        "Resultados disponíveis na pasta 'resultados'."
    )


if __name__ == "__main__":
    main()